class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: a string 
        # output: a boolean value saying whether the input string is a palindrome or not
        # having 2 pointers 1 at the beginning of the string and another at the end of the string moving in opposite directions (the begin pointer moves to the end of the string and the end pointer moves to the beginning of the string). Then we compare the pointing values of the 2 pointers at each iteration
        # if their values are equal then keep on iterating until i < ceiling of (string.len() / 2) (where i is the indexing var)
        # |aaaaaaa| / 2 = 3.5; |aaaaaa| / 2 = 3 
        # question: do we take white spaces between words into consideration? --> No 
        # question: how do we strip white spaces in a string?
        # first -> strip white spaces in the string -> have a loop iterating less than the ceiling of string's size / 2 -> have 2 pointers 
        # strip whitespaces
        #s.replace(" ", "")
        s1 = s.lower()
        cleaned = []
        for item in s1:
            if item.isalnum():
                cleaned.append(item)
        j = len(cleaned) - 1
        for i in range(0, -(len(cleaned)// -2)):
            
            if (cleaned[i] != cleaned[j]):
                return False
            j -= 1
        return True
        

