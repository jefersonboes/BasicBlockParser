"""
 * BasicBlockParser - Parse simplest files into blocks
 * Copyright (C) 2016 Jeferson Boes
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
"""

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

    def assign_pos(self, array):
        new_array = []
        pos = 1
        for field in array:
            new = []
            new.append(pos)
            new.append(field[0])
            if len(field) > 1:
                new.append(field[1])

            new_array.append(new)
            pos = pos + field[0]

        self.array = new_array
        
    def p_context(self):
        for field in self.array:
            name = None
            
            if len(field) > 2:
                name = field[2]
                
            self.get_p(field[0], field[1], name)
