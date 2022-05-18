import argparse
import os


def filepath(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)

def parsing():
    parser = argparse.ArgumentParser(usage='python main.py [optionals]',
                                    fromfile_prefix_chars='@',
                                    description='Options below')
    parser.add_argument('-r', '--rows',
                        type=int,
                        default=1920,
                        metavar="",
                        help='Main window width, DEFAULT=1920')
    parser.add_argument('-c', '--columns',
                        type=int,
                        default=1080,
                        metavar="",
                        help='Main window height, DEFAULT=1080')
    parser.add_argument('-f', '--fps',
                        type=float,
                        default=20.0,
                        metavar="",
                        help="Sets the frames per second of programme running, DEFAULT=30.0")
    parser.add_argument('-s', '--scale',
                        type=int,
                        default=20,
                        metavar="",
                        help="Sets the scale for programm running (20 at least for FHD recommended!) DEFAULT=30")
    parser.add_argument('-o', '--offset',
                        type=int,
                        default=1,
                        metavar="",
                        help="Sets the window offset, DEFAULT=1")
    args = parser.parse_args()
    return args