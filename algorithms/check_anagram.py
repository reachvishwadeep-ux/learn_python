"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, "listen" and "silent" are anagrams of each other.

use sorted() function to sort the characters of both strings and compare them. If they are equal, then the strings are anagrams of each other.

"""
def checkAnagram(string_1, string_2):
    isAnagram = False
    
    if(sorted(string_1) == sorted(string_2)):
        isAnagram = True
  
    
    return isAnagram

print(checkAnagram("ldaaa", "daldd"))