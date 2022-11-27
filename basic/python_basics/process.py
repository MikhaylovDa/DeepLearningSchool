def process(given_list):
    result = []
    for sentence in given_list:
        middle_result = []
        middle_result.append(' '.join([letter for letter in sentence.split() if letter.isalpha()]))
        for word in middle_result:
            result.append(word)
    return result

