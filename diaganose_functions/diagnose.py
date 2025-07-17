import logging
import pandas as pd
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Cambia el modelo a español
nlp = spacy.load('es_core_news_md')
diagnosis_df = pd.read_pickle("input_data/diagnosis_data.pkl")
symptoms_df = pd.read_pickle("input_data/symptoms.pkl")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
    
logging.basicConfig(
    filename='logging.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)

def encode_symptom(symptom):
    '''
    Convierte el síntoma a vector usando spaCy (español)
    '''
    logging.info(f"Codificando síntoma {symptom}")
    encoded_symptom = nlp(symptom).vector.tolist()
    return encoded_symptom

def create_illness_vector(encoded_symptoms):
    '''
    Compara la lista de síntomas codificados con los síntomas conocidos. Marca los que superan el umbral.
    '''
    threshold = 0.85
    symptoms_df['symptom_flagged'] = 0
    for encoded_symptom in encoded_symptoms:
        symptoms_df['similarity'] = list(cosine_similarity(np.array(encoded_symptom).reshape(1, -1),
                                                           np.array(list(symptoms_df['symptom_vector'])))[0])
        symptoms_df.loc[symptoms_df['similarity'] > threshold, 'symptom_flagged'] = 1
        number_of_symptoms_flagged = len(symptoms_df.loc[symptoms_df['similarity'] > threshold, 'symptom_flagged'])
        logging.info(f"Marcados {number_of_symptoms_flagged} posibles síntomas coincidentes")
    return list(symptoms_df['symptom_flagged'])

def get_diagnosis(illness_vector):
    '''
    Compara el vector de síntomas del usuario con las enfermedades conocidas y genera el diagnóstico.
    '''
    threshold = 0.5
    diagnosis_df['similarity'] = list(cosine_similarity(np.array(illness_vector).reshape(1, -1),
                                                        np.array(list(diagnosis_df['illness_vector'])))[0])
    if len(diagnosis_df.loc[diagnosis_df['similarity'] > threshold]) > 0:
        illness = (
            diagnosis_df.sort_values(by='similarity', ascending=False)['illness']
            .iloc[0]
        )
        logging.info(f"Diagnosticando al usuario con {illness}")
        diagnosis_string = f"Según tus síntomas, podrías tener {illness}"
    else:
        closest_match = (
            diagnosis_df
            .sort_values(by='similarity', ascending=False)[['illness', 'similarity']]
            .head(1)
        )
        logging.info(f"No se pudo encontrar un diagnóstico, la coincidencia más cercana fue {closest_match['illness'].iloc[0]} "
                     f"con {closest_match['similarity'].iloc[0]}")
        diagnosis_string = "Lamentablemente no puedo diagnosticarte con los síntomas proporcionados."
    return diagnosis_string

# NOTA: Para regenerar los archivos pickle en español, asegúrate de que los síntomas y enfermedades estén en español
# y vuelve a procesar los vectores usando este script con el modelo spaCy en español.