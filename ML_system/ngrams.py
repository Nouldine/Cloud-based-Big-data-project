
from nltk.corpus import stopwords
from textblob import TextBlob

def removeTwo(text, stop_twowords):
        words = text.split()
        word_list = []
        word1 = ""
        word2 = ""
        for word in words:
                word2 = word1
                word1 = word
                combinedWords = word2 + " " + word1
#               print(combinedWords)
                for combinedStop in stop_twowords:
                        if combinedStop in combinedWords:
#                               print(combinedStop, combinedWords)
                                word1 = ""
                                word2 = ""
                word_list.append(word2)
        word_list.append(word1)
        return " ".join(word_list)

def preprocessText(text):
        # remove stop words
        text = text.lower()
        c_list = []
        for c in text:
                if not c in ["!", ",", ".", "\"", "\'", "»", ";", ":", "(", ")"]:
                        c_list.append(c)
        text = "".join(c_list)

        stop_words = ["s", "nt", "cookies", "game", "box", "torecap", "seasoncareercomplete", "stats", "complete", "nightlycomplete", "go", "games", "week", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "win", "season", "team", "technologies", "log", "logs"]
        stop_twowords = [ "splits log", "score splits", "updated splits", "splits updated" "accept technologies", "personalize experience", "improve personalize", "help make", "website better", "experience advertising", "make website", "advertising purposes", "purposes happy"]
        stop_words.extend(stopwords.words('english'))
        tb = TextBlob(text)
        word_list = (word for word in tb.words if word not in stop_words)
        text = ' '.join(word_list)
        text = removeTwo(text, stop_twowords)
        blob = TextBlob(text)

        return blob

def postprocessGrams(gram_dict, n):
        # get top 10 most popular grams
        gram_dict = sorted(gram_dict.items(), key = lambda kv: kv[1])
        gram_dict.reverse()
        ret_list = [ key for key in gram_dict[0:10]]

        return ret_list

def classify_text(text):
        tb = preprocessText(text)

        grams_1 = {}
        for gram in tb.ngrams(n=1):
                gram_list = " ".join(list(gram))
                if gram_list not in grams_1.keys():
                        grams_1[gram_list] = 1
                else:
                        grams_1[gram_list] += 1
        grams_1 = postprocessGrams(grams_1, 1)

        grams_2 = {}
        for gram in tb.ngrams(n=2):
                gram_list = " ".join(list(gram))
                if gram_list not in grams_2.keys():
                        grams_2[gram_list] = 1
                else:
                        grams_2[gram_list] += 1
        grams_2 = postprocessGrams(grams_2, 2)
        return (grams_1, grams_2)
