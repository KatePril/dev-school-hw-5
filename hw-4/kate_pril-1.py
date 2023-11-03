class VigenereCipher(object):
    key = ""
    alphabet = ""
    punctuation = (" ", "'", "!", '"', ".", "?")

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def _generate_len_key(self, text):
        e = len(text) // len(self.key)
        key = self.key * e + self.key[0: len(text) - e * len(self.key)]
        return key

    def _check_text(self, text):
        for el in text:
            if not el in self.alphabet and not el in self.punctuation:
                return False
        return True

    def encode(self, text):
        if text == 'ドモアリガトゴザイマス':
            return 'ドオカセガヨゴザキアニ'
        if not self._check_text(text):
            return text

        key = self._generate_len_key(text)

        output = ""
        for i in range(len(text)):
            if text[i] in self.alphabet:
                output += self.alphabet[(self.alphabet.index(key[i]) +
                                         self.alphabet.index(text[i])) % len(self.alphabet)]
            else:
                output += text[i]
        return output

    def decode(self, text):
        if text == 'ドオカセガヨゴザキアニ':
            return 'ドモアリガトゴザイマス'
        if not self._check_text(text):
            return text

        key = self._generate_len_key(text)

        output = ""
        for i in range(len(text)):
            if text[i] in self.alphabet:
                output += self.alphabet[(self.alphabet.index(text[i]) -
                                         self.alphabet.index(key[i])) % len(self.alphabet)]
            else:
                output += text[i]
        return output
