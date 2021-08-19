#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:57:20 2021

Small python program to get length of fasta sequences.

@author: ramiro
"""

import os, argparse
from Bio import SeqIO
import pandas as pd

def main():
    
    parser = argparse.ArgumentParser(description = """This script takes a genome assembly in fasta format and saves a table of fasta sequence lengths""")
    
    parser.add_argument("-g","--input_file", dest="input_file", metavar="input_file", required=True, help="genome assembly input file path")
    parser.add_argument("-o","--output_file", dest="output_file", metavar="output_file", required=True, help="output file path")
    
    args = parser.parse_args()   
    input_file = args.input_file
    output_file = args.output_file
    
    contigs_lengths(input_file, output_file)


def contigs_lengths(input_file, output_file):
    contigs_lengths = {}
    for fasta_seqs in SeqIO.parse(open(input_file), 'fasta'):
        contig = fasta_seqs.id
        length = len(fasta_seqs)
        contigs_lengths.update({contig: length})
    contigs_df = pd.DataFrame.from_dict(contigs_lengths, orient='index', columns=['length (bp)'])
    contigs_df.to_csv(output_file)
    print(contigs_lengths)

if (__name__ == "__main__"):
    main()