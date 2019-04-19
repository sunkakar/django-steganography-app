# App 1 for static text encryption in Sonic Pi

from pythonosc import osc_message_builder
from pythonosc import udp_client
from psonic import *


#global key
key = []

#encrypted message to be taken from the front end
def enter_text():

    fileName = input("Please enter the name of text file in .txt format: ")
    fr = open(fileName,'r')
    message = fr.read()
    print(message)
    return message

def assign(num):
    
    if(num==0):
        note = 60
    elif(num==1):
        note = 62
    elif(num==2):
        note = 64
    elif(num==3):
        note = 65
    elif(num==4):
        note = 67
    elif(num==5):
        note = 69
    elif(num==6):
        note = 71
    elif(num==7):
        note = 72

    return note
    

    
def encrypt_text():
    
    melody = []
    melody2 = []
    message = enter_text()
    i = 0
    #ASCII value of the text
    for i in range(len(message)):
        melody.append(int(ord(message[i])))
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
        #sender = udp_client.SimpleUDPClient('localhost', 4559)
        #sender.send_message('/play/note', [70, 100, 8])
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


#global decipher variable
decipher = []

def enter_text():

    fileName = input("Please enter the name of key text file in .txt format for deciphering: ")
    fr = open(fileName,'r')
    line = fr.readline()
    while line:
        value = line.split()
        decipher.append(int(value[0]))
        line = fr.readline()
        
    fr.close()
    
def decode():
    
    asci = []
    #reading key.txt file
    enter_text()
    
    #print(decipher)

    # simply converting the key back to ascii
    for i in range(0, len(decipher)):

        power = 0
        decimal = 0
        octal = decipher[i]
        while(octal>0):

           decimal+= int(octal%10)*(8**power)
           power+=1
           octal= int(octal/10)
           
        asci.append(decimal)
           
    #print(asci)

    #writing the deciphered message inside a new file
    fw = open("decrypted.txt",'w')
    for i in range(0,len(asci)):
        a = chr(asci[i])
        fw.write(a)
decode()


