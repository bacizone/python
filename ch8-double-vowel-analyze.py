def count_syllables_in_word(word):
    count = 0


vowels = 'aeiouAEIOU'
prev_char_was_vowel = False

for char in word:
    if char in vowels:
        if not prev_char_was_vowel:
            count = count + 1
        prev_char_was_vowel = True
    else:
        prev_char_was_vowel = False

return count