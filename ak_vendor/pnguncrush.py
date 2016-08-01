# ---
# iPIN - iPhone PNG Images Normalizer v1.0
# Copyright (C) 2007
#
# Author:
#  Axel E. Brzostowski
#  http://www.axelbrz.com.ar/
#  axelbrz@gmail.com
#
# References:
#  http://iphone.fiveforty.net/wiki/index.php/PNG_Images
#  http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# ---

# Borrowed from: https://gist.github.com/Moligaloo/4671649

from binascii import crc32
from struct import pack, unpack
from zlib import compress, decompress

PNG_HEADER = b"\x89PNG\r\n\x1a\n"


def pnguncrush(old_png):
    if old_png[:8] != PNG_HEADER:
        return None

    new_png = old_png[:8]

    chunk_pos = len(new_png)
    pendingIDATChunks = []

    # For each chunk in the PNG file
    while chunk_pos < len(old_png):

        # Reading chunk
        chunk_length = old_png[chunk_pos:chunk_pos+4]
        chunk_length = unpack(">L", chunk_length)[0]
        chunk_type = old_png[chunk_pos+4: chunk_pos+8]
        chunk_data = old_png[chunk_pos+8:chunk_pos+8+chunk_length]
        chunk_crc = old_png[chunk_pos+chunk_length+8:chunk_pos+chunk_length+12]
        chunk_crc = unpack(">L", chunk_crc)[0]
        chunk_pos += chunk_length + 12

        # Parsing the header chunk
        if chunk_type == b"IHDR":
            width = unpack(">L", chunk_data[0:4])[0]
            height = unpack(">L", chunk_data[4:8])[0]

        # Parsing the image chunk
        if chunk_type == b"IDAT":
            try:
                # Uncompressing the image chunk
                buf_size = width * height * 4 + height
                if pendingIDATChunks:
                    chunk_data = decompress(
                        b''.join(pendingIDATChunks) + chunk_data, -8, buf_size)
                else:
                    chunk_data = decompress(chunk_data, -8, buf_size)

            except Exception:
                # The PNG image is normalized
                pendingIDATChunks.append(chunk_data)
                continue

            # Swapping red & blue bytes for each pixel
            new_data = b""
            for y in range(height):
                i = len(new_data)
                new_data += to_bytes(chunk_data[i])
                for x in range(width):
                    i = len(new_data)
                    new_data += to_bytes(chunk_data[i + 2])
                    new_data += to_bytes(chunk_data[i + 1])
                    new_data += to_bytes(chunk_data[i + 0])
                    new_data += to_bytes(chunk_data[i + 3])

            # Compressing the image chunk
            chunk_data = new_data
            chunk_data = compress(chunk_data)
            chunk_length = len(chunk_data)
            chunk_crc = crc32(chunk_type)
            chunk_crc = crc32(chunk_data, chunk_crc)
            chunk_crc = (chunk_crc + 0x100000000) % 0x100000000

        # Removing CgBI chunk
        if chunk_type != b"CgBI":
            new_png += pack(">L", chunk_length)
            new_png += chunk_type
            if chunk_length > 0:
                new_png += chunk_data
            new_png += pack(">L", chunk_crc)

        # Stopping the PNG file parsing
        if chunk_type == b"IEND":
            break

    return new_png

def to_bytes(data):
    if type(data).__name__ == 'int':
        return bytes([data, ])
    return data
