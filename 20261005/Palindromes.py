# 根據題目表格建立鏡像字典
mirror_map = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
    'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
    '3': 'E', '5': 'Z', '8': '8'
}

# 若題目提到 '0' (數字零) 和 'O' 視為相同，需在讀入字串時先做替換
def get_mirror(ch):
    if ch == '0':
        ch = 'O'  # 把 '0' 轉成 'O'
    # 如果有鏡像就傳回鏡像字元，沒有則傳回 None
    return mirror_map.get(ch, None)




def palindrome(s):
    s = s.replace('0', 'O')

    left = 0
    right = len(s) - 1

    is_p = True  # 是否為迴文
    is_m = True  # 鏡像

    while left<=right:
        #迴文
        if s[left] != s[right]:
            is_p = False
        #鏡像
        if get_mirror(s[left]) != s[right]:
            is_m = False

        left += 1
        right -= 1
        
    return is_p, is_m











import sys

for line in sys.stdin:
    text = line.strip()
    if not text:
        continue  
    is_p, is_m = palindrome(text)  
        
    if is_p and is_m:
                print(f"{text} -- is a mirrored palindrome.\n")
    elif is_m:
                print(f"{text} -- is a mirrored string.\n")
    elif is_p:
                print(f"{text} -- is a regular palindrome.\n")
    else:
                print(f"{text} -- is not a palindrome.\n")