import random


class Node:
    def __init__(self, key):
        self.__key = key
        self.__parent_key = None
        self.__left_key = None
        self.__right_key = None

    def get_key(self):
        return self.__key

    def get_left_key(self):
        return self.__left_key

    def set_left_key(self, node_key):
        self.__left_key = node_key

    def get_right_key(self):
        return self.__right_key

    def set_right_key(self, node_key):
        self.__right_key = node_key

    def get_parent_key(self):
        return self.__parent_key

    def set_parent_key(self, node_key):
        self.__parent_key = node_key


class NodeArn:
    def __init__(self, key):
        self.__key = key
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__color = "Nero"

    def get_key(self):
        return self.__key

    def get_left(self):
        return self.__left

    def set_left(self, node):
        self.__left = node

    def get_right(self):
        return self.__right

    def set_right(self, node):
        self.__right = node

    def get_parent(self):
        return self.__parent

    def set_parent(self, node):
        self.__parent = node

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Abr:
    def __init__(self, nodes_key):
        self.__nodes = []
        self.__root = None
        if len(nodes_key) != 0:
            for i in range(0, len(nodes_key)):
                self.tree_insert(nodes_key[i])

    def get_root_key(self):
        if self.__root is not None:
            return self.__root.get_key()
        else:
            return None

    def tree_insert(self, node_key):
        node = Node(node_key)
        self.__nodes.append(node)
        actual_parent = None
        actual_node = self.__root
        while actual_node is not None:
            actual_parent = actual_node
            if node_key < actual_node.get_key():
                actual_node = self.get_node(actual_node.get_left_key())
            else:
                actual_node = self.get_node(actual_node.get_right_key())
        if actual_parent is not None:
            node.set_parent_key(actual_parent.get_key())
            if node_key < actual_parent.get_key():
                self.get_node(actual_parent.get_key()).set_left_key(node_key)
            else:
                self.get_node(actual_parent.get_key()).set_right_key(node_key)
        else:
            self.__root = node

    def tree_delete(self, node_key):
        node = self.get_node(node_key)
        if node.get_left_key() is None:
            self.transplant(node_key, node.get_right_key())
        elif node.get_right_key() is None:
            self.transplant(node_key, node.get_left_key())
        else:
            y = self.get_node(self.tree_minimum(node.get_right_key()))
            if y.get_parent_key() != node_key:
                self.transplant(y.get_key(), y.get_right_key())
                y.set_right_key(node.get_right_key())
                (self.get_node(y.get_right_key())).set_parent_key(y.get_key())
            self.transplant(node_key, y.get_key())
            y.set_left_key(node.get_left_key())
            (self.get_node(y.get_left_key())).set_parent_key(y.get_key())
        self.__nodes.remove(node)

    def get_node(self, node_key):
        find = False
        i = 0
        while not find and i < len(self.__nodes):
            if self.__nodes[i].get_key() == node_key:
                find = True
            i += 1
        if find:
            return self.__nodes[i - 1]
        else:
            return None

    def transplant(self, original_root_key, substitute_root_key):
        u = self.get_node(original_root_key)
        v = self.get_node(substitute_root_key)
        if u.get_parent_key() is None:
            self.__root = v
        elif original_root_key == (self.get_node(u.get_parent_key())).get_left_key():
            (self.get_node(u.get_parent_key())).set_left_key(substitute_root_key)
        else:
            (self.get_node(u.get_parent_key())).set_right_key(substitute_root_key)
        if substitute_root_key is not None:
            v.set_parent_key(u.get_parent_key())

    def tree_minimum(self, node_key):
        node = self.get_node(node_key)
        while node.get_left_key() is not None:
            node = self.get_node(node.get_left_key())
        return node.get_key()

    def height(self, node_key):
        if node_key is None:
            return 0
        else:
            return max(self.height((self.get_node(node_key)).get_left_key()), self.height((self.get_node(node_key)).get_right_key())) + 1

    def get_length(self):
        return len(self.__nodes)


