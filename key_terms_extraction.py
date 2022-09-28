from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer


def lemmatize_list(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in words]


def remove_stopwords_and_punct(words):
    s_words = stopwords.words('english')
    return [w for w in words if w not in s_words and w not in punctuation]


def only_nouns(words):
    nouns = []
    for w in words:
        if nltk.pos_tag([w])[0][1] == 'NN':
            nouns.append(nltk.pos_tag([w])[0][0])
    return nouns


def header_title_dict(root, news):
    for r in root[0]:
        for n in r:
            if n.get('name') == 'head':
                head = n.text
            if n.get('name') == 'text':
                words = word_tokenize(n.text.lower())

                words = lemmatize_list(words)
                words = remove_stopwords_and_punct(words)
                words = only_nouns(words)

        news[head] = words
    return news


def print_headers_and_words(news):
    for k, v in news.items():
        print(f'{k}:')
        print(*list(dict(v).keys()))


def create_five_most_common(news):
    news_words = [' '.join(v) for v in news.values()]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(news_words)
    terms = vectorizer.get_feature_names()

    nouns_only = []
    for art in tfidf_matrix.toarray():
        words = {w: s for s, w in zip(art, terms)}
        words = sorted(words.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        nouns_only.append(words[0:5])

    titles = list(news.keys())
    return {t: n for t, n in zip(titles, nouns_only)}


def main():
    file = 'news.xml'
    root = etree.parse(file).getroot()
    news = {}
    news = header_title_dict(root, news)
    news = create_five_most_common(news)
    print_headers_and_words(news)

    
if __name__=='__main__':
  main()
