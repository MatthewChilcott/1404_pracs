input_string = input("Text: ").split()
word_counter_dict = {}
for word in input_string:
    if word in word_counter_dict:
        word_counter_dict[word] += 1
    else:
        word_counter_dict[word] = 1
for word in sorted(word_counter_dict):
    print(word, " : ", word_counter_dict[name])
