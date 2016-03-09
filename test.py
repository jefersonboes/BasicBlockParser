from basic_block_parser import Parser

p = Parser()

p.assign([
    [1, 3],
    [4, 1],    
    [5, 20, "named"],
    [25, 1],
    ])

p.load("1235test0123456789test012")

p.p_context()
