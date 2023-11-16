class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                # Only add 1 if the char isn't a vowel as the str
                # gets shorter by 1 if the vowel is removed so we
                # don't need to increment i
                i += 1
        return self.text

vm = VowelRemover('aeiou')
print(vm.remove_vowels())
