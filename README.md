# Rasa Chatbot Médico

Este proyecto es un chatbot médico desarrollado con [Rasa](https://rasa.com/) que permite a los usuarios ingresar síntomas en español y recibir un diagnóstico probable basado en procesamiento de lenguaje natural y aprendizaje automático.

## Características principales
- Procesamiento y comprensión de síntomas en español.
- Diagnóstico basado en similitud semántica usando spaCy y modelos personalizados.
- Acciones personalizadas para lógica de diagnóstico.
- Fácilmente extensible con nuevos síntomas y enfermedades.

## Requisitos previos
- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- [Rasa](https://rasa.com/docs/rasa/installation/)
- [spaCy](https://spacy.io/)

## Instalación
1. **Clona el repositorio:**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd <nombre-de-carpeta>
   ```
2. **Crea un entorno virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Instala el modelo spaCy para español:**
   ```sh
   python -m spacy download es_core_news_md
   ```

## Uso
1. **Entrena el modelo de Rasa:**
   ```sh
   rasa train
   ```
2. **Ejecuta el servidor de acciones personalizadas:**
   ```sh
   rasa run actions
   ```
3. **Inicia el chatbot:**
   ```sh
   rasa shell
   ```

## Estructura del proyecto
- `actions/` — Acciones personalizadas de Rasa (lógica de diagnóstico).
- `diaganose_functions/` — Funciones de procesamiento y diagnóstico.
- `data/` — Datos de entrenamiento de NLU, reglas y stories.
- `input_data/` — Datos serializados de síntomas y diagnósticos.
- `models/` — Modelos entrenados de Rasa.
- `tests/` — Pruebas automáticas.

## Ejemplo de `.gitignore`
```
venv/
.rasa/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
ENV/
.venv/
```

## Créditos y licencia
- Proyecto original de [@ihsan292292](https://github.com/ihsan292292/Rasa-Chatbot)s