class Arn:
    def __init__(self, nodes_key):
        self.__nodes = []
        self.__sentry = NodeArn(None)
        self.__root = self.__sentry
        if len(nodes_key) != 0:
            for i in range(0, len(nodes_key)):
                self.rb_insert(nodes_key[i])

    def rb_insert(self, node_key):
        node = NodeArn(node_key)
        self.__nodes.append(node)
        actual_parent = self.__sentry
        actual_node = self.__root
        while actual_node != self.__sentry:
            actual_parent = actual_node
            if node_key < actual_node.get_key():
                actual_node = actual_node.get_left()
            else:
                actual_node = actual_node.get_right()
        node.set_parent(actual_parent)
        if actual_parent == self.__sentry:
            self.__root = node
        elif node_key < actual_parent.get_key():
            self.get_node(actual_parent.get_key()).set_left(node)
        else:
            self.get_node(actual_parent.get_key()).set_right(node)
        node.set_left(self.__sentry)
        node.set_right(self.__sentry)
        node.set_color("Rosso")
        self.rb_insert_fixup(node)

    def rb_insert_fixup(self, node):
        parent = node.get_parent()
        while parent.get_color() == "Rosso":
            if parent == (parent.get_parent()).get_left():
                uncle = (parent.get_parent()).get_right()
                if uncle.get_color() == "Rosso":
                    (self.get_node(parent.get_key())).set_color("Nero")
                    (self.get_node(uncle.get_key())).set_color("Nero")
                    (self.get_node((parent.get_parent()).get_key())).set_color("Rosso")
                    node = parent.get_parent()
                    parent = node.get_parent()
                else:
                    if node == parent.get_right():
                        node = parent
                        parent = node.get_right()
                        self.left_rotate(self.get_node(node.get_key()))
                    (self.get_node(parent.get_key())).set_color("Nero")
                    (self.get_node((parent.get_parent()).get_key())).set_color("Rosso")
                    self.right_rotate(self.get_node((parent.get_parent()).get_key()))
            else:
                uncle = (parent.get_parent()).get_left()
                if uncle.get_color() == "Rosso":
                    (self.get_node(parent.get_key())).set_color("Nero")
                    (self.get_node(uncle.get_key())).set_color("Nero")
                    (self.get_node((parent.get_parent()).get_key())).set_color("Rosso")
                    node = parent.get_parent()
                    parent = node.get_parent()
                else:
                    if node == parent.get_left():
                        node = parent
                        parent = node.get_left()
                        self.right_rotate(self.get_node(node.get_key()))
                    self.get_node(parent.get_key()).set_color("Nero")
                    self.get_node((parent.get_parent()).get_key()).set_color("Rosso")
                    self.left_rotate(self.get_node((parent.get_parent()).get_key()))
        self.__root.set_color("Nero")

    def left_rotate(self, node):
        y = node.get_right()
        node.set_right(y.get_left())
        if y.get_left() != self.__sentry:
            (y.get_left()).set_parent(node)
        y.set_parent(node.get_parent())
        if node.get_parent() == self.__sentry:
            self.__root = y
        elif node == (node.get_parent()).get_left():
            (node.get_parent()).set_left(y)
        else:
            (node.get_parent()).set_right(y)
        y.set_left(node)
        node.set_parent(y)

    def right_rotate(self, node):
        y = node.get_left()
        node.set_left(y.get_right())
        if y.get_right() != self.__sentry:
            (y.get_right()).set_parent(node)
        y.set_parent(node.get_parent())
        if node.get_parent() == self.__sentry:
            self.__root = y
        elif node == (node.get_parent()).get_right():
            (node.get_parent()).set_right(y)
        else:
            (node.get_parent()).set_left(y)
        y.set_right(node)
        node.set_parent(y)

    def get_node(self, node_key):
        find = False
        i = 0
        while not find and i < len(self.__nodes):
            if self.__nodes[i].get_key() == node_key:
                find = True
            i += 1
        if find:
            return self.__nodes[i - 1]
        else:
            return None

    def height(self, node):
        if node.get_key() is None:
            return 0
        return max(self.height(node.get_left()), self.height(node.get_right())) + 1

    def get_root(self):
        return self.__root

    def get_length(self):
        return len(self.__nodes)

'''
keys = []
for i in range(0, 5000):
    keys.append(i)
random.shuffle(keys)
tree = Abr(keys)
h = tree.height(tree.get_root().get_key())
print("...")
'''
'''
ran1 = random.randint(0, 9)
ran2 = random.randint(0, 9)
while ran1 == ran2:
    ran2 = random.randint(0, 9)
tree.tree_delete(ran1)
tree.tree_delete(ran2)
'''
'''
keys = []
for i in range(0, 1000):
    keys.append(i)
#random.shuffle(keys)
tree = Arn(keys)
h = tree.height(tree.get_root())
print("...")
'''