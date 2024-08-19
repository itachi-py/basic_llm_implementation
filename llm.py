import re

class simple_tokenizer:
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
        text = re.sub(r'\s+([,.?_!"()\'])', r'\1', text)
        return text
    

"""

Explaination of Regexs:

re.split(r'([,.:;?_!"()\']|--|\s)'

[,.:;?_!"()\'] is the capturing group for all of the
punctuations. Any symbol added within [] is a captured 
punctuation

| is the OR bool in regex, we do |-- to consider, the 
case of -- in the text. Since -- is not a single symbol 
is cannot be included in []

We then do again |\s which means OR whitespace. \s is regex
for whitespace. 

All together, along with the re.split() function, the function
gets splits at any moment regex captures a punctuation, --, 
or a whitespace. 

***************************************************************

re.sub(r'\s+([,.?!"()\'])', r'\1', text)


\s matches the whitespace. + matches one or more.
[,.:;?_!"()\'] is the same capturing group as above. 

\1 refers to the first captured group of the regex. In this case
it is the punctuation. 

All together, we match any punctuation that comes after 1 or more 
whitespace. The whitespace(s) is then substituted by the punctuation
essentially deleting the whitespace between text and the punctuation. 



"""


"""
In this example, we continue with the example 
text, preprocess it and then tokenize. We 
see a list of the Token IDs and then we can 
convert the codes back into text.



"""

# with open("the_verdict.txt", "r", encoding="utf-8") as f:
#     raw_text = f.read()


# preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

# preprocess = [i for i in preprocess if i.strip()]


# all_words = sorted(list(set(preprocess)))

# vocab_list = {token:i for i, token in enumerate(all_words)}

# tokenizer = simple_tokenizer(vocab_list)


# id = tokenizer.encode(raw_text)

# print(id)

# print(tokenizer.decode(id))

"""


"""


class simple_tokenizer_v2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocess = [i.strip() for i in preprocess if i.strip()]
        preprocess = [i if i in self.str_to_int else "<|unk|>" for i in preprocess]
        id = [self.str_to_int[s] for s in preprocess]
        return id

    def decode(self, id):
        text = " ".join([self.int_to_str[i] for i in id])
        text = re.sub(r'\s+([,.?_!"()\'])', r'\1', text)
        return text
    



with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

preprocess = [i for i in preprocess if i.strip()]


all_words = sorted(list(set(preprocess)))

all_words.extend(["<|endoftext|>", "<|unk|>"])

vocab_list = {token:i for i, token in enumerate(all_words)}

tokenizer = simple_tokenizer_v2(vocab_list)



text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))



print(tokenizer.encode(text))

print(tokenizer.decode(tokenizer.encode(text)))

# text = " <|endoftext|> ".join((text1, text2))






# text1 = "Hello, do you like tea?"
# text2 = "In the sunlit terraces of the palace."


# preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', text)

# preprocess = [i for i in preprocess if i.strip()]


# all_words = sorted(list(set(preprocess)))

# vocab_list = {token:i for i, token in enumerate(all_words)}

# tokenizer = simple_tokenizer(vocab_list)

# print(tokenizer.encode(text))

# print(tokenizer.decode(tokenizer.encode(text)))

