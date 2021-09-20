from random import choice

class cell(object) :
    def __init__(self, pos_x, pos_y, cell_size, color_palette) :
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cell_size = cell_size
        self.free_space = []
        self.color_palette = color_palette

        self.draw_big_triangle(self.pos_x, self.pos_y)
        for emplacement in self.free_space :
            if emplacement == 1 :
                self.draw_small_triangles(self.pos_x, self.pos_y)
            elif emplacement == 2 :
                self.draw_small_triangles(self.pos_x + self.cell_size / 2 , self.pos_y)
            elif emplacement == 3 :
                self.draw_small_triangles(self.pos_x, self.pos_y + self.cell_size / 2)
            elif emplacement == 4 :
                self.draw_small_triangles(self.pos_x + self.cell_size / 2, self.pos_y + self.cell_size / 2)
            else :
                raise ValueError

    def draw_small_triangles(self, pos_x, pos_y, random_axis = True, axis = "U") :
        if random_axis :
            axis = choice(["U", "L", "R", "D"])
        else :
            axis = axis
        
        r, g, b = choice(self.color_palette)
        fill(r, g, b)
        if axis == "U" :
            triangle(pos_x, pos_y + self.cell_size / 2, pos_x + self.cell_size / 2, pos_y + self.cell_size / 2, pos_x + self.cell_size / 4, pos_y)
        elif axis == "L" :
            triangle(pos_x, pos_y, pos_x, pos_y + self.cell_size  / 2, pos_x + self.cell_size / 2, pos_y + self.cell_size / 4)
        elif axis == "R" :
            triangle(pos_x + self.cell_size / 2, pos_y, pos_x + self.cell_size / 2, pos_y + self.cell_size / 2, pos_x, pos_y + self.cell_size / 4)
        elif axis == "D" :
            triangle(pos_x, pos_y, pos_x + self.cell_size / 2, pos_y, pos_x + self.cell_size / 4, pos_y + self.cell_size / 2)
        else :
            raise ValueError


    def draw_big_triangle(self,
                          pos_x,
                          pos_y,
                          random_axis = True,
                          random_half = True,
                          axis = "U", half = 1):
        """TODO Doc"""
        # checking for the random axis mode ( if True give back 1 axis between the 4 possibles )
        if random_axis:
            axis = choice(["U", "L", "R", "D"])
        else:
            axis = axis

        # checking random half mode ( if True give back 1 half between the 2 possibles )
        if random_half:
            half = choice([1, 2])
        else:
            half = half

        if half == 2 and (axis == "R" or axis == "L") :
            pos_x += self.cell_size / 2
            self.free_space.append(1)
            self.free_space.append(3)
        elif half == 2 and (axis == "D" or axis == "U") :
            pos_y += self.cell_size / 2
            self.free_space.append(1)
            self.free_space.append(2)
        elif half == 1 and (axis == "R" or axis == "L") :
            self.free_space.append(2)
            self.free_space.append(4)
        elif half == 1 and (axis == "D" or axis == "U") :
            self.free_space.append(3)
            self.free_space.append(4)


        r, g, b = choice(self.color_palette)
        fill(r, g, b)
        if axis == "U":
            triangle(pos_x, pos_y, pos_x + self.cell_size, pos_y, pos_x + self.cell_size / 2, pos_y + self.cell_size / 2)
        elif axis == "D":
            triangle(pos_x, pos_y + self.cell_size / 2, pos_x + self.cell_size, pos_y + self.cell_size / 2, pos_x + self.cell_size / 2,
                     pos_y)
        elif axis == "L":
            triangle(pos_x, pos_y, pos_x + self.cell_size / 2, pos_y + self.cell_size / 2, pos_x, pos_y + self.cell_size)
        elif axis == "R":
            triangle(pos_x + self.cell_size / 2, pos_y, pos_x + self.cell_size / 2, pos_y + self.cell_size, pos_x,
                     pos_y + self.cell_size / 2)
