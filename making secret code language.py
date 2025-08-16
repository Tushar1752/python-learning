#making secret code language
import random
import string
def random_chars():
    return ''.join(random.choice(string.ascii_lowercase, k=3))
def encode_word(word):
    if len(word)>=3:
        word=word[1:] + word[0]
        return random_chars() + word +random_chars()
    else:
        return word[::-1]
def decode_word(word):
    if len(word) >= 9:
        core=word[3:-3]
        return core[-1] + core[:-1]
    else:
        return word[::-1]
def encode_message(message):
    words = message.split()
    return' '.join(decode_word(w) for w in words)

def decoded_message(message):
    words = message.split()
    return ' '.join(decode_word(w) for w in words)



msg = "Hello world my name is Python"
print("Original:",msg)

encoded = encode_message(msg)
print("Encoded:",encoded)
decoded= decoded_message(msg)
print("Decoded:",decoded)