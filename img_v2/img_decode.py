from PIL import Image
from img_encode import encoded_file_name

encoded_file_name_cpy = encoded_file_name
img2 = Image.open(encoded_file_name_cpy)

def decrypt_image(img2):
   
    width, height = img2.size
    msg = ""
    index = 0
    #parse the image matrix to retrieve the hidden text
    for i in range(height):
        for j in range(width):
            #extract the ascii value from the pixels
            r, g, b = img2.getpixel((j, i))	
            # extract the length from the first 'R' pixel to parse the message
            if i == 0 and j == 0:
                length = r
            elif index <= length:
                #convert it to original character and fill the message
                msg += chr(r)
            index += 1
    return msg


hidden_text = decrypt_image(img2)
print("Hidden text:\n{}".format(hidden_text))
