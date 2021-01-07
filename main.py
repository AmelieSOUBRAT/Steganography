import png
import argparse
import subprocess

def convertPNGAsGoodFormat(imageFile, alpha):
    '''
    Convert an image in the good format (RGBA/RGB)

            Parameters:
                    imageFile (png.Reader): image convert to be convert on tuple of informations
                    alpha (bool): a boolean value according to the number of planes; 4 is true, 3 is false

            Returns:
                    imageRead (tuple): Tuple of all information on the image file 
    '''

    if alpha:
        imageRead = imageFile.asRGBA()
    else:
        imageRead = imageFile.asRGB()
    return imageRead

def writePNG(textToWrite, imageFileName):
    '''
    Write text in a PNG

            Parameters:
                    textToWrite (string): text to write in the image file in binary
                    imageFileName (string): name of the image file

            Returns:
                    True/False (boolean): True if the text is write in the image file, if not False
    '''

    imageFile = png.Reader(filename=imageFileName)
    imageRead = imageFile.read()

    alpha = imageRead[3]['alpha']
    height = imageRead[1]
    width = imageRead[0]
    greyscale = imageRead[3]['greyscale']
    bitdepth = imageRead[3]['bitdepth']
    planes = imageRead[3]['planes']

    imageRead = convertPNGAsGoodFormat(imageFile, alpha)
   
    listOfPixels = list(imageRead[2])

    arrayOfPixels = []
    for i in range (len(listOfPixels)):
        arrayOfPixels.append([x for x in listOfPixels[i]])
    
    
    if (len(textToWrite) <= height*width*planes):
        for m in range(len(textToWrite)):
            i = int(m / len(arrayOfPixels[0]))
            j = m % len(arrayOfPixels[0])
            stringToList = list(convertIntToBinary(arrayOfPixels[i][j]))
            stringToList[-1] = textToWrite[m]
            listToString = "".join(stringToList)
            arrayOfPixels[i][j] = int(listToString, 2)

        f = open('image_2.png', 'wb')
        w = png.Writer(width, height, greyscale=greyscale, bitdepth=bitdepth, alpha=alpha)
        w.write(f, arrayOfPixels)
        f.close()
        # print("SUCCESS : text is write in the PNG")
        return True
    # print("ERROR : length of the text is too big")
    return False

def readPNG(imageFile):
    '''
    Read text in a PNG

            Parameters:
                    imageFileName (string): name of the image file

            Returns:
                    text (string): text read in the PNG
    '''

    imageFile = png.Reader(filename=imageFile)
    imageRead = imageFile.read()

    alpha = imageRead[3]['alpha']
    imageRead = convertPNGAsGoodFormat(imageFile, alpha)

    listOfPixels = list(imageRead[2])

    arrayOfPixels = []
    for i in range (len(listOfPixels)):
        arrayOfPixels.append([x for x in listOfPixels[i]])

    text = ""
    bitdepth = 0
    letter = []
    for m in range(len(arrayOfPixels) * len(arrayOfPixels[0])):
        i = int(m / len(arrayOfPixels[0]))
        j = m % len(arrayOfPixels[0])
        stringToList = list(convertIntToBinary(arrayOfPixels[i][j]))   
        if bitdepth < 8:
            letter.append(stringToList[-1])
            bitdepth += 1
        if bitdepth == 8:
            listToString = "".join(letter)
            text = text + chr(int(listToString, 2))                
            bitdepth = 0
            letter = []
            if listToString == "00000011":
                break
    return text

def convertIntToBinary(number):
    '''
    Convert an integer in base 2

            Parameters:
                    number (int): a integer to convert

            Returns:
                    binaryNumber (string): the convertion of integer in base 2 with 8 bits.
    '''

    binaryNumber = '{0:08b}'.format(number)
    return binaryNumber

def convertToAsciiBinary(text):
    '''
    Convert an acsii in base 2

            Parameters:
                    text (string): the text to convert

            Returns:
                    binaryText (string): the convertion of the text in base 2 with 8 bits.
    '''

    binaryText = ""
    for letter in text:
        binaryLetter = convertIntToBinary(ord(letter))
        binaryText += binaryLetter
    return binaryText

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description = "Write or read text in a PNG file")
    parser.add_argument("imageFile", type = str, help = "image file to write in it")
    parser.add_argument("-t", type = str, help = "text to write in the PNG")
    parser.add_argument("-f", type = str, help = "file to write in the PNG")
    parser.add_argument("-w", help = "write mode", action = "store_true")
    args = parser.parse_args()

    imageFile = args.imageFile
    if args.w:
        print("Write")
        if args.t:
            text = args.t
        elif args.f:
            textInFile = open(args.f, "r")
            text = textInFile.read()
            textInFile.close()
        else:
            text = input("Enter your text : ")
        
        text = convertToAsciiBinary(text) + "00000011"
        writePNG(text, imageFile)

    else:
        print("Read")
        text = readPNG(imageFile)[ : -1]
        try:
            p1 = subprocess.Popen(["echo", text], stdout = subprocess.PIPE)
            p2 = subprocess.Popen(["strings"], stdin = p1.stdout, stdout = subprocess.PIPE)
            p1.stdout.close()
            output = p2.communicate()[0]
            print(output)
        except:
            print ("Can't read the message")

