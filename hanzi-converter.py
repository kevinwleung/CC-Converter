'''
Hanzi-Converter created by Kevin Leung (https://github.com/kevinwleung/)

hanzi-converter.py - A simple Python program that converts Chinese characters to Mandarin, Cantonese, 
Hangeul (Korean) and Vietnamese and Japanese (Onyomi + Kunyomi) readings using data from Unihan. 
Open with Python 3.6.

Data used from official Unihan Code Database: https://www.unicode.org/Public/UCD/latest/

SOURCES:
https://stackoverflow.com/questions/1425493/convert-hex-to-binary
https://stackoverflow.com/questions/45715280/ucs-2-codec-cant-encode-characters-in-position-61-61
'''

from sys import version_info

f = open('data/Unihan_Readings.txt',encoding='UTF-8')
lines = f.readlines()

'''def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))'''

def findDef(string):
    chinChar = string
    # https://stackoverflow.com/questions/45715280/ucs-2-codec-cant-encode-characters-in-position-61-61

    a = chinChar.encode('utf-8')

    # https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    b1 = a[0]

    # only want last 4 bits
    b1 = format(b1, '0>8b')[4:]
    #print(b1)

    # only want last 6 bits
    b2 = a[1]
    b2 = format(b2, '0>8b')[2:]
    #print(b2)

    # only want last 6 bits
    b3 = a[2]
    b3 = format(b3, '0>8b')[2:]
    #print(b3)

    # hex code --> unicode code point
    finalHex = 'U+' + hex(int((b1 + b2 + b3),2))[2:].upper()
    #print(finalHex

    c = '[--]'
    m = '[--]'
    h = '[--]'
    v = '[--]'
    jk = '[--]'
    jo = '[--]'

    for x in range(0, len(lines)):
        if finalHex == lines[x][0:len(finalHex)]:
            if 'kCantonese' == lines[x][len(finalHex)+1:len(finalHex)+11]:
                c = '[' + lines[x][len(finalHex)+12:len(lines[x])-1] + ']'
                
            if 'kMandarin' == lines[x][len(finalHex)+1:len(finalHex)+10]:
                m = '[' + lines[x][len(finalHex)+11:len(lines[x])-1]+ ']'
                
            if 'kHangul' == lines[x][len(finalHex)+1:len(finalHex)+8]:
                h = '['  + lines[x][len(finalHex)+9:len(lines[x])-1] + ']'
            if 'kVietnamese' == lines[x][len(finalHex)+1:len(finalHex)+12]:
                v = '[' + lines[x][len(finalHex)+13:len(lines[x])-1] + ']'
            if 'kJapaneseKun' == lines[x][len(finalHex)+1:len(finalHex)+13]:
                jk = '[' + lines[x][len(finalHex)+14:len(lines[x])-1] + ']'
            if 'kJapaneseOn' == lines[x][len(finalHex)+1:len(finalHex)+12]:
                jo = '[' + lines[x][len(finalHex)+13:len(lines[x])-1] + ']'
    return(c,m,h,v, jk, jo)

def main():
    cant = ''
    mand = ''
    # kor = ''
    while True:
        print('Note: Use spaces to separate words')
        sent = input("Please enter Chinese characters: ")
        for x in range(0,len(sent)):
            if sent[x] == ' ':
                print('----------------------')
                print()
            else: 
                theDef = findDef(sent[x])
                cant = theDef[0]
                mand = theDef[1]
                kor = theDef[2]
                viet = theDef[3]
                jk = theDef[4]
                jo = theDef[5]

                    
                print(sent[x])
                print('MANDO:' + mand + " | " + 'CANTO:' + cant + " | " + 'KOR:' +kor + " | " + "VIET:" + viet)
                print('JPN-On:' + jo + " | " + 'JPN-Kun:' + jk)
                print()


main()
