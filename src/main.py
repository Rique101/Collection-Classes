from node.node import *
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from stack.serialsearch import *
from stack.selectionsort import *
from queues.queue import *
from queues.palindrome import *
from queues.palindrome2 import *
from queues.palindrome3 import *
from loops import *
def main():
    # testInit()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    # review()
    #testListLength()
    #testListSearch()
    #testListPosition()
    #testListCopy()
    #testListCopyWithTail()
    #testPush()
    #testPop()
    #testIsEmpty()
    #testPeek()
    #print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y")) # False
    #print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y)")) # False
    #print("Parenthesis are balanced?", balancedparens.isBalanced("({X+Y}*Z)")) # True
    #print("Parenthesis are balanced?", balancedparens.isBalanced("[A+B]*({X+Y}*Z)")) # True
    #print("(((6+9)/3)*(6-4)) = ", calculator.evaluate("(((6+9)/3)*(6-4))"))
    #print("(6+(3*(6-4))) = ", calculator.evaluate("(6+(3*(6-4)))"))
    #print("((5+2)-(3*(6/9))) = ", calculator.evaluate("((5+2)-(3*(6/9)))"))
    #print("((5*2)-(3*(6/2))) = ", calculator.evaluate("((5*2)-(3*(6/2)))"))
    #testSerialSearch()
    #testSelectionSort()
    #testEnqueue()
    #testQueueIsEmpty()
    #testDequeue()
    #testQueuePeek()
    #testIsPalindrome()
    #testIsPalindrome2()
    #testIsPalindrome3()
    #SantaClaus()
    #getPalindromes()
    testRecursion()
#Question 1
def SantaClaus():
    s = node("A",None)
    s = node("T", s)
    s = node("N", s)
    s = node("A", s)
    s = node("S", s)
    
    #Question 2
    c = node("S", None)
    c = node("U", c)
    c = node("A", c)
    c = node("L", c)
    c = node("C", c)

    #Question 3
    selection = s

    #Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    #Question 5
    selection.setLink(c)

#Question 6
def getPalindromes():
    s1 = stack()
    s2 = stack()

    Words = input("Enter ten words separated by a space: ").split()
    if (palindrome.isPalindrome(Words)):
        s1.push(Words)
    else:
        s2.push(Words)

    print('These words are Palindromes', end=" ")
    while (not s1.isEmpty()):
        print(s1.pop(), end=" ")
    print()

    print('These words are not Palindromes', end=" ")
    while (not s2.isEmpty()):
        print(s2.pop(), end=" ")
    print()

#Question 7
def testRecursion():
    evens_recursive(-10,10)


def testIsPalindrome3():
    while True:
        exp = input("Please enter an expression: ")
        
        if exp == "":
            print("Good Bye!")
            break
        
        result = palindrome3.isPalindrome(exp)

        if result is True:
            print("Your expression is a Palindrome")
        else:
            # Print the characters where mismatches occurred
            print(f"This is not a palindrome\nMismatched characters: {result}")

def testIsPalindrome2():
        while True:
            exp = input("Please enter an expression: ")
            if palindrome2.isPalindrome(exp):
                print("Your expression is a Palindrome")
            else:
                print("Your expression is not a Palindrome")
            if(exp == ""):
                print("Good Bye!")
                break
        

def testIsPalindrome():
    exp = input("Please enter an expression.")

    if (palindrome.isPalindrome(exp)):
        print("Your expression is a Palindrome")
    else:
        print("Your expression is not a Palindrome")
        
def testEnqueue():
    print("Testing Enqueue Method")
    b = queue()

    b.enqueue('A')
    b.enqueue('B')
    b.enqueue('C')
    b.enqueue('D')
    b.enqueue(1)
    b.enqueue(2)
    b.enqueue(3)
    print(b)

def testQueueIsEmpty():
    print("Testing is QueueIsEmpty Method")
    
    b = queue()
    b.enqueue('J')
    b.enqueue('O')
    b.enqueue('B')
    b.enqueue('S')

    print("Queue size is:", b.size()) #4
    print('Queue contains:', b) # [J O B S]

    while(not b.isEmpty()):
        print("Just dequeued:", b.dequeue())
    
    print("Queue size is:", b.size()) # 0
    print("Queue contains:", b) # []

