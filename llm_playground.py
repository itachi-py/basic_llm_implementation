import re


with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total no. of characters", len(raw_text))
print(raw_text[:99])

# text = "Hello, world. This, is a test"

# result = re.split(r'([,.:;?_!"()\']\s)', text)

# result = [i for i in result if i.strip()]


#preprocess the text

preprocess = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

preprocess = [i for i in preprocess if i.strip()]

print(preprocess[0:30])



#obtain a set-list of all the unique words in the text
all_words = sorted(list(set(preprocess)))

vocab_list = {token:i for i, token in enumerate(all_words)}

