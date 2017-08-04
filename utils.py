def parse(filepath):
    import csv
    import itertools
    import nltk

    sentence_start_token = "SENTENCE_START"
    sentence_end_token = "SENTENCE_END"
    
    with open(filepath, 'rb') as f:
        reader = csv.reader(f, skipinitialspace=True)
        reader.next()

        # Split full comments into sentences
        sentences = itertools.chain(*[nltk.sent_tokenize(x[0].decode('utf-8').lower()) for x in reader])

        # Append SENTENCE_START and SENTENCE_END
        sentences = ["%s %s %s" % (sentence_start_token, x, sentence_end_token) for x in sentences]

    return sentences
