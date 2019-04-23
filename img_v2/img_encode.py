from PIL import Image

img_file = "right.png"
encoded_file_name = "encrypted " + img_file
img = Image.open(img_file)
def encrypt_image(img, msg):

    #save length of message too for decoding process
    length = len(msg)
    # use a copy of image to hide the text in
    encrypt = img.copy()
    width, height = img.size
    index = 0
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            # first value is the length of message
            if i == 0 and j == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                #ascii value of text to be encoded
                asc = ord(c)
            else:
                asc = r
            encrypt.putpixel((j, i), (asc, g , b))
            index += 1
    #return encrypted image
    return encrypt

    
encoded_image = encrypt_image(img,"some hidden text, boi!")
#save the encoded file in the same directory
encoded_image.save(encoded_file_name)
