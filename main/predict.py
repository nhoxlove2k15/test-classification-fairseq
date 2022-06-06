# -*- coding: utf-8 -*-
import clean_text

import numpy as np
from fairseq.data.encoders.fastbpe import fastBPE
from fairseq.data import Dictionary
import argparse
print(111)

path_bert = "../resource/phobert/"

parser = argparse.ArgumentParser()
parser.add_argument('--bpe-codes', 
    default=path_bert + "bpe.codes",
    required=False,
    type=str,
    help='path to fastBPE BPE'
)
args, unknown = parser.parse_known_args()
bpe = fastBPE(args)
# Load the dictionary
vocab = Dictionary()
vocab.add_from_file(path_bert + "dict.txt")
MAX_LEN = 256

def PredictNumbers(text):
  test_id = []
  text = clean_text.clean_text(text)
  subwords = '<s> ' + bpe.encode(text) + ' </s>'
  # subwords =  text
  encoded_sent = vocab.encode_line(subwords, append_eos=True, add_if_not_exist=False).long().tolist()
  test_id.append(encoded_sent)

  return test_id
  # print(predicts)

# predict ==================================================================
# print(text)
