# Pablo Hurtado Curbelo
import socket


class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        print("Your age is", currentYear - self.year)

    def listAnniversaries(self):
        anniversaries = []

        tenYearAnniversariesCount = (2022 - self.year)//10

        for n in range(tenYearAnniversariesCount):
            anniversaries.append((n+1) * 10)

        return anniversaries

    def modifyYear(self, n):
        result = []

        self.repeatFirstTwoDigits(n, result)
        self.oddCharsOfMultiplication(n, result)

        return "".join(result)

    def repeatFirstTwoDigits(self, n, result):
        """
        Repeats the first two digits of the year n times and appends to result.
        Example:
            - n=3, self.year=1980 -> 191919
        """
        yearFirstTwoDigits = str(self.year)[:2]
        for _ in range(n):
            result.append(yearFirstTwoDigits)

    def oddCharsOfMultiplication(self, n, result):
        """
        Multiplies the year by n and appends the odd positioned digits to result.
        Example: 
            - n=2, self.year=1980 -> 36
        """
        multipliedYear = str(self.year*n)

        odd = True
        for char in multipliedYear:

            # Append odd positioned digits to result
            # Example: multipliedYear=2134, append(2) & append(3)
            if odd:
                result.append(char)

            # Flip flag
            odd = not odd

    @staticmethod
    def checkGoodString(string):

        if len(string) < 9:
            return False

        if not string[0].islower():
            return False

        # Count all numbers in the string
        numberCount = 0
        for char in string:
            if char.isdigit():
                numberCount += 1

        if numberCount != 1:
            return False

        return True

    @staticmethod
    def connectTcp(host, port):
        try:
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.connect((host, port))
            tcpSocket.close()

        except Exception as e:
            # For debuging
            # print(e)
            return False

        return True
