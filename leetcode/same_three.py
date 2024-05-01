# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        # return bool(all(
        #     [
        #         p.val == q.val,
        #         self._valid_tree_node_values(p.left, q.left),
        #         self._valid_tree_node_values(p.right, q.right),
        #     ]
        # ))
        # Utilizando da recursão do python, chamando a mesma função chamada é possivel validar todos os valores.
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Outra forma /\/\/\/\/\/\/\/\

    # def _valid_tree_node_values(self, p, q):
    #     if not p and not q:
    #         return True
    #     if not p or not q:
    #         return False
    #     return bool(p.val == q.val)
