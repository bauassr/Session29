# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:27:35 2018

"""



from bs4 import BeautifulSoup
import urllib.request
import string
import nltk
from collections import Counter
import matplotlib.pyplot as plt


# Get Raw Text

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")


text = soup.getText()
print(len(text))



#Clean the Text

# Replace MIDDLE DOT with space  

text_bullets_replaced= text.replace(u"\u00B7"," ") # Unicode Character 'MIDDLE DOT' (U+00B7)

print(len(text_bullets_replaced))
text_bullets_replaced[:10000]

# Replace punctuations points in the text with space  

punctuations = string.punctuation
print(len(punctuations))

text_no_punctuations = text_bullets_replaced.translate(str.maketrans(punctuations," "*len(punctuations)))
print(len(text_no_punctuations))
text_no_punctuations[:10000]                                  


# Replace number symbols in the text with space  
numbers = "1234567890"
text_no_numbers = text_no_punctuations.translate(str.maketrans(numbers," "*len(numbers))) 
print(len(text_no_numbers))
text_no_numbers[:10000]   


#Tokenize words

nltk.download('punkt')
words  = nltk.word_tokenize(text_no_numbers) # we can also use wordpunct_tokenize() but we already cleaned the punctuations

print(len(words))
print(words[:100])


# Clean the Tokenized Words List


# Create word list by adding strings which are only alphabets 
words_only = [word for word in words if word.isalpha()] 
print(len(words_only))
print(words_only[:100]) 



# Convert words in the word list into lower case
words_lower = [word.lower() for word in words_only]
print(len(words_lower))
print(words_lower[:100])


# Calculate the Frequency of Words


# Word Frequencies
from collections import Counter
word_freq_counter = Counter(words_lower)
print(len(word_freq_counter))
print(word_freq_counter)

print(word_freq_counter.most_common(50))


# Convert to Dictionary - To Create Dataframe Later


word_freq_dict = dict(word_freq_counter)


#Notes:

#This word count dictionary can then be used to create a pandas dataframe for further manipulation.

#However, notice that we haven't removed ntlk stopwords, nor have we lemmatized or stemmed the words.

# Further Cleaning Using NLTK- Remove Stopwords


# Remove the stopwords
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
print(stopwords)



words_no_stopwords = [word for word in words_lower if word not in stopwords]
print(len(words_no_stopwords))
print(words_no_stopwords[:100])


# Further Cleaning Using NLTK- Lemmatize

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words_lemmatized = [lemmatizer.lemmatize(word) for word in words_no_stopwords]
print(len(words_lemmatized))
print(words_lemmatized[:100])


# Calculate the Frequency of Words


lemmatized_words_freqdist =  nltk.FreqDist(words_lemmatized)
print(len(lemmatized_words_freqdist))
print(lemmatized_words_freqdist.items())



print(lemmatized_words_freqdist.most_common(50))


plt.figure(figsize=(20,5))
lemmatized_words_freqdist.plot(len(lemmatized_words_freqdist.most_common(50)))
plt.show()


# Convert Lemmatized Words FreqDist Object into a Dictionary  

lemmatized_words_freq_dict =  dict(lemmatized_words_freqdist)
print(len(lemmatized_words_freq_dict))
print(lemmatized_words_freq_dict)


#Further Cleaning Using NLTK- Stem (From Word List after removing Stopwords)

# Snowball Stemmer
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english')
words_stemmed = [stemmer.stem(word) for word in words_no_stopwords]
print(len(words_stemmed))
print(words_stemmed[:100])


#Calculate the Frequency of Words

stemmed_words_freqdist =  nltk.FreqDist(words_stemmed)
print(len(stemmed_words_freqdist))
print(stemmed_words_freqdist.items())



print(stemmed_words_freqdist.most_common(50))


import matplotlib.pyplot as plt
plt.figure(figsize=(20,5))
stemmed_words_freqdist.plot(len(stemmed_words_freqdist.most_common(50)))
plt.show()


# Convert Stemmed Words FreqDist Object into a Dictionary  


stemmed_words_freq_dict =  dict(stemmed_words_freqdist)
print(len(stemmed_words_freq_dict))
print(stemmed_words_freq_dict)


