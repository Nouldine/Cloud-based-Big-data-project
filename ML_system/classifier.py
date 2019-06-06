from gather_texts import getTexts
from ngrams import classify_text
from ngrams import classify_text
from server import classifyOffWorld

print("Getting text from MongoDB...")
texts = getTexts() #[0: 100]
print("Finished")

print("Concatenating text into a single file..")
texts_list = []
for text in texts:
        texts_list.append( text['feed'] )
print("List created...")
part_list = 250 # int(len(texts_list)/5.0)
big_text = " ".join(texts_list[0:part_list])
big_text2 = " ".join(texts_list[part_list: 2*part_list])
print("Finished")

print("Creating classifications...")
owgrams1, owgrams2 = classifyOffWorld(big_text2)
grams1, grams2 = classify_text(big_text)

# find top 10 of 1-grams and 2-grams
total_grams1 = {}
for gram1 in owgrams1:
        total_grams1[ gram1[0] ] = gram1[1]
total_grams2 = {}
for gram2 in owgrams2:
        total_grams2[ gram2[0] ] = gram2[1]

for gram1 in grams1:
        key = gram1[0]
        if not key in total_grams1.keys():
                total_grams1[key] = gram1[1]
        else:
                total_grams1[key] += gram1[1]
for gram2 in grams2:
        key = gram2[0]
        if not key in total_grams2.keys():
                total_grams2[key] = gram2[1]
        else:
                total_grams2[key] += gram2[1]

grams1 = sorted(total_grams1.items(), key = lambda kv: kv[1])
grams1.reverse()
grams1 = (gram1 for gram1 in grams1[0:10])
grams2 = sorted(total_grams2.items(), key = lambda kv: kv[1])
grams2.reverse()
grams2 = (gram2 for gram2 in grams2[0:10])
print("Finished")

print("Writing classifications to file...")
f = open("classifications.txt", "w")
for gram1 in grams1:
        f.write(gram1[0] + "\n")

for gram2 in grams2:
        f.write(gram2[0] + "\n")
f.close()
print("Finished")




