import re

# def readTxt(filePath):
    
#     with open(filePath, "r") as file:
#         content = file.read()

#     match = re.search(r"calculate\s+(.*)", content)
#     if match:
#         expression = match.group(1)
#     else:
#         raise ValueError("İfade bulunamadı!")
    
#     return expression

def read_text(content):

    match = re.search(r"interest for\s+(.*)", content)
    if match:
        expression = match.group(1)
        process_interest(expression)
    else:
        match = re.search(r"calculate\s+(.*)", content)
        if match:
            expression = match.group(1)
            process_math(expression)
        else:
            expression = content
            process_math( expression)

def process_interest(expression):
    wordsInter = expression.split()
    resultsInterest = []


    principalIndex = wordsInter.index("principal") #0
    try:
        rateIndex = wordsInter.index("rate") #3
    except:
        rateIndex = wordsInter.index("rates") #3
    durationIndex = wordsInter.index("duration") #6

    principal = text_to_integer(" ".join(wordsInter[principalIndex +1:rateIndex]))
    interestRate = text_to_integer(" ".join(wordsInter[rateIndex+1:durationIndex]))
    duration = text_to_integer(" ".join(wordsInter[durationIndex+1:]))

    interestResult = calculateInterest(principal, interestRate, duration)
    resultsInterest.append(interestResult)
    writeResults(resultsInterest)
    
def process_math(expression):
    words = expression.split()
    results = []

    for index, word in enumerate(words):
        if word == "plus":
            previous = text_to_integer(" ".join(words[:index]))
            next_word = text_to_integer(" ".join(words[index+1:]))
            result = previous + next_word
            results.append(result)

        elif word == "minus":
            previous = text_to_integer(" ".join(words[:index]))
            next_word = text_to_integer(" ".join(words[index+1:]))
            result = previous - next_word
            results.append(result)

        elif word == "times":
            previous = text_to_integer(" ".join(words[:index]))
            next_word = text_to_integer(" ".join(words[index+1:]))
            result = previous * next_word
            results.append(result)

        elif word == "divided" and index < len(words)-1 and words[index+1] == "by":
            previous = text_to_integer(" ".join(words[:index]))
            next_word = text_to_integer(" ".join(words[index+2:]))
            result = previous / next_word
            results.append(result)

    writeResults(results)


def text_to_integer(text):
    try:
        numbers = {
            'zero': 0,'on':1 ,'one': 1, 'two': 2, 'to': 2, 'three': 3, 'tree': 3, 'four': 4, 'for': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
            'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
            'nineteen': 19, 'twenty': 20, 'thirty': 30, 'fourty': 40, 'forty': 40, 'fifty': 50,
            'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
        }

        text = text.lower().replace(" and ", " ")
        parts = text.split(" point ")
        if len(parts) > 1:
            whole, decimal = parts
            decimal = [numbers[word] for word in decimal.split()]
            decimal = sum([num / 100 for i, num in enumerate(decimal)])
        else:
            whole = parts[0]
            decimal = 0
        whole = whole.split()
        num = 0
        group = 0
        for word in whole:
            if word == "hundred":
                group *= 100
            elif word == "thousand":
                group *= 1000
                num += group
                group = 0
            elif word == "million":
                group *= 1000000
                num += group
                group = 0
            else:
                group += numbers[word]
        return num + group + decimal
    except :
        return 0

def calculateInterest(principal, interestRate, duration):
    interest = principal * (interestRate / 100) * duration
    sum = principal + interest
    return sum

def writeResults(results):
    with open("output.txt", "w") as file:
        for result in results:
            file.write(str(result) + "\n")