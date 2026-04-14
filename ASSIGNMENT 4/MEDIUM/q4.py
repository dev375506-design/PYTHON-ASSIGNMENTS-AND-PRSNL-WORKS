#NAYAK DEV_240280117049
sentence = "Learning Python is fun and rewarding. Python is a great language for beginners."

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)