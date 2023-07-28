'''
Calculate name similarity using Levenshtein distance algorithm
'''

def check_name_similarity(name_x, name_y):
    # Convert names to lowercase
    name_x = name_x.lower()
    name_y = name_y.lower()

    # Calculate the Levenshtein distance
    matrix = [[0] * (len(name_y) + 1) for _ in range(len(name_x) + 1)]
    for i in range(len(name_x) + 1):
        matrix[i][0] = i
    for j in range(len(name_y) + 1):
        matrix[0][j] = j
    for i in range(1, len(name_x) + 1):
        for j in range(1, len(name_y) + 1):
            cost = 0 if name_x[i - 1] == name_y[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    # Calculate the similarity percentage
    max_length = max(len(name_x), len(name_y))
    similarity_percentage = ((max_length - matrix[-1][-1]) / max_length) * 100

    return similarity_percentage

# To use the function in the same file, just use check_name_similarity("name_x", "name_y")
# To use the function in another file in the same directory, import the function first "from check_name_similarity import *" (without quotation), then call the function by using check_name_similarity("name_x", "name_y")