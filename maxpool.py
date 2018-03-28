import numpy as np

def __max_pool(arr, win_sz, i_start, j_start):
    current = []
    for i in range(i_start, i_start + win_sz):
        for j in range(j_start, j_start + win_sz):
            current.append(arr[i,j])
    print('Current:',current)
    return max(current)

def max_pool(arr, win_sz):
    if len(arr) % win_sz != 0:
        raise AttributeError('Matrix must be divisible by window size')
    print('Array:')
    print(arr)
    i_start,j_start = 0,0
    iters = int((len(arr)*len(arr))/(win_sz*win_sz))
    new_size = int(len(arr)/win_sz)
    new = np.zeros((new_size,new_size))
    i,j,k = 0,0,0
    while k < iters:
        new[i,j] = __max_pool(arr, win_sz, i_start,j_start)
        if i == len(new)-1:
            i = 0
            i_start = 0
            j_start += win_sz
            j += 1
            k += 1
            continue
        i += 1
        i_start += win_sz
        k += 1
    return new

x = np.random.rand(12,12)
pool = max_pool(x, 2)
print('Maxpool: ')
print(pool)


# A much better implementation
def patchify(img, patch_shape):
    a, X, Y, b = img.shape
    x, y = patch_shape
    shape = (a, X - x + 1, Y - y + 1, x, y, b)
    a_str, X_str, Y_str, b_str = img.strides
    strides = (a_str, X_str, Y_str, X_str, Y_str, b_str)
    return np.lib.stride_tricks.as_strided(img, shape=shape, strides=strides)

x = np.random.randint(0,9,(10,24,24,3))
S = 5
out = patchify(x, (S,S)).max(axis=(3,4))


# My attempt to eliminate restrictions of NxN dimensional vector that is divisible by window size
def __max_pol(arr, win_sz, i_start, j_start):
    current = []
    for i in range(i_start, i_start + win_sz):
        for j in range(j_start, j_start + win_sz):
            current.append(arr[i,j])
    print('Current:',current)
    return max(current)

def max_pol(arr, win_sz, stride):
    print('Array:')
    print(arr)
    i_start,j_start = 0,0
    iters = int((len(arr)*len(arr))/(win_sz*win_sz))
    new_sizeM = int(len(arr)/win_sz)
    new_sizeN = int(len(arr)/stride) - 1
    new = np.zeros((new_sizeM,new_sizeN))
    i,j,k = 0,0,0
    while k < iters:
        new[i,j] = __max_pol(arr, win_sz, i_start,j_start)
        if i == len(new)-1:
            i = 0
            i_start = 0
            j_start += win_sz
            j += 1
            k += 1
            continue
        i += 1
        i_start += stride
        k += 1
    print()
    return new

# y = np.random.rand(4,4)
# print(max_pol(y,2,1))