# App 1 for static text encryption in Sonic Pi


from psonic import *
from note import assign

#global key
key = []

#encrypted message to be taken from the front end
def enter_text():

    fileName = input("Please enter the name of text file in .txt format: ")
    fr = open(fileName,'r')
    message = fr.read()
    print(message)
    return message
    
    
def encrypt_text(hiddentext):
    
    melody = []
    melody2 = []
    i = 0
    #ASCII value of the text
    for i in range(len(hiddentext)):
        melody.append(int(ord(hiddentext[i])))
        i = i+1

    i = 0

    #Converting decimal(ASCII) to octal
    for i in range(len(melody)):
        storage = melody[i]
        j = 0
        temp = 0
        temp2 = 1
        while (storage > 0 ):
            
            temp+= int(storage %8)*temp2
            storage = int(storage/8)
            temp2*=10

        i = i + 1
        melody2.append(int(temp))

    #in the resulting melody2 list, all the digits of the number are

    print("Decimal ASCII value ",melody)
    print("Octal value - ",melody2)
    
    return melody2


def music():

    scal = scale(C4, MAJOR)
    key_copy = encrypt_text()
    key = key_copy 
    key2 = []
    main_key = []
    #dividing the octal values to individual notes
    for i in range(0,len(key_copy)):
        j = 0
        k = key_copy[i]
        l = 0
        while(k > 0):
            j = (k%10)
            key2.append(j)
            k = int(k/10)
            l+=1
    
        i =i + 1

    #play the encrypted text into music(Sonic Pi running in the background)    
    for i in range(0, len(key2)):
        notes = key2[i]
        notes2 = assign(notes)
        play(notes2, attack= 0, release= 0.75, amp= 2)
        sleep(0.25)
        i+=1
        print(notes2)

    #generate a key file that can be decoded later
    fw = open('key.txt','w')
    for i in range(0, len(key)):
        token = str(key[i])
        fw.write(token+'\n')
        i+=1
    print(key)


music()

