# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
def remove_char(s):
    return s[1:-1]



    # https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    return sum(x for x in arr if x > 0)



    # https://www.codewars.com/kata/53369039d7ab3ac506000467
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"



        # https://www.codewars.com/kata/56dec885c54a926dcd001095
def opposite(number):
    return number * -1






7 kyu
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    num_vo = 0
    vo = "aeiou"
    for i in sentence:
        if i in vo:
            num_vo += 1
    return num_vo



    # https://www.codewars.com/kata/546e2562b03326a88e000020
def square_digits(num):
    num_str = str(num)
    squared_digits = ''

    for digit in num_str:
        digit_int = int(digit)
        squared_value = digit_int ** 2
        squared_value_str = str(squared_value)
        squared_digits += squared_value_str

    result = int(squared_digits)

    return result




    # https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(num):
    numlst = num.split()

    intstr = []

    for i in numlst:
        intstr.append(int(i))


    highest = max(intstr)
    lowest = min(intstr)

    return f"{highest} {lowest}"




    # https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    result = []
    for i in l:
        if type(i) is int:
            result.append(i)
    return result