def testDequeue():
    print("Testing Dequeue Method")
    b = queue()
    b.enqueue('J')
    b.enqueue('O')
    b.enqueue('B')
    b.enqueue('S')

    print(b) #[J O B S]

    b.dequeue() #Removes J
    b.dequeue() #Removes O
    b.dequeue() #Removes B
    print(b) #[S]

def testQueuePeek():
    print("Testing QueuePeek Method")
    b = queue()
    b.enqueue('J')
    b.enqueue('O')
    b.enqueue('B')
    b.enqueue('S')
    print("Element in front of Queue", b.peek()) #J

    b.dequeue()
    print("Element in front of Queue", b.peek()) #O

def testSelectionSort():

    # create an empty stack
    data = stack()
    
    # initialize first
    first = 1
    #first = 4
    #first = 6
    
    # push -7 onto the top of the stack
    data.push(-7)
    
    # push 42 onto the top of the stack
    data.push(42)
    
    # push 70 onto the top of the stack
    data.push(70)
    
    # push 39 onto the top of the stack
    data.push(39)
    
    # push 3 onto the top of the stack
    data.push(3)
    
    # push 63 onto the top of the stack
    data.push(63)
    
    # push 8 onto the top of the stack
    data.push(8)
    
    # print unsorted stack
    print("Unsorted Stack: ",data)
    
    # call selection sort method
    #print sorted stack
    print("Sorted Stack: ", selectionsort(data, first))


def testSerialSearch():
    # create an empty stack
    a = stack()
    
    # initialize first
    # initialize size
    # initialize target
    first = 1
    size = 7
    target = 70
    
    # push -7 onto the top of the stack
    a.push(-7)
    
    # push 42 onto the top of the stack
    a.push(42)
    
    # push 70 onto the top of the stack
    a.push(70)
    
    # push 39 onto the top of the stack
    a.push(39)
    
    # push 3 onto the top of the stack
    a.push(3)
    
    # push 63 onto the top of the stack
    a.push(63)
    
    # push 8 onto the top of the stack
    a.push(8)
    
    # print the stack
    print(a)
    
    # call serial search method and display its return.
    print(target, 'found at node position', serialsearch(a, first, size, target))


def testPeek():
    print("Testing Peek Method in Stack Class")

    s = stack()
    print("Stack size is:", s.size()) # 0
    print('Stack contains:', s) # []
    s.push("S") 
    print("Stack size is:", s.size()) # 1
    print('Stack contains:', s) #[S]
    print("Top element in stack is:", s.peek()) # returns S
    s.push("B")
    print("Stack size is:", s.size()) # 2
    print('Stack contains:', s) # [B S]
    print("Top element in stack is:", s.peek()) # Returns B
    s.push("O")
    print("Stack size is:", s.size()) # 3
    print('Stack contains:', s) # [O B S]
    print("Top element in stack is:", s.peek()) # Returns O
    s.push("J")
    print("Stack size is:", s.size()) # 4
    print('Stack contains:', s) # [J O B S]
    print("Top element in stack is:", s.peek()) # Returns J
def testIsEmpty():
    print("Testing is Empty Method in Stack Class")
    
    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) #4
    print('Stack contains:', s) # [J O B S]

    while(not s.isEmpty()):
        print("Just popped:", s.pop())
    
    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s) # []

def testPop():
    print("Testing Pop Method in Stack Class")
    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) #4
    print('Stack contains:', s) # [J O B S]
    print("Just popped:", s.pop()) # removes J

    print("Stack size is:", s.size()) #3
    print('Stack contains:', s) # [O B S]
    print("Just popped:", s.pop()) # removes O

    print("Stack size is:", s.size()) #2
    print('Stack contains:', s) # [B S]
    print("Just popped:", s.pop()) # removes B

    print("Stack size is:", s.size()) #1
    print('Stack contains:', s) # [S]
    print("Just popped:", s.pop()) # removes S

    print("Just popped:", s.pop()) # will print "Stack is empty"

def testPush():
    print("testing Push Method in Stack Class")

    s = stack()
    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s)       # []

    s.push('S')
    print("Stack size is:", s.size())  # 1
    print("Stack contains", s)       # [S]

    #s.push('B')
    s.push(1)
    print("Stack size is:", s.size())  # 2
    print("Stack contains", s)       # [B S]

    #s.push('O')
    s.push((1,2))
    print("Stack size is:", s.size())  # 3
    print("Stack contains", s)       # [O B S]

    #s.push('J')
    s.push([1,2,3])
    print("Stack size is:", s.size())  # 4
    print("Stack contains", s)       # [J O B S]

