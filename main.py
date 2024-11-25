import string

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            first_sentence = text.split('.')[0]
            print('First sentence:', first_sentence)
            return text
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return None

def clean_and_sort(text):
    # Видаляємо пунктуацію
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    # Фільтруємо українські та англійські слова
    ukr_words = [word for word in words if any('\u0400' <= char <= '\u04FF' for char in word)]
    eng_words = [word for word in words if any('a' <= char <= 'z' for char in word.lower())]

    # Сортуємо списки
    ukr_words_sorted = sorted(ukr_words, key=lambda w: w.lower())
    eng_words_sorted = sorted(eng_words, key=lambda w: w.lower())

    # Об'єднуємо результати
    eng_ukr_words = ukr_words_sorted + eng_words_sorted
    print('Sorted words:', eng_ukr_words)

    return len(words)

file_path = 'text.txt'

# Читаємо перше речення
text = read_first_sentence(file_path)
if text:
    # Чистимо текст і сортуємо слова
    word_count = clean_and_sort(text)
    print(f"Total word count: {word_count}")