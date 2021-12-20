def char_array(self, background):
    array = []
    
    try:
        for x in range(self.width):
            array.append(background)
    except:
        for x in range(self.width):
            array.append(" ")
    final_array = []
    for y in range(self.height):
        final_array.append(array)
    return final_array