text = input("Enter a paragraph: ")

characters = len(text)
words = len(text.split())
spaces = text.count(" ")

vowels = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1

print("\n--- Text Analysis ---")
print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
print("Spaces:", spaces)