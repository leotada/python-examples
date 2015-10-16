from sys import argv
import hashlib
import os

def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def getMD5(arquivos):
    for file in arquivos:
        if os.path.isfile(file):
            print('Filename: %s - MD5: %s' %
                           (file, md5(file)))
        else:
           if not os.path.isdir(file):
               print('O Arquivo não existe')

def main():
    if len(argv) > 1:
        getMD5(argv[1:])
    else:
        print('Uso: BatchMD5 arquivo1 arquivo2...')

if __name__ == '__main__':
    main()
