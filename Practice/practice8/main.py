import pymorphy2
from collections import Counter
from translate import Translator

with open('dialog.txt', 'r', encoding='utf-8') as file:
    text = file.read()

morph = pymorphy2.MorphAnalyzer()

words = text.split()
normalized_words = [morph.parse(word)[0].normal_form for word in words]

word_counts = Counter(normalized_words)

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

word_dict = {word: count for word, count in sorted_words}

translator = Translator(to_lang='en')

translated_words = {word: translator.translate(word) for word in word_dict.keys()}

result_dict = {word: (translated_words[word], count) for word, count in word_dict.items()}

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write("Исходное слово | Перевод | Количество упоминаний\n")
    for word, (translation, count) in result_dict.items():
        file.write(f"{word} | {translation} | {count}\n")

print("Результаты в result.txt")