
with open('corpus') as f:
    lines = f.readlines()

letters = {}

total = 0

for line in lines:
    s = line.split(' ', 1)[1]
    for n in range(0, len(s)):
        if s[n] != ' ' and s[n] != '\n':
            try:
                letters[s[n]] += 1
            except:
                letters[s[n]] = 1
            total += 1


freq = {}

for c in letters:
    freq[c] = letters[c]/total * 100

t = 0

freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

for c in freq:
    print(c, str(round(freq[c], 3)) + "%")
    t += freq[c]

print(total)
