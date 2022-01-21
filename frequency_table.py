#  @uthor: Dr.-Ing. Joan MOUBA, joan.mouba@gmail.com
import string
import random
from typing import Dict, Iterable
from pprint import pprint


def frequency_table(input_iterable: Iterable) -> Dict:
    """ Build a frequency table of the symbols present in an iterable """
    freq_table = {}
    for symbol in input_iterable:
        if symbol in freq_table:
            freq_table[symbol] += 1
        else:
            freq_table[symbol] = 1
    return freq_table

if __name__ == '__main__':
    char_sequence = random.choices(string.ascii_letters, k=100000)  # generate random data
    freq_table_generated = frequency_table(char_sequence)
    pprint(freq_table_generated)



