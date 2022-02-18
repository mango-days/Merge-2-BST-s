# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) :
        self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        parent = self.root
        temp = self.root
        
        while temp :
            parent = temp
            
            if temp == None : 
                temp = Node ( data )
                return
            
            if temp.data < data : 
                temp = temp.right
                if temp == None : 
                    parent.right = Node ( data )

            elif temp.data == data : 
                temp = temp.right
                if temp == None : 
                    parent.right = Node ( data )

            elif temp.data > data : 
                temp = temp.left
                if temp == None :
                    parent.left = Node ( data )

            else : print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.left : self.printList ( node.left )
        if node.data : print ( node.data ) #data exists
        if node.right : self.printList ( node.right )
        return
    
    def merge ( self , Tree2_node ) :
        if Tree2_node == None : return
        if Tree2_node.left : self.merge ( Tree2_node.left )
        if Tree2_node.data : self.insert ( Tree2_node.data )
        if Tree2_node.right : self.merge ( Tree2_node.right )
        return
    
        

Tree1 = BinaryTree ()
Tree2 = BinaryTree ()

arr1 = [ 5 , 3 , 6 , 2 , 4 ]
arr2 = [ 2 , 1 , 3 , 7 , 6 ]

for index , value in enumerate ( arr1 ) : Tree1.insert ( value )
for index , value in enumerate ( arr2 ) : Tree2.insert ( value )


#Tree1.printList ( Tree1.root )
#Tree2.printList ( Tree2.root )

Tree1.merge ( Tree2.root )
Tree1.printList ( Tree1.root )
