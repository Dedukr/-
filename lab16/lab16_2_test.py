from lab16.lab16_1 import extract_stopwords
import textwrap

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

processed_text = extract_stopwords(text.split())
print(processed_text)

# Запис у новий файл
with open("output_text.txt", "w", encoding="utf-8") as file:
	file.write(textwrap.fill(" ".join(processed_text), 100))

print("Оброблений текст збережено у файлі 'output_text.txt'")
