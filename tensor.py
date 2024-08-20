import torch
from torch.utils.data import Dataset, DataLoader

import tiktoken


"""
class of pytorch Dataset

Our data is primarly determined by our 
1.) text
2.) the method of tokenization
3.) input-target pairs

max and stride are part of the sliding window
and are simply the max amount of context and
the stride to take. Stride is better shown 
with an example below.


"""


class gpt_dataset_v1(Dataset):
    def __init__(self, text, tokenizer, max, stride):
        self.tokenizer = tokenizer
        self.input = []
        self.target = []

        id = tokenizer.encode(text)
        for i in range(0, len(id) - max, stride):
            input_chunk = id[i:i+max]
            target_chunk = id[i+1:i + max + 1]
            self.input.append(torch.tensor(input_chunk))
            self.target.append(torch.tensor(target_chunk))
    
    def __len__(self):
        return len(self.input)
    
    def __getitem__(self, index):
        return self.input[index], self.target[index]
    

"""
dataloader_v1 generates the DataLoader object
The dataloader simply handles dataset shuffling, 
creating batches etc. 

"""

def dataloader_v1(text, batch=4, max=256, stride=128, shuffle=True, drop_last=True):
    tokenizer = tiktoken.get_encoding("gpt2")
    dataset = gpt_dataset_v1(text, tokenizer, max, stride)
    dataloader = DataLoader(dataset, batch_size=batch, shuffle=shuffle, drop_last=drop_last)
    return dataloader


"""
In this example we use the original text. The current parameters in the 
dataloader_v1() are set to do the following:

Processing the raw text to generate input-target pairs in singular batches, 
with a max context of 4 tokens, and a single stride. The data will also not 
be shuffled. 

If we make batch > 1, there will be multiple batches of data in the tensor

If we set stride > 1, then the window will not just shift one token, but multiple 
tokens. 

If shuffle = True then the data would be shuffled in order.

"""


with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


dataloader = dataloader_v1(raw_text, batch=1, max=4, stride=1, shuffle=False)

iteration = iter(dataloader) 
batch_1 = next(iteration)

print(batch_1)

batch_2 = next(iteration)
print(batch_2)


"""
The importance of stride can further be seen here. 

In the first case, the number of batches is 8 while 
the stride is set to 1. Notice how there is a lot 
of overlapping within the data. This would not be 
very useful in training the model to predict the next
word as there is a lot of overlap between the target 
and the input data. 


However, when we increase the stride to 4, we see less 
overlap which is better.

"""


dataloader = dataloader_v1(raw_text, batch=8, max=4, stride=1, shuffle=False)

iteration = iter(dataloader) 
inputs, targets, = next(iteration)
print("Inputs:\n", inputs)
print("\Targets:\n", targets)



dataloader = dataloader_v1(raw_text, batch=8, max=4, stride=4, shuffle=False)

iteration = iter(dataloader) 
inputs, targets, = next(iteration)
print("Inputs:\n", inputs)
print("\Targets:\n", targets)
