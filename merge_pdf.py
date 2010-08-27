#!/usr/bin/python

from pyPdf import PdfFileWriter, PdfFileReader
import sys

#Requires Python 2.7
#import argparse
#parser = argparse.ArgumentParser(description="Merges a series of pdf files into a single pdf")
#parser.add_argument('destFile', metavar="D", type=file, nargs='1', help="desired filename of the final merged pdf")
#parser.add_argument('pdfFiles', metavar='I', type=file, nargs='+', 
#            help="filename of a pdf you'd like to merge into the destination")


def merge_pdf(argv=None):
    # Parse arguments
    if argv is None:
        argv = sys.argv

    args = sys.argv[1:]
    
    if len(args) < 2:
        print "Usage: merge_pdf.py dest.pdf input1.pdf...inputn.pdf"
        sys.exit(1)

    dest = args[0]
    pdfFiles = args[1:]

    # Add pages to write
    output = PdfFileWriter()
    outputStream = file(dest, 'wb')

    for f in pdfFiles:    
        inputF = PdfFileReader(file(f, "rb"))
        numPages = inputF.getNumPages()
        
        for pageNum in xrange(numPages):
            output.addPage(inputF.getPage(pageNum))

    # Write output
    output.write(outputStream)
    outputStream.close()

if __name__ == "__main__":
    merge_pdf()

