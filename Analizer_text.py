#Hello!
text = input("Enter text: ")

words = text.split()

total = len(words)
unique = len(set(words))

print(f"\nTotal words: {total}")
print(f"Unique: {unique}")

if not words:
    print("there's nothing to analyze")
    exit()
 
freq = {}

for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1


most_common = max(freq, key=freq.get)
print(f"Самое частое слово {most_common} Встречается {freq[most_common]} раз")


longest = max(words, key= len)
print(f"Самое длинное слово: {len(longest)} букв")

shortest = min(words, key= len)
print(f"Самое короткое словл: {len(shortest)} букв")



print("\nТоп-5 по частоте:")
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_freq[:5]:
   print(f"  {word}: {count} раз")