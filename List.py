acronyms = ['lol', 'brb', 'idk', 'smh']
print(acronyms[0])  # Output: lol
print(acronyms[2])  # Output: idk
acronyms.append('tbh')
print(acronyms) # Output: ['lol', 'brb', 'idk', 'smh', 'tbh']
acronyms.remove('brb')
print(acronyms) # Output: ['lol', 'idk', 'smh', 'tbh']
print(len(acronyms)) # Output: 4
print(acronyms.index('smh')) # Output: 2
acronyms.append('fomo')
print(acronyms) # Output: ['lol', 'idk', 'smh', 'tbh', 'fomo']

print(acronyms[1:4]) # Output: ['idk', 'smh', 'tbh']
for acronym in acronyms:
    print(acronym)
# Output:
# lol
# idk
# smh
# tbh
# fomo
if 'idk' in acronyms:
    print("found idk") # Output: found idk
else:
    print("idk not in the list")