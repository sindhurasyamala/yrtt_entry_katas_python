# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    lis = text.split()

    newlist = []
    for i in lis:
        i1 = i[1:] + i[:1] + 'ay'

        newlist.append(i1)

    newstr = ' '.join(newlist)
    print("Converted string: ", end='')
    print('"', newstr, '"')


str = input("Enter a sentence: ")
pig_it(str)