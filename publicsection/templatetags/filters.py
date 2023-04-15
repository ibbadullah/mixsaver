from django import template
import time
register = template.Library()


@register.filter(name='discount')
def discountFormula(price1,price2):
    discount = price2 - price1
    formula = discount/price2 * 100
    return round(formula)


@register.filter(name="CurrentMonthYear")
def currentMonthYear(request):
    month = time.strftime("%B")
    year = time.strftime("%Y")
    date = month+" "+year
    return date

@register.filter(name='minus1')
def minus(request,num):
    return num-1


@register.filter(name='decrypt')
def changed(request,z1):
    m1 = {
        "X": "q", "w": "Q",
        "W": "r", "v": "R",
        "V": "s", "u": "S",
        "U": "t", "t": "T",
        "T": "u", "s": "U",
        "S": "v", "r": "V",
        "R": "w", "q": "W",
        "Q": "x", "p": "X",
        "P": "y", "o": "Y",
        "O": "z", "n": "Z",
        "~": " ",
        "N": "a", "5": "0", "m": "A",
        "M": "b", "4": "1", "l": "B",
        "L": "c", "3": "2", "k": "C",
        "K": "d", "2": "3", "j": "D",
        "J": "e", "1": "4", "i": "E",
        "I": "f", "0": "5", "h": "F",
        "H": "g", "9": "6", "g": "G",
        "G": "h", "8": "7", "f": "H",
        "F": "i", "7": "8", "e": "I",
        "E": "j", "6": "9", "d": "J",
        "D": "k", "-": "!", "c": "K",
        "C": "l", "?": "@", "b": "L",
        "B": "m", "=": "#", "a": "M",
        "A": "n", ")": "^", "z": "N",
        "Z": "o", "[": ".", "y": "O",
        "Y": "p", "}": ":", "x": "P",
        "!": "-","@": "?", "#": "=",
        "^": ")",".": "[",":": "}",

    }

    m2 = ""
    for ch in z1:
        m2 += m1.get(ch,ch)
    return m2


