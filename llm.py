import re

class simple_tokenizer:
    #vocab is a dictionary
    #int_to_str is the inverse dictionary
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocess = [i.strip() for i in preprocess if i.strip()]
        id = [self.str_to_int[s] for s in preprocess]
        return id
    def decode(self, id):
        text = " ".join([self.int_to_str[i] for i in id])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    

        