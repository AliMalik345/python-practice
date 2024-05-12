import pandas as pd
import string
from operator import itemgetter 

def remove_punctuations(para):
    return para.translate(str.maketrans(" ", " ",string.punctuation))

def count_words(para):
    
    words=para.split()
    make_dict={}
    for word in words:
        make_dict[word]=make_dict.get(word, 0)+1
        
    return make_dict
    
def sort_paragraph(para):
    return sorted(para.items(), key=itemgetter(1), reverse=True)

with open("input.txt", "r") as file:
    paragraph=file.read()
    
    paragraph= remove_punctuations(paragraph.lower())
    
    final_paragraph = sort_paragraph(count_words(paragraph))
    df=pd.DataFrame(final_paragraph)
    
    df.to_csv("sorted_paragraph.csv", index=False)
        
