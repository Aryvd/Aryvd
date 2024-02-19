import jpeglib

def extract(matrix):
    msg = ''
    for i in range(len(matrix)):
        msg += str(matrix[i][i] % 2)  # get lsb of diagonal of the matrix
    return msg

def time_based_prng(seed=None):
    state = seed

    while True:
        state = (state * 1103515245 + 12345) & 0x7FFFFFFF
        yield state

def extract_message_from_image(seed):
    im_modified = jpeglib.read_dct(str(seed) +'.jpg')
    msg_extracted = ''
    arr0 = [0] * 100
    arr1 = [0] * 100
    prng = time_based_prng(seed)
    for i in range(100):
        arr0[i] = next(prng) % 128
        arr1[i] = next(prng) % 128
    for i in range(100):
        msg_extracted += extract(im_modified.Y[arr0[i]][arr1[i]])

    return msg_extracted

seed_value = 5613721136707  
extracted_msg = extract_message_from_image(seed_value)
print("Extracted message:", extracted_msg)
