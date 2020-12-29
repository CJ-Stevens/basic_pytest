def rectangle(w, h):
    if w <= 0 or h <= 0:
        raise ValueError('w, h must be greater than zero.')
    return w * h
    

def triangle(b, h):
    return .5 * b * h

if __name__ == "__main__":
    print(rectangle(5, 3))