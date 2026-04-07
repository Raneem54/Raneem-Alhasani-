vowels=0
word="Vowels"
for char in word:
    if char.lower() in "aeiou":
        vowels=vowels+1
print(vowels)