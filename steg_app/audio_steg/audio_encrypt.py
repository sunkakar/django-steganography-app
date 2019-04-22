#from psonic import *

#global notes dictionary
note = {0:60, 1:62, 2:64, 3:65, 4:67, 5:69, 6:71, 7:72}

def audio_encrypt(hiddentext):

    melody = []
    melody2 = []

    #ASCII value of the text
    for i in range(len(hiddentext)):
        melody.append(int(ord(hiddentext[i])))

    #Converting decimal(ASCII) to octal
    for i in range(len(melody)):
        storage = melody[i]
        temp = 0
        temp2 = 1
        while (storage > 0 ):
            temp+= int(storage %8)*temp2
            storage = int(storage/8)
            temp2*=10
        melody2.append(int(temp))

    #in the resulting melody2 list, all the digits of the number are

    print("Decimal ASCII value ",melody)
    print("Octal value - ",melody2)

    return melody2


def music(hiddentext):

    #scal = scale(C4, MAJOR)
    key_copy = audio_encrypt(hiddentext)
    key2 = []
    #dividing the octal values to individual notes
    for i in range(0,len(key_copy)):
        j = 0
        k = key_copy[i]
        l = 0
        while(k > 0):
            j = k%10
            key2.append(j)
            k = k//10
            l+=1
        print("hello" + str(i))

    #play the encrypted text into music(Sonic Pi running in the background)
    sonicpi_output = []
    for notes in key2:
        note_val = note[notes]
        #play(notes2, attack= 0, release= 0.75, amp= 2)
        #sleep(0.25)
        i+=1
        sonicpi_output.append(note_val)

    #generate a key file that can be decoded later
    return (sonicpi_output)


def audio_decrypt(decipher_str):

    asci = []
    decipher_clean = decipher_str.replace("[","")
    decipher_clean = decipher_clean.replace("]","")
    decipher = decipher_clean.split(",")
    list(map(int, decipher))
    output = ""
    # converting the key back to ascii
    for i in range(0,len(decipher)):

        power = 0
        decimal = 0
        octal = int(decipher[i])
        while(octal > 0):

           decimal+= int(octal%10)*(8**power)
           power+=1
           octal= int(octal/10)

        asci.append(decimal)

    print(asci)
    
    for i in range(0,len(asci)):
        output += chr(asci[i])

    return(output)
