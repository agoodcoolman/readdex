# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binascii

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
    #  read unsigned leb 128
def getleb128string(f, addressoff):
    f.seek(addressoff + 1)
    first = int(str(binascii.b2a_hex(f.read(1))), 16)
    print 'first value=', hex(first), first > 0x7f
    if first != 0:
        pass
    # if first > 0x7f:
    #     first = (first & 0x7f) << 7
    #     f.seek(addressoff + 2)
    #     two = hex(int(binascii.b2a_hex(bytearray(f.read(1))), 16))
    #     first = (two & 0x7f) | first
    #     if two > 0x7c:
    #         f.seek(addressoff + 3)
    #         three = f.read(2)
    #         first = (three & 0x7f) | first << 14
    #         if three > 0x7f:
    #             f.seek(addressoff + 4)
    #             four = f.read(2)
    #             first = (four & 0x7f) | first << 21
    #             if four > 0x7f:
    #                 f.seek(addressoff + 5)
    #                 five = f.read(2)
    #                 first = (five & 0x7f) | (first << 28)

    print "first result", first, str(first)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    f = open(".\\Hello.dex", 'rb', True)

    f.seek(0x38)
    stringidsSize = f.read(4)
    stringidsSize = bytearray(stringidsSize)[::-1]
    stringidsSize = (bytes(stringidsSize))
    stringidsSize = binascii.b2a_hex(stringidsSize)
    stringidsSize = int(str(stringidsSize), 16)
    print 'totalstringsize', stringidsSize

    # read string off addreass
    f.seek(0x3c)
    stringidoff = f.read(4)
    stringidoff = bytearray(stringidoff)[::-1]
    stringidoff = binascii.b2a_hex(bytes(stringidoff))
    stringidoff = hex(int(str(stringidoff), 16))
    print 'stringidoffaddress', stringidoff

    # read string off
    stringDataOffs = []
    for index in range(stringidsSize):
        f.seek(int(stringidoff, 16) + 4 * index)
        stringDataOff = f.read(4)
        stringDataOff = int(str(binascii.b2a_hex(bytes(bytearray(stringDataOff)[::-1]))), 16)
        stringDataOffs.append(stringDataOff)
        print hex(stringDataOff)

    for readIndex in range(len(stringDataOffs)):
        f.seek(stringDataOffs[readIndex])
        # # read string head size
        mutf8zise = f.read(1)
        print 'size=', binascii.b2a_hex(mutf8zise), 'off=', stringDataOffs[readIndex]

        getleb128string(f, stringDataOffs[readIndex])







    f.close();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
