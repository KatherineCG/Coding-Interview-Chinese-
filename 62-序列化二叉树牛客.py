class Solution:
    def Serialize(self, root):
        if root is not None:
            return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)
        else: return ['#']
    def Deserialize(self, s):
        self.s = s
        return self.rDLF()
    def rDLF(self):
        temp = self.s.pop(0)
        if temp != '#':
            root = TreeNode(temp)
            root.left = self.rDLF()
            root.right = self.rDLF()
        else: root =None
        return root