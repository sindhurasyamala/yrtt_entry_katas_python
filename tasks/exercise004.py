# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.
def pig_it(text):
    text = text.split()
    newlist = []
    newstring=''
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    counter = 0
    for word in text:
        wordlist = list(word)

        for char in wordlist:
            if char not in alpha:
                counter += 1

        newstr = ''.join(wordlist)

        if counter == 0:
            for i in newstr:
                i1 = newstr[1:] + newstr[0] + 'ay'
            newlist.append(i1)
        else:
            for i in newstr:
                i1 = newstr[1: -counter] + newstr[0] + 'ay' + newstr[-counter:]
            newlist.append(i1)

    newstring = ' '.join(newlist)
    return newstring


pig_it("Pig latin is cool")