import tiktoken

"""
https://github.com/openai/tiktoken

Byte pair encoding is a more complicated manner of coding. 
It is easier to use Open AI's tiktoken package. 

"""

tokenizer = tiktoken.get_encoding("gpt2")

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))

id = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

strings = tokenizer.decode(id)

print(id)

print(strings)

