from transformers import pipeline, T5ForConditionalGeneration, T5Config

summarizer = pipeline("summarization")
summarizer = pipeline("summarization", model="t5-small")


text = """
Hugging Face is an AI company based in New York and Paris that focuses on Natural Language Processing (NLP).
Their mission is to democratize AI by building an open-source library for NLP. The Hugging Face platform is one of the most widely used tools for building state-of-the-art machine learning models and is used by both academics and industry practitioners.
The Hugging Face Transformers library provides a large number of pre-trained models for a variety of tasks, including text classification, question answering, summarization, and more. The company has grown rapidly and is at the forefront of advancing NLP and AI research.
"""

summary = summarizer(text)
summary  # mirar el tipo de dato type(summary)
summary[0]


# buscar los archivos -----------
import os
os.listdir(os.path.expanduser('~/.cache/huggingface/hub'))
!ls ~/.cache/


# Información sobre los modelos -----------
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
config = model.config
config


translation = pipeline("translation_en_to_fr", model="t5-small")
