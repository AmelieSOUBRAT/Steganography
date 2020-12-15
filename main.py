import png
import argparse

def readFile(textToWrite):
    imageFile = png.Reader(filename='shiba_samuraiNOEL2.png')
    imageRead = imageFile.read()
    print(imageRead)

    if imageRead[3]['alpha']:
        imageReadRGBA = imageFile.asRGBA()
        listOfPixels=list(imageReadRGBA[2])
        arrayOfBinaryPixels = []
        for i in range (len(listOfPixels)):
            arrayOfBinaryPixels.append([convertIntToBinary(x) for x in listOfPixels[i]])
        i = 0
        for m in range(len(textToWrite)):
            i = int(m/len(arrayOfBinaryPixels[0]))
            j = m % len(arrayOfBinaryPixels[0])
            # print(arrayOfBinaryPixels[i][j])
            stringToList = list(arrayOfBinaryPixels[i][j])
            stringToList[-1] = textToWrite[m]
            listToString = "".join(stringToList)
            # print(listToString)
            # break
    else:
        print("RGB")

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
        textToWrite = convertToAsciiBinary(args.t)
        readFile(textToWrite)
    if args.f:
        print("f turned on")

    if args.i:
        print("i turned on")