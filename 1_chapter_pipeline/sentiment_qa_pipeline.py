from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

# Sentiment analysis pipeline
analyzer = pipeline("sentiment-analysis")

# Specify the model and tokenizer that are compatible
oracle = pipeline(
    task="question-answering", model="distilbert-base-cased-distilled-squad",
    tokenizer="distilbert-base-cased"
)

# Named entity recognition pipeline, passing in a specific model and tokenizer
model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
recognizer = pipeline("ner", model=model, tokenizer=tokenizer)

# Your input dictionary remains the same
input_dict = {
    "question": "What is the colour of the dog?",
    "context": "It was a great story about love and loss. Henry and I took a walk in the park. We saw a dog and a cat. The cat was black and the dog was brown. It was a great day."
}

print(oracle(input_dict))

print(analyzer("This restaurant is awesome"))

print(recognizer("Hugging Face is a French company based in New-York."))
