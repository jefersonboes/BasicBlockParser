
class Parser:
    def load(self, sstr):
        self.cstr = sstr
        self.cpos = 0
    
    def get(self, pos, size):
        self.cpos = pos - 1
        return self.cstr[self.cpos : self.cpos + size]
    
    def get_p(self, pos, size, name):
        strp = ''
        if name != None:
            strp += name.center(6)
            strp += " "
            
        strp += str(str(pos) + ',' + str(size)).center(6) + ' ' + self.get(pos, size)
            
        print(strp)
        
    def assign(self, array):
        self.array = array
        
    def p_context(self):
        for field in self.array:
            name = None
            
            if len(field) > 2:
                name = field[2]
                
            self.get_p(field[0], field[1], name)
