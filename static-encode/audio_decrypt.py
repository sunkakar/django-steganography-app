
#global decipher variable
decipher = []

def enter_text(text):

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
           
    print(asci)

    #writing the deciphered message inside a new file
    fw = open("decrypted.txt",'w')
    for i in range(0,len(asci)):
        a = chr(asci[i])
        fw.write(a)


