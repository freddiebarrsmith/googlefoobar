
words = ["z", "yx", "yz"]
alphabet = []
#alphabet is effectively the positional array

#currentletter2 = words[0][1]
currentletter = words[0][0]
relationsarray = [["" for x in xrange(3)] for x in xrange(26)]


###letter####lessthan#####greaterthan
#threedarray[0].append(words[0][0])
lettercount = 0
#print type(words[0][0])
#print type(relationsarray[0][0][0])

relationsarray[0][0] = words[0][0]
relationsarray[1][1] = words[0][0]

lettercount += 1
def order():
    print currentletter
    i = len(words)
    for word in words:
        if word[0] != currentletter:
            #put the word[0] in the greater than array for the currentletter
            #and the converse
            relationsarray[lettercount][][] = word[0]
            previousletter = lettercount - 1
#            relationsarray[previousletter][2] = word[0]
#            relationsarray[currentletter][] = word[0]
            lettercount += 1            
            currentletter = word[0]
            alphabet.append(word[0])

        else:
            if word[1] != currentletter2:
                # put word[1] in the greater than array for the currentletter2
                currentletter2 = word[1]
            else:
                pass

#def shifter():


##in order to shift it properly you need to come up with a way to order the things correctly


##so default behaviour is it shifts by 1 to the left of the thing that it is less than

#### you then scan through the other elements of the array, if there is any occurence of the letter in question then you adapt the shift to correspond with that
#### on finding an occurence of the letter in another letter's array, you move the letter one position to the left (if is less than the letter found)
### or you move the letter one to the right of the found letter (if it is more than the letter found)




#words = ["z", "yx", "yz"]

#[letter][greaterthan][lessthan]
#[z][][z]
#[y][z][]
#[x][][z]

#if you have a seperate list for the actual position of them then that would probs make things a lot easier

#so basically the theory is you have 



print relationsarray
s = ''.join(alphabet)
print s

#you want to also sort on the second letter