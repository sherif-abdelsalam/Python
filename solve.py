from elimination_recursion import CFG

input_string = "S;T;L#a;b;c;d;i#S/ScTi,La,Ti,b;T/aSb,LabS,i;L/SdL,Si"

cfg = CFG(input_string)
print("\nBefore left recursion elimination:")
print (cfg.toString())

cfg.eliminate_left_recursion()

print("\nAfter left recursion elimination:")
print(cfg.toString())
print("\n")