#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: kourosh Gerayeli


"""

class Morse():
    def __init__(self, dot='.', dash='-'):
            self.dot = dot
            self.dash = dash


    @property
    # Creating the dictionary for words and numbers
    def codebook(self):
        code = {
            'a' : '.-',
            'b' : '-...',
            'c' : '-.-.',
            'd' : '-..',
            'e' : '.',
            'f' : '..-.',
            'g' : '--.',
            'h' : '....',
            'i' : '..',
            'j' : '.---',
            'k' : '-.-',
            'l' : '.-..',
            'm' : '--',
            'n' : '-.',
            'o' : '---',
            'p' : '.--.',
            'q' : '--.-',
            'r' : '.-.',
            's' : '...',
            't' : '-',
            'u' : '..-',
            'v' : '...-',
            'w' : '.--',
            'x' : '-..-',
            'y' : '-.--',
            'z' : '--..',
            '1' : '.----',
            '2' : '..---',
            '3' :  '...--',
            '4' : '....-',
            '5' : '.....',
            '6' : '-....',
            '7' : '--...',
            '8' : '---..',
            '9' : '----.',
            '0' : '-----'}
        return code
    
    # Defining the encode function
    def encode(self,s):
        code = self.codebook
        encodelist = []
        mylst = list(s)
        for i in mylst:
            if i in code.keys():
                encoded_str = code[i]
                # This part of the code makes the translation if you want to use other
                # argument instead of dash and dots.
                table = encoded_str.maketrans('.-',self.dot + self.dash)
                encodelist.append(encoded_str.translate(table))
            else:
                raise ValueError
        return (encodelist)




    # Defining the decode function
    def decode(self,s):
        code = self.codebook
        last_str = ''
        myval = list(code.values())
        mykey = list(code.keys())
        for i in s:
            # This part of the code makes the translation if you want to use other
            # argument instead of dash and dots.
            table2 = i.maketrans(self.dot + self.dash, '.-')
            i = i.translate(table2)
            if i not in myval:
                raise ValueError('Only dot and dash are allowed!')
            myval.index(i)
            letter = mykey[myval.index(i)]
            last_str += letter
        return last_str



if __name__ == "__main__":
    # You can use your desired argument here (the default are dash and dots).
    my_morse = Morse()
    print(my_morse.encode('sos'))
    print(my_morse.decode(['...', '---', '...']))