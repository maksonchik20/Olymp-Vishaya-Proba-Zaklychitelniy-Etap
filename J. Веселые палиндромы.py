def test_good_s(s):
    sl = {}
    for char in s:
        if sl.get(char) is None:
            sl[char] = 1
        else:
            sl[char] += 1
            if sl.get(char) > 2:
                return False
    return True

def all_palindromes(text):
    cnt = len(text)
    text_length = len(text)
    for idx, char in enumerate(text):
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            if test_good_s(text[start:end+1]):
                cnt += 1
            start -= 1
            end += 1

        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            if test_good_s(text[start:end+1]):
                cnt += 1
            start -= 1
            end += 1
    return cnt


print(all_palindromes(input()))