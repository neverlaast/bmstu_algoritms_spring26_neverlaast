def max_string(s):
    
    letter_ind = {}
    left = 0
    max_length = 0
    right = 0
    
    while right < len(s):
        letter = s[right]

        if letter in letter_ind and letter_ind[letter] >= left:
            left = letter_ind[letter] + 1

        letter_ind[letter] = right
        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

        right += 1
    

    return max_length
    