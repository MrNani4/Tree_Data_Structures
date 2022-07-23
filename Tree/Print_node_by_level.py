class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' '* self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
def build_tree():
    root = TreeNode('Animals')

    land = TreeNode('Land Animals')

    herbivors = TreeNode('Herbivorus')
    herbivors.add_child(TreeNode('Dear'))
    herbivors.add_child(TreeNode('Rabbit'))

    cornivours = TreeNode('Cornivours')
    cornivours.add_child(TreeNode('Lion'))
    cornivours.add_child(TreeNode('Tiger'))

    land.add_child(herbivors)
    land.add_child(cornivours)

    water = TreeNode("Water Animals")

    large = TreeNode("Large")
    large.add_child(TreeNode('Shark'))
    large.add_child(TreeNode("Whale"))

    small = TreeNode("Small")
    small.add_child(TreeNode("Star fish"))
    small.add_child(TreeNode("Jelly fish"))

    water.add_child(large)
    water.add_child(small)

    root.add_child(land)
    root.add_child(water)

    return root
if __name__ == '__main__':
    root = build_tree()
    root.print_tree(1)
