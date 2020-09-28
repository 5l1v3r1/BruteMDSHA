from ext import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--hash", help="Você precisa usar esse argumento para poder setar a hash", type=str)
    parser.add_argument("-m","--mode", help="Usará esse argumento para setar se quer encrypt ou decrypt", type=str)
    parser.add_argument("-t","--type", help="Usará esse argumento para setar o tipo de hash", type=str)
    parser.add_argument("-v","--vebose", type=bool)

    args = parser.parse_args()

    if args.type == "md5":
        if args.mode == "decrypt":
            md5.decrypt(args.hash)

            print(f'\nWordlist Count: {md5.count}')
        else:
            md5.encrypt(args.hash)

    elif args.type == "sha1":
        if args.mode == "decrypt":
            sha1.decrypt(args.hash)
        else:
            sha1.encrypt(args.hash)
    else:
        print("Não trabalho com esse tipo de hash!")