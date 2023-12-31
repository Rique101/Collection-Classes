from stack.stack import *

class balancedparens:
    @staticmethod
    def isBalanced(expression: str):
        """Checks a specified mathematical expression to see when the
        parenthesis are balanced.

        Args:
            expression (str): specified mathematical expression
        
        Returns:
            Boolean: True if the parenthesis is in the expression are balanced,
            else False
        """        

        #Variables for parenthesis
        LEFT_NORMAL = "("
        RIGHT_NORMAL = ")"
        LEFT_CURLY = "{"
        RIGHT_CURLY = "}"
        LEFT_SQUARE = "["
        RIGHT_SQUARE = "]"

        #Stack used to store parenthesis
        store = stack()

        #Variable used to indicate imbalance
        imbalance = False

        #Loop through expression a character at a time
        #as long as there isn't an imbalance
        for s in expression:
            if (not imbalance):
                if (s == LEFT_CURLY or s == LEFT_NORMAL or s == LEFT_SQUARE):
                    #if the current character is a {, (, [
                    #push it onto the stack
                    store.push(s)
                elif (s == RIGHT_NORMAL):
                    #if the current character is a ), check if stack is empty
                    #or if top node doesn't contain a (
                    if (store.isEmpty() or store.pop() != LEFT_NORMAL):
                        #set imbalance to true
                        imbalance = True
                
                elif (s == RIGHT_SQUARE):
                    #if the current character is a ), check if stack is empty
                    #or if top node doesn't contain a (
                    if (store.isEmpty() or store.pop() != LEFT_SQUARE):
                        #set imbalance to true
                        imbalance = True
                
                elif (s == RIGHT_CURLY):
                    #if the current character is a ), check if stack is empty
                    #or if top node doesn't contain a (
                    if (store.isEmpty() or store.pop() != LEFT_CURLY):
                        #set imbalance to true
                        imbalance = True

        #Return true if there are no parenthesis on the stack and
        #an imabalance hasn't been found
        return (store.isEmpty() and not imbalance)
