import pickle

# write17
p2file = open("parse_trees/write17_pt_kh.pkl", "rb")
write17_tree2 = pickle.load(p2file)
print("PT for write17:")
print("Root type = ", type(write17_tree2))
print(type(write17_tree2))
write17_tree2.dump()
print()

# readwrite
p2file = open("parse_trees/readwrite_pt_kh.pkl", "rb")
readwrite_tree2 = pickle.load(p2file)
print("PT for readwrite:")
readwrite_tree2.dump()
print()

# onetoten
#p2file = open("onetoten_pt_kh.pkl", "rb")
#onetoten_tree2 = pickle.load(p2file)
#print("PT for onetoten:")
#onetoten_tree2.dump()
#print()

p2file = open("parse_trees/factorial_pt_kh.pkl", "rb")
factorial_tree2 = pickle.load(p2file)
print("PT for factorial:")
factorial_tree2.dump()
print()


