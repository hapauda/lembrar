from typing import Optional

class TreeNode:
    def __init__(self, valor=0, left=None, rigth=None):
        self.valor = valor
        self.left = left
        self.rigth = rigth

class solução:
    def inverterTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.rigth = root.rigth, root.left
            self.inverterTree(root.left)
            self.inverterTree(root.rigth)
        return root
    def insert(self, root: Optional[TreeNode], valor:int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(valor)
        if valor < root.valor:
            root.left = self.insert(root.left,valor)