def testListCopyWithTail():
    print("Testing List Copy With Tail")

    #Construct a node with data equal to S and link equal to None
    #and assign its reference to source
    source = node("S", None) # S

    #Construct a node with data equal to B and link equal to source
    #and assign its reference to source
    source = node("B", source) # B -> S

    #Construct a node with data equal to O and link equal to source
    #and assign its reference to source
    source = node("O", source) # O -> B -> S

    #Construct a node with data equal to J and link equal to source
    #and assign its reference to source
    source = node("J", source) # J -> O -> B -> S

    copy = node.listCopyWithTail(source) 
    # [J -> O -> B -> S, S]

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(source, 2).getData(),
          node.listPosition(source, 3).getData(),
          node.listPosition(source, 4).getData())
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(),
          node.listPosition(copy[0], 2).getData(),
          node.listPosition(copy[0], 3).getData(),
          node.listPosition(copy[0], 4).getData())

    print("Copy tail contains", node.listPosition(copy[1], 1).getData())

def testListCopy():
    print("Testing List Copy")

    #Construct a node with data equal to S and link equal to None
    #and assign its reference to source
    source = node("S", None) # S

    #Construct a node with data equal to B and link equal to source
    #and assign its reference to source
    source = node("B", source) # B -> S

    #Construct a node with data equal to O and link equal to source
    #and assign its reference to source
    source = node("O", source) # O -> B -> S

    #Construct a node with data equal to J and link equal to source
    #and assign its reference to source
    source = node("J", source) # J -> O -> B -> S

    copy = node.listCopy(source) # J -> O -> B -> S, but at a different memory location

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(source, 2).getData(),
          node.listPosition(source, 3).getData(),
          node.listPosition(source, 4).getData())
    
    print("Copy contains", node.listPosition(copy, 1).getData(),
          node.listPosition(copy, 2).getData(),
          node.listPosition(copy, 3).getData(),
          node.listPosition(copy, 4).getData())

def testListPosition():
    print("Testing List Position")
    
    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("S", None) # S

    #Construct a node with data equal to B and link equal to Head
    #and assign its reference to head
    head = node("B", head) # B -> S

    #Construct a node with data equal to O and link equal to Head
    #and assign its reference to head
    head = node("O", head) # O -> B -> S

    #Construct a node with data equal to J and link equal to Head
    #and assign its reference to head
    head = node("J", head) # J -> O -> B -> S

    print('First node contains data:', node.listPosition(head, 1).getData()) # J -> O -> B -> S
    print('Second node contains data:', node.listPosition(head, 2).getData()) # O -> B -> S
    print('Third node contains data:', node.listPosition(head, 3).getData()) # B -> S
    print('Fourth node contains data:', node.listPosition(head, 4).getData()) # S

    if(node.listPosition(head, 5) != None):
        print("Fifth node contains data:", node.listPosition(head, 5).getData())
    else:
        print("There is no fifth node.")


def testListSearch():
    print("Testing List Search")
    
    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("S", None) # S

    #Construct a node with data equal to B and link equal to Head
    #and assign its reference to head
    head = node("B", head) # B -> S

    #Construct a node with data equal to O and link equal to Head
    #and assign its reference to head
    head = node("O", head) # O -> B -> S

    #Construct a node with data equal to J and link equal to Head
    #and assign its reference to head
    head = node("J", head) # J -> O -> B -> S

    print("Head contains", node.listSearch(head, "J").getData())
    print("Head contains", node.listSearch(head, "O").getData())
    print("Head contains", node.listSearch(head, "B").getData())
    print("Head contains", node.listSearch(head, "S").getData())
    
    if (node.listSearch(head, "Z") != None):
        print("Head contains", node.listSearch(head, "Z").getData())
    else:
        print("Head does not contain Z.")

def testListLength():
    print("Testing List Length")

    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("S", None) # S

    #Construct a node with data equal to B and link equal to Head
    #and assign its reference to head
    head = node("B", head) # B -> S

    #Construct a node with data equal to O and link equal to Head
    #and assign its reference to head
    head = node("O", head) # O -> B -> S

    #Construct a node with data equal to J and link equal to Head
    #and assign its reference to head
    head = node("J", head) # J -> O -> B -> S

    print("Length of head is: ", node.listlength(head))

