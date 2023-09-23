from Lab4 import Deque

def wordToDeque(input):
    deque = Deque()
    for char in input:
        deque.push(char)
    return deque

def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front == None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True
test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque)) # Should return True

def OffByOne(char1, char2):
    return abs(ord(char1)- ord(char2)) == 1

char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2)) #print True


def OffByN(char1, char2, N):
    return abs(ord(char1) - ord(char2)) == N

char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N)) #Prints True
