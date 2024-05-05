# 4256번: 트리
T = int(input())

def postorder(preorder, inorder):

    if not preorder:
        return []

    root = preorder[0]
    root_index = inorder.index(root)

    left_subtree_postorder = postorder(preorder[1:1+root_index], inorder[:root_index])
    right_subtree_postorder = postorder(preorder[1+root_index:], inorder[root_index+1:])

    return left_subtree_postorder + right_subtree_postorder + [root]


for i in range(T):
    n = int(input())
    preorder_list = list(map(int, input().split()))
    inorder_list = list(map(int, input().split()))

    result = postorder(preorder_list, inorder_list)

    print(' '.join(map(str, result)))
