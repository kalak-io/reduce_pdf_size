#!/usr/bin/env python
# coding: utf-8

import argparse
import os


def reduce_pdf_size():
    try:
        os.system("gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite \
                  -dCompatibilityLevel=1.4 -dPDFSETTINGS={} \
                  -sOutputFile={} {}".format(args.settings, args.output,
                                             args.input))
    except:
        print('error: exception is raised.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str,
                        default='output.pdf',
                        help='Name of the output file')
    parser.add_argument('-i', '--input', type=str,
                        required=True,
                        help='Name of the file to reduce')
    parser.add_argument('-s', '--settings', type=str,
                        default='/screen',
                        choices=['/screen', '/ebook', '/printer', '/prepress'],
                        help='Choose your level of quality')
    args = parser.parse_args()
    reduce_pdf_size()