def review():
    print("Review")

    #Question 1
    head = node("X", None)
    head = node("X", head)
    head = node("X", head)
    head = node("X", head)

    #Question 2
    selection1 = head

    #Question 3
    selection1.addNodeAfter("O")

    #Question 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 5
    selection1.addNodeAfter("O")

    #Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 7
    selection1.addNodeAfter("O")

    #Question 8
    tail = head

    #Question 9
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    #Question 10
    selection2 = head

    #Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    #Question 12
    head.setData("A")
    selection2.setData("A")
    selection1.setData("A")
    tail.setData("A")

    #Question 13
    head.removeNodeAfter()
    selection1.removeNodeAfter()
    selection2.removeNodeAfter()

def testRemoveNodeAfter():
    print("Testing Remove Node After")

    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("S", None) # S

    #Construct a node with data equal to B and link equal to Head
    #and assign its reference to head
    head = node("B", head) # B -> S

    #Construct a node with data equal to O and link equal to Head
    #and assign its reference to head
    head = node("O", head) # O -> B -> S

    #Construct a node with data equal to J and link equal to Head
    #and assign its reference to head
    head = node("J", head) # J -> O -> B -> S

    print("The head node contains data", head.getData())

    #Remove the node after the node head refers to (node that has data equal to 0)
    head.removeNodeAfter() # J -> B -> S

    head = head.getLink() # B -> S

    print("The head node contains data", head.getData())

    #Remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() # B

    print("The head node contains data", head.getData())

"""     #Remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() this line of code will generate an AttributeError """


def testAddNodeAfter():
    print("Testing Add Node After")
    
    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("J", None) # J

    print("The head node contains data:", head.getData())

    # Declare a new node named selection and make it refer 
    # to the same node as head
    selection = head 

    print("The head node contains data:", head.getData())
    print("The head node contains data:", selection.getData())

    # Add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('O') # j -> o

    # Get selection's link and assign its reference back to selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The head node contains data:", selection.getData())

    # Add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('B') # j -> B

    # Get selection's link and assign its reference back to selection
    selection = selection.getLink() # B

    print("The head node contains data:", head.getData())
    print("The head node contains data:", selection.getData())


    # Add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('S') # B -> S

    # Get selection's link and assign its reference back to selection
    selection = selection.getLink() # S

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # Declare a new node named tail and make it refer to the same 
    # node is head
    tail = head

    # Get tail's link and assign its reference to tail
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a new node with data equal to z after the node tail
    # refers to
    tail.addNodeAfter("Z")

    # Get tail's link and assign its reference to tail
    tail = tail.getLink()

    print("The head node contains data:", head.getData())
    print("The head selection contains data:", selection.getData())
    print("The tail node contains data:", tail.getData())


def testGettersAndSetters():
    print("Testing Getters and Setters")
    
    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("R", None) # R

    print("The head node contains data:", head.getData())

    head.setData("S") # S
    print("The head node contains data:", head.getData())

    head = node("B", head) # B -> S
    print("The head node contains data:", head.getData())

    head = node("O", head) # O -> B -> S
    print("The head node contains data:", head.getData())

    head = node("J", head) # J -> O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign it reference back to head
    head = head.getLink() # O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign it reference back to head
    head = head.getLink() # B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign it reference back to head
    head = head.getLink() # S
    print("The head node contains data:", head.getData())

    # get head's link and assign it reference back to head
    """ head = head.getLink() # None
    print("The head node contains data:", head.getData()) """ 

    print("The head node contains link:", head.getLink())

    # Set head's link to a new node
    head.setLink(node('O', None)) # S -> O

def testInit():
    print("Testing Node Init")

    #Construct a node with data equal to S and link equal to None
    #and assign its reference to head
    head = node("S", None) # S

    #Construct a node with data equal to B and link equal to Head
    #and assign its reference to head
    head = node("B", head) # B -> S

    #Construct a node with data equal to O and link equal to Head
    #and assign its reference to head
    head = node("O", head) # O -> B -> S

    #Construct a node with data equal to J and link equal to Head
    #and assign its reference to head
    head = node("J", head) # J -> O -> B -> S

    head = node(1, head) # 1 -> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1, 2], head) # [1, 2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node(('A', 'B'), head) # ('A', 'B') -> [1, 2] -> 1.5 -> 1 -> J -> O -> B -> S

    print()


if __name__ == "__main__":
    main()