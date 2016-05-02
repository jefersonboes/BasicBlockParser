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

p.assign_pos([
    [3],
    [1],
    [20, "named"],
    [1],
    ])

p.load("1235test0123456789test012")

p.p_context()
