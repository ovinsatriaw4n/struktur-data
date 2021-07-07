q = "y"
b = ""
while(q == "y"):
    def binary_tree(x):
        return [x, [], []]
    def insert_left(root, new_branch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [new_branch, t, []])
        else:
            root.insert(1, [new_branch, [], []])
            return root
    def insert_right(root, new_branch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2, [new_branch, [], t])
        else:
            root.insert(2, [new_branch, [], []])
        return root
    def get_root_val(root):
        return root(0)
    def set_root_val(root, new_val):
        root[0] = new_val
    def get_left_child(root):
        return root[1]
    def get_right_child(root):
        return root[2]

    cuaca = str(input("masuk cuaca :"))
    x =binary_tree ("cuaca")
    insert_left (x, str(input("akar :")))
    insert_left (x, str(input("ranting :")))
    insert_right (x, str(input("kiri:")))
    insert_right (x, str(input("kanan :")))
    l=get_left_child(x)
    print (x)
    if(cuaca == "hujan") or (b == "angin"):
        print("hasil : tidak")
    elif (b == "cerah") or (b == "lembab"):
        print("hasil : main")
    q = input("ulang lagi")
