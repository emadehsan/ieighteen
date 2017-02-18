
'''
    @author Emad Ehsan
    1. Picks up a line from sourceLang file, e.g. './en/strings.txt'
    2. Request google to translate the query
    3. Creates a file for targetLang, e.g. './ur/strings.txt'
    4. Places translation at exact line number to targetLang file
'''

from html.parser import HTMLParser
import requests
from requests.utils import quote
import binascii

counter = 1
# Locale code of source and target languages
sourceLang = 'en'
targetLang = 'ur'
# Put file name here
filename = 'strings.txt'

'''
    For each line in sourceLang file, getTranslation
    and put translated line targetLang file
'''
def translate(infile, outfile):
    with open(infile) as fin:
        with open(outfile, 'wb') as fout:
            for line in fin:
                outline = bytes(line, 'utf-8')
                # print(line)
                line = line.strip()

                if len(line) == 0:
                    continue

                # now line is prepared to be translated
                translation = getTranslation(line)

                # add new line at the end
                outline = translation + bytes('\n', 'utf-8')
                # save
                fout.write(outline)

'''
    Translates via google translate as described here
    https://ctrlq.org/code/19909-google-translate-api
'''
def getTranslation(sentence):
    global counter, sourceLang, targetLang

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sourceLang
    url = url + "&tl=" + targetLang + "&dt=t&q=" + quote(sentence);

    print('Request# ' + str(counter) + ': ' + url)
    counter += 1

    page = requests.get(url)

    # strip the response to extract urdu text along with quotes
    translation = page.content
    translation = translation[3:]
    removeLast = 16 + len(sentence)
    translation = translation[:-removeLast]

    # still has a trailing comma
    if (translation[-1] == ','):
        translation = translation[:-1]

    return translation

def main():
    global filename

    infile  = './' + sourceLang + '/' + filename
    outfile = './' + targetLang + '/' + filename

    translate(infile, outfile)

main()
