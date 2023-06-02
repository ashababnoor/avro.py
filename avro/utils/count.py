'''

## Count functions (avro.utils) for avro.py

---

MIT License

Copyright (c) 2022-present HitBlast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


# Import local modules.
from avro import config


# Functions.
def count_vowels(text) -> int:
    '''
    ### Count number of occurrences of vowels in a given string.
    '''

    count = 0
    for i in text:
        if i.lower() in config.AVRO_VOWELS:
            count += 1
    return count


def count_consonants(text) -> int:
    '''
    ### Count number of occurrences of consonants in a given string.
    '''

    count = 0
    for i in text:
        if i.lower() in config.AVRO_CONSONANTS:
            count += 1
    return count
