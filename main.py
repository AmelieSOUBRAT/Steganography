import png
import argparse

def readFile():
    r = png.Reader(filename='shiba_samuraiNOEL2.png')
    t = r.read()
    print(t[3]['alpha'])
    if t[3]['alpha']:
        print("RGBA")
        t.asRGBA()
    else:
        print("RGB")


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
        readFile()
    if args.f:
        print("f turned on")

    if args.i:
        print("i turned on")