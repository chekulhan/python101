import transformers

classifier = pipeline("text-classification", model="bert-base-multilingual-cased")
spanish_text = "Me encanta aprender sobre inteligencia artificial."
result = classifier(spanish_text)
print(result)
