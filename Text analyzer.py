upper_case=0
lower_case=0
digit=0
vowel=0
consonant=0
punctuation=0
spaces=0
special_character = 0
sentence = input('Enter a paragraph:')

for char in sentence:

    #spce count
    if char==' ':
        spaces=spaces+1
        continue

    #punctuation
    if char=='.' or char==',' or char==';' or char==':' or char=='!' or char=='?':
        punctuation=punctuation+1
        continue

    #Digit count
    if char>='0' and char<='9':
        digit=digit+1
        continue

    if (char>='a' and char<='z') or (char>='A' and char<='Z'):

        #Lower case
        if char>='a' and char<='z':
            lower_case=lower_case+1

        #Upper case
        if char>='A' and char<='Z':
            upper_case=upper_case+1

        #Vowel
        if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u') or (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
            vowel=vowel+1

        #Consonant
        else:
            consonant=consonant+1
        continue

    #Special character
    special_character=special_character+1


print('Lower case=',lower_case)
print('Upper case=', upper_case)
print('Digit=', digit)
print('Vowel=', vowel)
print('Consonant=', consonant)
print('Punctuation=', punctuation)
print('Spaces=', spaces)
print('Special character=', special_character)