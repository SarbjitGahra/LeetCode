#binary tree
class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent=None


    def insert(self, val):
        temp = node(val)
        if self.val == val :
            return False
        if self.val > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = temp
                return True
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = temp
                return True
    def find(self, val):
        max = self.max()
        min = self.min()
        if val > max or val < min:
            return False
        if self.val==val:
            return True
        elif self.val < val:
            return  self.right.find(val)
        elif self.val > val:
            return self.left.find(val)


    def min(self):
        if self.left == None:
            return self.val
        elif self.left:
            return self.left.min()

    def max(self):
        if self.right == None:
            return self.val
        elif self.right:
            return self.right.max()

    def preorder(self):
        if self:
            print (str(self.val))
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print (str(self.val))
    def inorder(self):
        if self:
            if self.left:
                self.left.preorder()
            print (str(self.val))
            if self.right:
                self.right.preorder()



class binarytree(node):

    def __init__(self):
        self.root = None

    def insert(self, val):
        temp = node(val)
        if self.root:
            return self.root.insert(val)
        else:
            self.root = node(val)
            return True
    def find(self, val):
        return self.root.find(val)

    def pre_order(self):
        self.root.preorder()
    def post_order(self):
        self.root.postorder()
    def in_order(self):
        self.root.inorder()

    def min(self):
        return self.root.min()


bi = binarytree()
for i in range (5):
    bi.insert(i)

print (bi.find(9))


#bi.pre_order()
#bi.post_order()
#bi.in_order()
