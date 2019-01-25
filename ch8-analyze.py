import ch1text

def count_sentences(text):
    count = 0

    for char in text:
        if char == '.' or
        char == ';'

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)

    total_sentences = count_sentences(text)

    # print(words)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
    # print(text)

compute_readability(ch1text.text)