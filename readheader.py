# -*- coding: UTF-8 -*-
import binascii

def start(file):
    file.seek(0x00);
    magic_mask = file.read(4)
    magic_mask = binascii.b2a_hex(magic_mask)
    magic_mask = str(magic_mask)
    print '文本标识符',magic_mask

    file.seek(0x04)
    magic_mask = file.read(4)
    magic_mask = binascii.b2a_hex(magic_mask)
    magic_mask = str(magic_mask)
    print 'version',magic_mask

    file.seek(0x08)
    magic_mask = file.read(4)
    magic_mask = binascii.b2a_hex(magic_mask)
    magic_mask = str(magic_mask)
    print 'checksum', magic_mask

    file.seek(0x0c)
    magic_mask = file.read(20)
    magic_mask = binascii.b2a_hex(magic_mask)
    magic_mask = str(magic_mask)
    print 'sign', magic_mask

    file.seek(0x20)
    magic_mask = file.read(4)
    magic_mask = bytearray(magic_mask);
    magic_mask = str(magic_mask)[::-1]
    magic_mask = str(binascii.b2a_hex(bytes(magic_mask)))
    print 'filesize', int(magic_mask, 16), 'byte'

    file.seek(0x24)
    header_size = file.read(4)
    header_size = bytearray(header_size)
    header_size = header_size[::-1]

    header_size = binascii.b2a_hex(header_size)
    header_size = str(int(header_size, 16))
    print header_size


    file.seek(0x28)
    header_size = file.read(4)
    header_size = binascii.b2a_hex(header_size)
    print 'endian_tag', header_size

    file.seek(0x2c)
    header_size = file.read(4)
    header_size = binascii.b2a_hex(header_size)
    print 'link_size', header_size

    file.seek(0x30)
    header_size = file.read(4)
    header_size = binascii.b2a_hex(header_size)
    print 'link_off', header_size

    file.seek(0x34)
    header_size = file.read(4)
    header_size = bytearray(header_size)[::-1]
    header_size = binascii.b2a_hex(header_size)
    print 'map_off', str(int (header_size, 16))


if __name__ == '__main__':
    f = open("/Users/jinmingkai/PycharmProjects/readdex/Hello.dex", 'rb', True)
    start(f);
