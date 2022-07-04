from math import cos, pi


def transform(vector):
    result = []
    factor = pi / len(vector)
    
    for i in range(len(vector)):
        s = 0.0
        k0 = i * factor
        
        for j in range(len(vector)):
            v = vector[j]
            s += v * cos((j + 0.5) * k0)
        
        result.append(s)
    
    return result


def inverse_transform(vector):
    result = []
    factor = pi / len(vector)
    k2 = 2.0 / len(vector)
    
    for i in range(len(vector)):
        s = vector[0] / 2.0
        k1 = (i + 0.5) * factor
        
        for j in range(1, len(vector)):
            v = vector[j]
            s += v * cos(j * k1)
        
        s *= k2
        result.append(s)
    
    return result


def ex0():
    v0 = [0.0, 1.0, 2.0, 3.0, 10.0, 1.0, 2.0]
    print('v0', v0)
    
    w0 = transform(v0)
    print('w0', w0)

    r0 = inverse_transform(w0)
    print('r0', r0)


if __name__ == '__main__':
    ex0()
