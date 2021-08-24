# Lychrel Numbers
# Made by: Zuhair H. Khan
# Date: 2021-03-03
# Purpose: To meet all 4 requirements in rubric... :)

def palindrome(num):
    '''palindrome() returns true if the word is a palindrome
    arg:
    -- num : int
    return:
    -- Boolean
    '''

    num1 = str(num)

    revNum = list(reversed(num1))

    # checks for palindrome
    for i in range(0, len(num1)):
        if num1[i] != revNum[i]:
            # not a palindrome
            return False
        # end of if
    # end of for
    return True


# end of palindrome()


def lychrel(num):
    '''lychrel() returns the value for the sum of the number and the number reveresed
    arg:
    -- num : string
    return:
    -- palNum : int
    '''

    num1 = num[::-1]

    num2 = int(num)
    revNum = int(num1)

    # print(num1, num2, revNum)

    palNum = num2 + revNum

    return palNum


# end of lychrel


def maxCheck(num):
    '''maxCheck() returns the value for the sum of the number and the number reveresed
    arg:
    -- num : int
    return:
    -- maxNum : int
    '''
    maxNum = 0
    if num > maxNum:
        maxNum = num

    return maxNum


# variable declaration
currentChain = [0] * 195
mChain = 0
lChain = []
maxNum = [0] * 195
maximum = 0

# loop repeats for numbers --> [1,195]
for i in range(1, 196):
    num = str(i)

    count = 1

    boolNum = palindrome(lychrel(num))

    while boolNum == False:
        num = str(lychrel(num))

        boolNum = palindrome(lychrel(num))

        count += 1
    # end of while

    '''
    USED TO TEST HOW MANY ITERATIONS EACH NUMBER GOES THROUGH TO REACH A PALINDROMIC NUMBER
    print('Repeated', count, 'times', 'for', i)
    '''
    currentChain[i - 1] = count

    maxNum[i - 1] = maxCheck(lychrel(num))

    if mChain <= currentChain[i - 1]:
        mChain = currentChain[i - 1]
    # end of if
# end of for


j = 1
c = 0
while j <= 195:
    # Finds number(s) with the longest chain
    if mChain == currentChain[j - 1]:
        lChain.append(str(j))
    # end of if

    # Finds largest possible number generated in this program
    if maximum < maxNum[j - 1]:
        maximum = maxNum[j - 1]
    # end of if

    # Finds number of sequences that are larger than 2
    if currentChain[j - 1] > 2:
        c += 1
    # end of if

    j += 1
# end of while


print('1) Number(s) that generate the longest chain:', lChain)
print('2) Length of the longest list/sequence is:', mChain + 1)
print('3) The largest possible number generated from this program is:', maximum)
print('4) There are', c, 'sequences that are longer than 2')
