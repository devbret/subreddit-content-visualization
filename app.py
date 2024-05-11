import feedparser
import json
import os
import re
from collections import Counter
from nltk import bigrams, word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')
subreddits = ["https://www.reddit.com/r/example.rss",]
bigram_freq = Counter()
def clean_text(text):
    text = re.sub('<.*?>', '', text)  
    text = re.sub(r'\\u[\dA-Fa-f]{4}', '', text) 
    text = re.sub(r'&#\d+;', '', text)
    text = re.sub('submitted by', '', text, flags=re.IGNORECASE)
    text = re.sub(r'/u/[\w-]+', '', text)
    text = text.replace('[link]', '').replace('[comments]', '')
    return text.strip()
def process_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|\d+|\W+', ' ', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens
def get_bigrams(tokens):
    return bigrams(tokens)
def parse_and_analyze_feed(feed_url):
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        if 'summary' in entry:
            clean_summary = clean_text(entry.summary)
            if clean_summary:
                combined_text = entry.title + ' ' + clean_summary
                tokens = process_text(combined_text)
                post_bigrams = get_bigrams(tokens)
                filtered_bigrams = [bigram for bigram in post_bigrams if not any(word in bigram for word in ["gt", "lt", "x", "b", "p", "n", "e", "g"])]
                bigram_freq.update(filtered_bigrams)
for feed_url in subreddits:
    parse_and_analyze_feed(feed_url)
most_common_bigrams = bigram_freq.most_common(1000)
data_for_d3 = [{'phrase': ' '.join(bigram), 'frequency': freq} for bigram, freq in most_common_bigrams if 'quot' not in bigram]
output_file = 'bigram_frequencies.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data_for_d3, f, indent=4)
print(f"Bigram frequency data saved to {output_file}")
