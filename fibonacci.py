#!/usr/bin/env python3

"""
Writes given list to a file with the items separated by ','
"""
def writeFibonacciFile(series):
    fileName = "fibonacciSeries.txt"
    file = open(fileName, 'w')
    file.write(', '.join(str(i) for i in series))
    file.close()
    print("Fibonacci series written to ", fileName)

"""
Calculates a Fibonacci series, returns it as a list.
arg1: starting number for the series, the series will start from the first number bigger than the given starting number
arg2: length of the series
"""
def getFibonacciSeries(startingNumber, seriesLength):
    a, b = 0, 1
    series = []

    while len(series) < seriesLength:
        if a > startingNumber:
            series.append(a)
        a, b = b, a+b

    return series

"""
Handles user prompts, returns given integer or 10 if defaultLengthAllowed is true
and the user input was empty/whitespace. Raises ValueError if input is invalid.
"""
def handleMenuInput(prompt, defaultLengthAllowed):
    try:
        val = input(prompt)
        if str(val).isspace() or len(str(val)) == 0 and defaultLengthAllowed:
            return 10

        return int(val)
    except:
        raise ValueError("Unexpected input.")

def main():
    #Ask for user input
    while True:
        try:
            startingNumber = handleMenuInput("Starting number for the Fibonacci series? : ", False)
            seriesLength = handleMenuInput("How many terms should be calculated? (leave empty for 10) : ", True)
            if seriesLength < 1:
                raise ValueError("Series length should be more than 0.")
            break
        except Exception as e:
            print(str(e))

    series = getFibonacciSeries(startingNumber, seriesLength)
    writeFibonacciFile(series)

if __name__ == "__main__":
    main()
