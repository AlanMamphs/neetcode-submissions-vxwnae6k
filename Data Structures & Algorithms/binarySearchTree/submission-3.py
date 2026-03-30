class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertBST(self.root, key, val)
        # self.getInorderKeys()

    def insertBST(self, curr, key, val):
        if not curr:
            return TreeNode(key, val)
        
        if key < curr.key:
            curr.left = self.insertBST(curr.left, key, val)
        elif key > curr.key:
            curr.right = self.insertBST(curr.right, key, val)
        else:
            curr.val = val
        
        return curr

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.findMin(self.root)
        return curr and curr.val

    def findMin(self, curr):
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr and curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeBST(self.root, key)
    
    def removeBST(self, curr, key) -> None:
        if not curr:
            return
        
        if key < curr.key:
            curr.left = self.removeBST(curr.left, key)
        elif key > curr.key:
            curr.right = self.removeBST(curr.right, key)
        else:
            if not curr.right and not curr.left:
                return
            if not curr.right:
                return curr.left
            if not curr.left:
                return curr.right
            
            minNode = self.findMin(curr.right)
            curr.key = minNode.key
            curr.val = minNode.val
            curr.right = self.removeBST(curr.right, minNode.key)
        
        return curr

    def getInorderKeys(self) -> List[int]:
        vals = []
        self.inorderBST(self.root, vals)
        print(vals)
        return vals
    
    def inorderBST(self, curr, vals):
        if not curr:
            return
        self.inorderBST(curr.left, vals)
        vals.append(curr.key)
        self.inorderBST(curr.right, vals)


    

