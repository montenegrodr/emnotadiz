import csv
import unicodedata
import matplotlib.pyplot as plt
    from wordcloud import WordCloud
from nltk.corpus import stopwords

all_stopwords = stopwords.words('portuguese')

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def preprocess(s):
    s = s.lower().replace('&quot;','')
    s = s.decode('utf-8')
    s = remove_accents(s)
    s = [word for word in s.split() if word not in all_stopwords]
    s = ' '.join(s)
    return s

text = ''

with open('./notas.csv', 'r') as f:
    reader = csv.reader(f)
    for c, row in enumerate(reader):
        if c == 0:
            continue
        text += preprocess(row[1]) + '\n'


# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('chart.png')
