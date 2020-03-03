# node class
class StringRegisterNode :

    def __init__(self , length) :
        # initialize children of length of the alphabet for each node
        self.children = [ None ] * length

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


# Register data structure class

class StringRegister :

    def __init__(self , A) :

        # sorts the alphabets

        A.sort ( )

        # set the alphabet attribute to the alphabets

        self.alphabet = A

        self.root = self.getNode ( )

    def getNode(self) :

        # returns new node initialized to null

        return StringRegisterNode ( len ( self.alphabet ) )

    # converts the current key character to into index using the sorted alphabet list
    def charToIndex(self , ch) :

        start = 0
        end = len ( self.alphabet ) - 1

        # binary search to search for the character and its index in the given alphabets
        while start <= end :  # logc

            mid = start + (end - start) // 2;
            if self.alphabet [ mid ] == ch :
                return mid
            elif ch > self.alphabet [ mid ] :
                start = mid + 1
            else :
                end = mid - 1

        return -1

    # inserting a string in the register
    def insert(self , key) :

        rootnode = self.root

        # visits each character of the string #O(k)
        for charIndex in range ( len ( key ) ) :
            index = self.charToIndex ( key [ charIndex ] )  # logc , defined above

            # if the character exists in the alphabet
            if index != -1 :

                # if current character is not present in the tree
                if rootnode.children [ index ] == None :
                    rootnode.children [ index ] = self.getNode ( )

                rootnode = rootnode.children [ index ]  # O(1)

            else :
                return "Character not present in the alphabet"

        # last node is marked as end of word
        rootnode.isEndOfWord = True

    # searching a string in the register
    def search(self , key) :

        rootnode = self.root
        length = len ( key )
        # visits each character of the string #O(k)
        for charIndex in range ( length ) :
            index = self.charToIndex ( key [ charIndex ] )  # logc , defined above

            # searches for the character in the node
            if rootnode.children [ index ] == None :
                return False
            rootnode = rootnode.children [ index ]  # O(1)

        return rootnode != None and rootnode.isEndOfWord

    # deleting a string from the register
    def delete(self , key) :

        rootnode = self.root
        length = len ( key )
        # visits each character of the string #O(k)
        for charIndex in range ( length ) :
            index = self.charToIndex ( key [ charIndex ] )  # logc , defined above

            # if the character of the string to delete doesn't exist in the node
            if rootnode.children [ index ] == None :
                return False
            rootnode = rootnode.children [ index ]  # O(1)

        # end of word is removed from the last character as it is being deleted
        rootnode.isEndOfWord = False



