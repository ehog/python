from pprint import pprint
from wordcloud import WordCloud
import json
import matplotlib.pyplot as plt

keywords = ''
input = '/Users/ehog/AnypointStudio/workspace/metamule/src/main/app/guitar.jpg.json'

with open(input) as data_file:
    json_obj = json.load(data_file)

pprint(json_obj)

for i in json_obj['Labels']:
    for key, value in i.iteritems():
        if key == "Name":
            print value
            keywords+=str(value) + ' '

# Generate a word cloud image
wc = WordCloud().generate(keywords)

# Display the generated image:
plt.imshow(wc, interpolation='bilinear')
wc.to_file('wordcloud.png')
plt.axis("off")
plt.show()
