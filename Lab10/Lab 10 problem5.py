def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def main():
    str1 = "enraged"
    str2 = "angered"

    if is_anagram(str1, str2):
       print ("The two strings are anagrams")
    else:
       print ("The two strings are not anagrams")

main()



#sorted function runtime (O(N*log N))







