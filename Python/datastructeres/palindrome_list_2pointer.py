def _ispalindrome_(List:list) -> bool:
    for idx,_ in enumerate(List):
        rev = (len(List)-1) - idx
        if List[idx] != List[rev]:
            return False
        if idx == rev:
            break
    return True

def gptBro_said_to_do_ts(List:list) -> bool:
    left = 0
    length = (len(List)-1)
    for i in List:
        right = length-left
        if List[left] != List[right]:
            return False
        if left>=right:
            break
        left +=1
    return True

print(gptBro_said_to_do_ts([1, 2, 1]))        # True — odd palindrome
print(gptBro_said_to_do_ts([1, 2, 2, 1]))     # True — even palindrome
print(gptBro_said_to_do_ts([1, 2, 3]))        # False — not a palindrome
print(gptBro_said_to_do_ts([5, 5]))           # True — two equal elements
print(gptBro_said_to_do_ts([5, 4]))           # False — two different elements
print(gptBro_said_to_do_ts([7]))              # True — single element
print(gptBro_said_to_do_ts([1, 2, 3, 1]))     # False — mismatch near the end
print(gptBro_said_to_do_ts([3, 1, 2, 1, 3]))  # True — longer palindrome