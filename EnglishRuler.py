def draw_line(length,label=""):
    line= "-"*length
    if label:
        line+= " " + label
    print(line)

def draw_interval(length):
    if length>0:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)

def draw_ruler(inches,major_length):
    draw_line(major_length,'0')
    for i in range(1, inches+1):
        draw_interval(major_length-1)
        draw_line(major_length,str(i))

draw_ruler(2,4)
