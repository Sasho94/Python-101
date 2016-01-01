def sum_of_digits(digits):
    result = 0
    for n in range(0, len(digits)):
        result += digits[n]

    return result

# print(sum_of_digits([5, 6]))


def to_digits(dig):
    dg = dig
    i = 0
    ar = []
    while dig != 0:
        dg = dig % 10
        # print(dg)
        ar += [dg]
        dig = dig // 10
        i = i + 1
    return ar
# print(to_digits(1212))


def to_number(digit):
    sum = 0
    lent = len(digit) - 1
    point = 10
    for n in range(0, len(digit)):
        sum += digit[lent - n] * point
        point *= 10
    return sum
# print(to_number([1, 2, 3, 4]))


def factsimp(num):
    l = 1
    for m in range(1, num + 1):
        l *= m
    return l


def fact_digits(number):
    arr = []
    arr = to_digits(number)
    j = 0
    sum1 = 0
    for j in range(0, len(arr)):

        sum1 = sum1 + factsimp(arr[j])
    return sum1
print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))


def fibonachi(n):
    result = []
    a, b = 1, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result
print(fibonachi(10))


def fib_number(n):
    strn = ""
    for num in fibonachi(n):
        strn += str(num)
    return strn
print(fib_number(10))


def palindrome(n):
    string = str(n)
    for i in range(0, len(string)):
        if(string[i] == string[len(string) - 1 - i]):
            return True
        else:
            return False
print(palindrome("kapak"))


def count_vowels(string):
    count = 0
    lower_string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for ch in lower_string:
        for i in range(0, len(vowels)):
            if (ch == vowels[i]):
                count += 1
                continue
    return count
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


def check_consonats(string):
    count = 0
    lower_string = string.lower()

    Cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    for ch in lower_string:
        for i in range(0, len(Cons)):
            if (ch == Cons[i]):
                count += 1
                continue

    return count

print(check_consonats("Github is the second best thing that happend to programmers, after the keyboard!"))


def char_histogram(sequence):
    histogram = {}
    for element in sequence:
        if (not histogram.has_key(element)):
            histogram[element] = 1
        else:
            histogram[element] += 1

    for i in histogram:
        print (str(i) + ": " + str(histogram[i]))

char_histogram("AAAAaaa!!!")
