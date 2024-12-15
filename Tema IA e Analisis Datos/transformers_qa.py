
from transformers import pipeline

# Default Model: distilbert-base-uncased-distilled-squad (Distilled BERT model trained on SQuAD dataset).
qa_pipeline = pipeline("question-answering")

context = "La Levenshtein Distance mide el número mínimo de operaciones necesarias para convertir una cadena en otra. FuzzyWuzzy usa este algoritmo para calcular cuánta diferencia hay entre dos cadenas. A medida que la distancia disminuye, la similitud entre las cadenas aumenta."

pregunta = input("¿Qué buscas?")

if pregunta:
    result = qa_pipeline(question = pregunta, context=context)
    st.write(f"Answer: {result['answer']}")
