# Reverse String
#
# Problem: Reverse an array of characters in-place using the two-pointer technique.
#
# Example: ["h","e","l","l","o"] → ["o","l","l","e","h"]
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def palindrome_ornot(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return "not a palindrome"
        left += 1
        right -= 1
    return "a palindrome"


if __name__ == "__main__":
    input_str = input("Enter the input string").replace(" ", "")
    char_list = list(input_str)
    rev_str = reverse_string(char_list)
    print("Reversed String is", ''.join(rev_str))
    palin_ornot = palindrome_ornot(input_str)
    print("String is ", palin_ornot)

