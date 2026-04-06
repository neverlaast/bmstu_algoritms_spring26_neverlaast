def binary_search(matrix, k):

    # задаём границы поиска
    length_matrix = len(matrix)
    left = matrix[0][0]
    right = matrix[length_matrix-1][length_matrix-1]
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        row = 0
        col = length_matrix - 1

        # считаем сколько элементов меньше mid с правого верхнего угла
        while row < length_matrix and col >= 0:
            if matrix[row][col] <= mid:
                count += col + 1
                row += 1
            else:
                col -= 1

        # бинарный поиск
        if count < k:
            left = mid + 1
        else:
            right = mid
    
    return left
    