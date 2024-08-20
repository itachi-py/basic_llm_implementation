import tiktoken

"""
https://github.com/openai/tiktoken

Byte pair encoding is a more complicated manner of coding.
It essentially turns repeating pairs of sequences to with 
place holder bytes. For example the word mississippi

"is" occurs the most. Lets make X = is.
mXssXppi

now both "ss" and "pp" are equally frequent. Let's go with ss = Y.

mXYXppi

now pp = Z

mXYXZi

The final result is now compressed to be a smaller string
and is thus more efficent. Furthermore, this compression 
and stroring pairs as new bytes allow language models to 
handle words that are out of vocabulary as each word gets
broken into groups of characters rather than entire strings. 

It is easier to use Open AI's tiktoken package. In the below 
example we see that this is done easily. 

"""

tokenizer = tiktoken.get_encoding("gpt2")

# text1 = "Hello, do you like tea?"
# text2 = "In the sunlit terraces of the palace."
# text = " <|endoftext|> ".join((text1, text2))

# id = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

# strings = tokenizer.decode(id)

# print(id)

# print(strings)

"""
Now we apply the tokenizer to the entire text. We also 
we implement basic input-target pairs. These pairs will 
be important in training the model to be able 
to predict the next word. 

"""

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

encode = tokenizer.encode(raw_text)

sample = encode[50:]

#context is how many words we want the pairs to have

context = 4

"""
Sliding window approach:
x is a sample list from 0 to 4
y is from 1 to 5
"""
x = sample[:context]
y = sample[1:context+1]

print(f"x: {x}")
print(f"y: {y}")


for i in range(1,context +1):
    input = sample[:i]
    target = sample[i]
    print(input, "->", target)

for i in range(1,context +1):
    input = sample[:i]
    target = sample[i]
    print(tokenizer.decode(input), "->", tokenizer.decode([target]))