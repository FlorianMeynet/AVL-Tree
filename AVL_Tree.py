# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:44:13 2020

@author: fm195666
"""

class Node(object): 
	def __init__(self, val): 
		self.value = val 
		self.left = None
		self.right = None
		self.height = 1
        
class AVL_Tree(object):
    
    def __init__(self,root=None):
        self.root = root
        
    def getHeight(self, node): 
        if not node: 
            return 0

        return node.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 
    
    
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        
        
        y.right=z     
        z.left=T3
        
        y.height=1+max(self.getHeight(y.left),self.getBalance(y.right))
        z.height=1+max(self.getHeight(z.left),self.getBalance(z.right))
        
        return(y)
    
    def leftRotate(self,z):
        y=z.right
        T3=y.left
        
        y.left=z
        z.right=T3
        
        y.height=1+max(self.getHeight(y.left),self.getBalance(y.right))
        z.height=1+max(self.getHeight(z.left),self.getBalance(z.right))
        
        return (y)
    
    def insertAVL(self,root,key):
        if not root: 
            return(Node(key))
        if(key<root.value):
            root.left=self.insertAVL(root.left,key)
        else:
            root.right=self.insertAVL(root.right,key)
            
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))    
        
        balance=self.getBalance(root)
        
        if balance >1 and key<root.left.value:
            #c'est plus lourd a gauche et on a inserer a gauche
            return self.rightRotate(root)
        if balance >1 and key>=root.left.value:
            #c'est plus lourd a gauche et on a inserer a droite
            root.left=self.leftRotate(root)
            
            return self.rightRotate(root)
        
        if balance <-1 and key>=root.right.value :
            #c'est plus lourd a droite et on a inseré a droite
            return self.leftRotate(root)
            
            
        if balance <-1 and key<root.right.value : 
            #c'est plus lourd a droite et on a inseré a gauche
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return(root)  #Si on est pas dans tous les cas
    
    def preorder_print(self,start):
            if start:
                print(start,end=' ')
                self.preorder_print(start.left)
                self.preorder_print(start.right)
                
    def postorder_print(self,start):
        if start:            
            self.postorder_print(start.left)
            print(start,end=' ')
            self.postorder_print(start.right)

    def inorder_printDescending(self,start):
        if start:            
            
            self.inorder_printDescending(start.right)
            print(start,end=' ')
            self.inorder_printDescending(start.left)
            
            
    def inorder_print(self,start):
        if start:            
            self.inorder_print(start.left)
            self.inorder_print(start.right)
            print(start,end=' ')
            
        
    def preOrder(self, root): 
    
        if not root: 
            return
  
        print("{0} ".format(root.value), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right)

        
#Ex6   
    def delete(self,root,key): #Pour le delete on enleve le node et apres on refait comme le insert pour remettre l'arbre equilibré
        if not root:
            return(root)
        #Metode delete clasic pour n'importe quel arbre
        if key < root.val: 
            root.left = self.delete(root.left, key)   #On est dans le coté gauche de l'arbre
  
        if key > root.val:   
            root.right = self.delete(root.right, key) #On est dans le coté droit de l'arbre
        
         else: #On a trouvé l'endroit de la node dans l'arbre
            
            if(root.left is None && root.right is None) #S'il n'y a pas de child
                root=None
                return None
            
            elif root.left is None:   #S'il n'y a pas de left child
                new = root.right #On remplace 
                root = None
                return new 
  
            elif root.right is None: #S'il n'y a pas de right child
                new = root.left 
                root = None
                return new 
                
            else : #Il y a 2 child
                new = self.getMinValueNode(root.right) #On cherche le min des 2 child
                root.val = new.val 
                root.right = self.delete(root.right,new.val) #on enleve le min puisque qu'on la mis a la place de la node a supprimé
    
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))    
        
        balance=self.getBalance(root)
        
        if balance >1 and key<root.left.value:
            #c'est plus lourd a gauche et on a inserer a gauche
            return self.rightRotate(root)
        if balance >1 and key>=root.left.value:
            #c'est plus lourd a gauche et on a inserer a droite
            root.left=self.leftRotate(root)
            
            return self.rightRotate(root)
        
        if balance <-1 and key>=root.right.value :
            #c'est plus lourd a droite et on a inseré a droite
            return self.leftRotate(root)
            
            
        if balance <-1 and key<root.right.value : 
            #c'est plus lourd a droite et on a inseré a gauche
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return(root)  #Si on est pas dans tous les cas
        
        
#Ex7    
    def Sorted_list(self,root):
        L=[]
        if root:            
            self.Sorted_list(root.right)  #On prend d'abord a droite car les plus grand chiffres sont a droite
            L.append(root.key)
            self.Sorted_list(root.left)  #Une fois qu'on a pris tous az droite on vient a gauche
        return L
        
        
        
#Ex8    
    def create_Tree(self,L):
        tree = AVL_Tree() #On defenie un Tree vide
        for c in L:
            c.insertAVL(tree.root,c) #On insert chaque valeur dans le tree
        return tree
    
    
#Ex9    
    def Compare_2AVL(self,root_1,root_2):
        while(root_2!=None):
            root_1.insertAVL(root_1,root_2.key)
            root_2.delete(root2,root_2.key)
        return root_1
 
            
myTree=AVL_Tree()
root=None
nums=[9,5,10,0,6,11,-1,1,2]

for num in nums:
    root=myTree.insertAVL(root, num)            
            
myTree.preOrder(root)           