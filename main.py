import png
import argparse
import subprocess

def convertPNGAsGoodFormat(imageFile, alpha):
    if alpha:
        return imageFile.asRGBA()
    else:
        return imageFile.asRGB()

def writePNG(textToWrite, imageFile):
    imageFile = png.Reader(filename=imageFile)
    imageRead = imageFile.read()
    
    alpha = imageRead[3]['alpha']

    imageRead = convertPNGAsGoodFormat(imageFile, alpha)
    
    listOfPixels = list(imageRead[2])
    arrayOfPixels = []
    for i in range (len(listOfPixels)):
        arrayOfPixels.append([x for x in listOfPixels[i]])
    
    height = imageRead[1]
    width = imageRead[0]*imageRead[3]['planes']
    if (len(textToWrite) <= height*width):

        for m in range(len(textToWrite)):
            i = int(m/len(arrayOfPixels[0]))
            j = m % len(arrayOfPixels[0])
            stringToList = list(convertIntToBinary(arrayOfPixels[i][j]))
            stringToList[-1] = textToWrite[m]
            listToString = "".join(stringToList)
            arrayOfPixels[i][j] = int(listToString, 2)

        f = open('swatch4.png', 'wb')
        w = png.Writer(703, 614, greyscale=False, bitdepth=8, alpha=True)
        w.write(f, arrayOfPixels)
        f.close()
        print("SUCCESS : message is write in the PNG")
        return
    print("ERROR : length of the text is too big")
    return

def readPNG(imageFile):
    imageFile = png.Reader(filename=imageFile)
    imageRead = imageFile.read()

    alpha = imageRead[3]['alpha']
    imageRead = convertPNGAsGoodFormat(imageFile, alpha)

    listOfPixels = list(imageRead[2])

    arrayOfPixels = []
    for i in range (len(listOfPixels)):
        arrayOfPixels.append([x for x in listOfPixels[i]])

    word = ""
    r = 0
    binaryListOnCharacter = []
    for m in range(len(arrayOfPixels)*len(arrayOfPixels[0])):
        # print(m)
        i = int(m/len(arrayOfPixels[0]))
        j = m % len(arrayOfPixels[0])
        stringToList = list(convertIntToBinary(arrayOfPixels[i][j]))   
        if r < 8:
            binaryListOnCharacter.append(stringToList[-1])
            r = r + 1
        if r == 8:
            listToString = "".join(binaryListOnCharacter)
            word = word + chr(int(listToString, 2))                
            r = 0
            binaryListOnCharacter = []
            if listToString == "00000011":
                break
    print("SUCCESS : message was read on the PNG")
    print(word)

def convertIntToBinary(number):
    binary = '{0:08b}'.format(number)
    return binary

def convertToAsciiBinary(text):
    fullBinaryText = ""
    for i in text:
        binaryText = bin(ord(i)).replace('0b', '')
        while len(binaryText) < 8:
            binaryText = '0' + binaryText
        fullBinaryText += binaryText
    return fullBinaryText

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description = '')
    parser.add_argument("imageFile", type = str, help = "image file")
    parser.add_argument("-t", type = str, help = "Text")
    parser.add_argument("-f", type = str, help = "File")
    parser.add_argument("-w", help = "write mode", action = "store_true")
    args = parser.parse_args()

    imageFile = args.imageFile
    if args.w:
        print("ECRITURE \n")
        if args.t:
            text = args.t
        elif args.f:
            print("f turned on")
            textInFile = open(args.f, "r")
            text = textInFile.read()
            textInFile.close()
        else:
            text = input("Enter your message : ")
        
        text = convertToAsciiBinary(text) + "00000011"
        writePNG(text, imageFile)

    else:
        print("LECTURE \n")
        readPNG(imageFile)
    

# ARGPARSE, 
# VERIF LONGUEUR MESSAGE PAR RAPPORT TAILLE IMAGE - 8 (END OF TEXT)
#LECTURE DANS LE FICHIER
#SUBPROCESS

#Verifier pour les guillement