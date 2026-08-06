sentence = input("Enter a sentence: ")

print("Word count:", len(sentence.split()))
print("Character count:", len(sentence))
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())
print("Underscores:", sentence.replace(" ", "_"))
