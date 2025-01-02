import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних даних
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


# Створення файлу з текстом
with open("input_text.txt", "w", encoding="utf-8") as file:
    file.write("""
    Natural language processing (NLP) is a subfield of artificial intelligence that focuses 
    on the interaction between computers and humans using natural language. 
    The ultimate goal of NLP is to enable computers to understand, interpret, and generate human languages.
    """)
# Читання тексту з файлу
with open("input_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Токенізація
tokens = word_tokenize(text)

# Лемматизація
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Стеммінг
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words("english"))
filtered_tokens = [token for token in stemmed_tokens if token.lower() not in stop_words]

# Видалення пунктуації
processed_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Об'єднання результату
processed_text = " ".join(processed_tokens)

# Запис у новий файл
with open("output_text.txt", "w", encoding="utf-8") as file:
    file.write(processed_text)

print("Оброблений текст збережено у файлі 'output_text.txt'")