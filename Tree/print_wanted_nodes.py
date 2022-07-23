class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
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
    def print_tree(self,wanted):
        if wanted == 'both':
            value = self.name + " (" + self.designation + ")"
        elif wanted == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level()*3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(wanted)

def build_tree():
    root = TreeNode('Electronics','E')

    Laptop = TreeNode('Laptop','L')
    Laptop.add_child(TreeNode('mac',"m"))
    Laptop.add_child(TreeNode('realme','r'))
    Laptop.add_child(TreeNode('Hp','H'))

    Mobiles = TreeNode("Mobiles",'M')
    Mobiles.add_child(TreeNode('xiaomi','X'))
    Mobiles.add_child(TreeNode('Nokia','N'))
    Mobiles.add_child(TreeNode('iphone','i'))

    TV = TreeNode("TV",'T')
    TV.add_child(TreeNode('LG','L'))
    TV.add_child(TreeNode("Sansui",'S'))
    TV.add_child(TreeNode("Oneplus",'O'))

    root.add_child(Laptop)
    root.add_child(Mobiles)
    root.add_child(TV)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree('both')
    root.print_tree('name')
    root.print_tree('desigantion')
