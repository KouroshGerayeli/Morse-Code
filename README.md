# Morse-Code
Morse encoder-decoder with an object-oriented design.

The goal is to implement a class Morse with at least the following two methods: encode and decode. When using the `encode` method, one gives a string of ascii characters, and the encoder returns a list of morse symbols using dash-dot notations (-.). The decode method gets a list of strings of dash-dot notations and concatenates the results in a single string of characters. Only lower-case characters in the English alphabet will be allowed (excluding the numerals from the above table).

Extra points for a checking whether we have lower-case characters from the English alphabet (in case of an encoding) or a list only containing strings with dashes and dots (in case of decoding); throwing a ValueError whenever this is not respected.
Upon testing, an object coder will be instantiated from your Morse class, and your code will be tested by calling coder.encode and coder.decode on some test sequences (unknown to you).

Allow to have other symbols to represents dots and dashes by giving arguments dot and dash during the instantiation of your objects. Take a look at str.maketrans() and str.translate().

The problem was designed by Mr.Ronald Phlypo at UGA-INP Phelma school (2022).
