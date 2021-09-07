# from .projectivize import trees
from Data.projectivize import trees
from Data.projectivize import heads
from Data.projectivize import is_projective
from Data.projectivize import projectivize

# 0 ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
# 1 FORM: Word form or punctuation symbol.
# 2 LEMMA: Lemma or stem of word form.
# 3 UPOS: Universal part-of-speech tag.
# 4 XPOS: Language-specific part-of-speech tag; underscore if not available.
# 5 FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
# 6 HEAD: Head of the current word, which is either a value of ID or zero (0).
# 7 DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
# 8 DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
# 9 MISC: Any other annotation.

ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7
DEPS = 8
MISC = 9

NUMBER_VALUES = ["Coll", "Count", "Dual", "Grpa", "Grpl",
                 "Inv", "Pauc", "Plur", "Ptan", "Sing", "Tri"]


class Dataset():
    ROOT = ('<root>', '<root>', 0, '<root>', 0)  # Pseudo-root

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'rt', encoding='utf-8') as lines:
            for tree in trees(lines):
                tmp = [Dataset.ROOT]
                pheads = heads(tree)
                if not is_projective(pheads):
                    pheads = projectivize(pheads)

                for i, row in enumerate(tree):
                    row[HEAD] = "%d" % pheads[i+1]

                    number = 0  # Default value, if missing.
                    if "Number=" in row[FEATS]:
                        for nvidx in range(len(NUMBER_VALUES)):
                            num_val = NUMBER_VALUES[nvidx]
                            if f'Number={num_val}' in row[FEATS]:
                                # Note the +1, as 0 is reserved.
                                number = nvidx+1

                    tmp.append(
                        (row[FORM], row[UPOS], int(row[HEAD]), row[LEMMA], number))
                yield tmp


PAD = '<pad>'
UNK = '<unk>'


def make_vocabs(gold_data):
    word_vocab = {PAD: 0, UNK: 1}

    for sentence in gold_data:
        for word, _, _, _, _ in sentence:
            # Make is so that there is only lower case letters
            word = word.lower()
            if not word in word_vocab:
                word_vocab[word] = len(word_vocab)

    return word_vocab
