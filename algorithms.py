def sutherland_cohen(segment, window):
    def compute_code(x, y, xmin, ymin, xmax, ymax):
        code = 0
        if x < xmin:
            code |= 1  # left
        elif x > xmax:
            code |= 2  # right
        if y < ymin:
            code |= 4  # bottom
        elif y > ymax:
            code |= 8  # top
        return code

    xmin, ymin, xmax, ymax = window
    (x1, y1), (x2, y2) = segment

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        if code1 == 0 and code2 == 0:
            return ((x1, y1), (x2, y2))
        elif code1 & code2 != 0:
            return None
        else:
            x, y = None, None
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & 8:  # top
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & 4:  # bottom
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & 2:  # right
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & 1:  # left
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)