import png
import argparse

def writePNG(textToWrite):
    imageFile = png.Reader(filename='shiba_samuraiNOEL2.png')
    imageRead = imageFile.read()
    print(imageRead)

    if imageRead[3]['alpha']:
        imageReadRGBA = imageFile.asRGBA()
        listOfPixels=list(imageReadRGBA[2])

        arrayOfPixels = []
        for i in range (len(listOfPixels)):
            arrayOfPixels.append([x for x in listOfPixels[i]])
        
        for m in range(len(textToWrite)):
            i = int(m/len(arrayOfPixels[0]))
            j = m % len(arrayOfPixels[0])

            stringToList = list(convertIntToBinary(arrayOfPixels[i][j]))
            stringToList[-1] = textToWrite[m]
            listToString = "".join(stringToList)
            arrayOfPixels[i][j] = int(listToString, 2)

    # print(arrayOfPixels[0])


    f = open('swatch4.png', 'wb')
    w = png.Writer(703, 614, greyscale=False, bitdepth=8, alpha=True)
    w.write(f, arrayOfPixels)
    f.close()
    # else:
    #     print("RGB")

def readPNG():
    imageFile = png.Reader(filename='swatch4.png')
    imageRead = imageFile.read()
    print(imageRead)

    if imageRead[3]['alpha']:
        imageReadRGBA = imageFile.asRGBA()
        listOfPixels=list(imageReadRGBA[2])

        print(listOfPixels[0][0])

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
                r=0
                binaryListOnCharacter = []
        print (word)

def convertIntToBinary(number):
    binary = '{0:08b}'.format(number)
    return binary

def convertToAsciiBinary(text):
    fullBinaryText = ""
    for i in text:
        binaryText = bin(ord(i)).replace('0b','')
        while len(binaryText) < 8:
            binaryText = '0' + binaryText
        fullBinaryText += binaryText
    return fullBinaryText

if __name__=="__main__": 
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-t", type=str, help="Text")
    parser.add_argument("-f", type=str, help="File")
    parser.add_argument("-i", type=str, help="Image")
    args = parser.parse_args()

    if args.t:
        print("t turned on")
        print(convertToAsciiBinary(args.t))
        # print(convertToAsciiBinary("Ã"))
        textToWrite = convertToAsciiBinary(args.t)
        print("ECRITURE \n")
        writePNG(textToWrite)
        print("LECTURE \n")
        readPNG()
    if args.f:
        print("f turned on")

    if args.i:
        print("i turned on")