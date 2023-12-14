def most_frequent_word(paragraph):
    words = paragraph.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common_word = max(word_count, key=word_count.get)
    count = word_count[most_common_word]
    return most_common_word


f = open('sample.txt', 'r')
paragraph = f.readline()
result = most_frequent_word(paragraph)

print(f"The most frequent word is: {result}")

