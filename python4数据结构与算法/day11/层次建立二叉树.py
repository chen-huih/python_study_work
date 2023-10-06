class note():
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class tree():
    def __init__(self):
        self.root = None
        self.queue = []

    def insert_note(self, elem):
        new_note = note(elem)
        self.queue.append(new_note)
        if self.root is None:
            self.root = new_note
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_note
            else:
                self.queue[0].rchild = new_note
                self.queue.pop(0)

    def preorder(self, root):
        if root:
            print(root.elem, end=' ')
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def midorder(self, root):
        if root:
            self.midorder(root.lchild)
            print(root.elem, end=' ')
            self.midorder(root.rchild)

    def lastorder(self, root):
        if root:
            self.lastorder(root.lchild)
            self.lastorder(root.rchild)
            print(root.elem, end=' ')


if __name__ == '__main__':
    tree1 = tree()
    for i in range(1, 10):
        tree1.insert_note(i)

    tree1.preorder(tree1.root)
    print()
    tree1.midorder(tree1.root)
    print()
    tree1.lastorder(tree1.root)
    print()
