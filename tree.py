#定义数据结构的类，树的三个私有属性，左子树，右子树，根节点
class Node():

     def __init__(self,data = None,left = None, right = None):
          self.data = data
          self.left = left
          self.right = right
    

## 前序遍历
def orderTraversal(tree):
    if tree == None:
        return False
    print(tree.data)
    orderTraversal(tree.left)
    orderTraversal(tree.right)



## 中序遍历
def inoderTraversal(tree):
    if tree == None:
        return False
    inoderTraversal(tree.left)
    print(tree.data)
    inoderTraversal(tree.right)

## 后续遍历

def postoderTraversal(tree):
    if tree == None:
        return False
    postoderTraversal(tree.left)
    postoderTraversal(tree.right)
    print(tree.data)

## 层次遍历

def roworderTraversal(tree):
    queue = []
    queue.append(tree)
    while True:
        if queue == []:
            break
        print(queue[0].data)
        first_tree = queue[0]
        if first_tree.left != None:
            queue.append(first_tree.left)
        if first_tree.right != None:
            queue.append(first_tree.right)
        queue.remove(first_tree)


if __name__ == "__main__":

    tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
    roworderTraversal(tree)