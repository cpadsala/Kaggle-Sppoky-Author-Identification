#!/usr/bin/env python
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
#text = open('C:/Users/tankn/PycharmProjects/word_cloud/hpl.txt',encoding='utf-8').read()
text = open('C:/Users/tankn/PycharmProjects/word_cloud/mws.txt',encoding='utf-8').read()
#text = open('C:/Users/tankn/PycharmProjects/word_cloud/eap.txt',encoding='utf-8').read()
#text = open('C:/Users/tankn/PycharmProjects/word_cloud/HPL_test.txt').read()
#text = open('C:/Users/tankn/PycharmProjects/word_cloud/MWS_test.txt').read()
#text = open('C:/Users/tankn/PycharmProjects/word_cloud/EAP_test.txt').read()

# read the mask image
#alice_mask = np.array(Image.open(path.join(d, "3.png")))
alice_mask = np.array(Image.open(path.join(d, "1.png")))
#alice_mask = np.array(Image.open(path.join(d, "2.png")))


#stopwords = set(STOPWORDS)
#stopwords.add(".")

#wc = WordCloud(background_color="LightSkyBlue", mask=alice_mask)
wc = WordCloud(background_color="Pink", mask=alice_mask)
#wc = WordCloud(background_color="Aquamarine", mask=alice_mask)

# generate word cloud
wc.generate(text)

# store to file
#wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
