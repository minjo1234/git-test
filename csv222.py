import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

new = pd.read_csv('crawlingcrime.csv')

nouns_list = []

for item in new['text'][:150]:
    sentence_list = kkma.sentences(item)

    for sentence in sentence_list:
        nouns = kkma.pos(sentence)
        for pos in nouns:
            if pos[1] == 'NNG' or pos[1] == 'NNP':
                nouns_list += [pos[0]]


count = Counter(nouns_list)

wordcloud = WordCloud(width=600, height=600)
wordcloud = wordcloud.generate_from_frequencies(count)
array = wordcloud.to_array()
print(type(array))
print(array.shape)

fig = plt.figure(figsize=(80, 80))
plt.imshow(array, interpolation="bilinear")
plt.show()
