from archive import Archiver

if __name__ == '__main__':
    text = 'bananabanana'
    print('Original text: ', text)
    archive = Archiver.archiver(text, bwt=True)
    print('Compressed text: ', archive)
    unpack = Archiver.unpacker(archive)
    print('Unpacked text: ', unpack)
