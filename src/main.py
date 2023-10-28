from node.node import *

def main():
    # testInit()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    review()

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