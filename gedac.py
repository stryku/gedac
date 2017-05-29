#!/usr/bin/python
import sys
import base64


def generate():
    oryginal_file = open(sys.argv[1], 'rb')
    cracked_file = open(sys.argv[2], 'rb')

    oruginal_file_content = oryginal_file.read()
    cracked_file_content = cracked_file.read()

    output = ''

    offset = 0
    for byte in oruginal_file_content:
        if byte != cracked_file_content[offset]:
            output += str(offset) + ' ' + base64.b64encode(cracked_file_content[offset]) + '\n'

        offset += 1

    crack_data_file = open('crack_data.dat', 'w')
    crack_data_file.write(output)


def apply():
    crack_data_file = open('crack_data.dat', 'r')
    oryginal_file = open(sys.argv[1], 'r+b')
    lines = crack_data_file.readlines()

    for line in lines:
        offset = line.split(' ')[0]
        b64_data = line.split(' ')[1]
        oryginal_file.seek(int(offset))
        oryginal_file.write(base64.b64decode(b64_data))

    oryginal_file.close()
    crack_data_file.close()


if len(sys.argv) < 2:
    print("Usage to generate patch: gadec.py oryginal_file cracked_file")
    print("Usage to apply patch: gadec.py oryginal_file")
else:

    if len(sys.argv) == 2:
        apply()
    else:
        generate()
