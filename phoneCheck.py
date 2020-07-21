import re


"""Checks to make sure the number is valid"""
def checkNumber(number: str) -> bool:
    phone = re.compile("^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$")
    if phone.match(number):
        return True
    return False


"""Makes all the inputted numbers uniform"""
def formatNumber(number: str) -> str:
    #pattis taught me well
    return "".join([i for i in number if i in [str(i) for i in range(10)]])

    """
    final = ""
    for i in number:
        if i in [str(i) for i in range(10)]:
            final += i
    return final
    """



if __name__ == "__main__":
    phoneNum = input("Input a phone number ")

    print(checkNumber(phoneNum))

