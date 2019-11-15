class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

class BST:
    def __init__(self, num_list):
        self.root = None
        for num in num_list:
            self.insert(num)

    def insert(self, num):
        if self.root is None:
            # root = Node(num)
            self.root = Node(num)
            return

        root = self.root
        while True:
            if num < root.num:
                if root.left is None:
                    root.left = Node(num)
                    break
                else:
                    root = root.left

            elif num > root.num:
                if root.right is None:
                    root.right = Node(num)
                    break
                else:
                    root = root.right

            # 同じ数値が既に入っているので何もせず終了
            else:
                break

    def serarch(self, num):
        result = self.is_exist(num)
        if result is None:
            print("Search target is not found.")
        elif result:
            print(str(num) + " is found!")
        elif not result:
            print(str(num) + " is not found.")

    def is_exist(self, num):
        root = self.root
        if root is None:
            return None
        
        else:
            stack = []
            stack.append(root)
            while len(stack) > 0:
                node = stack.pop()
                if num == node.num:
                    return True
                
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                    
            return False

    def sort(self, node):
        if node is not None:
            self.sort(node.left)
            print(node.num)
            self.sort(node.right)


if __name__ == "__main__":
    import random
    random_list = list(range(50))
    random.shuffle(random_list)
    print(random_list)

    tree = BST(random_list)
    tree.serarch(10)
    tree.sort(tree.root)