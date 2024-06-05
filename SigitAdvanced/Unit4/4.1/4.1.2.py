def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_words = (words.get(word, word) for word in sentence.split())

    translated_sentence = ''
    translated_words_iter = iter(translated_words)
    for _ in range(len(sentence.split())):
        translated_word = next(translated_words_iter, '')
        translated_sentence += translated_word + ' '

    return translated_sentence.strip()

print(translate("el gato esta en la casa"))