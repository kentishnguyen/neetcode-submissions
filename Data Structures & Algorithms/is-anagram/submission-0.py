class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if (len(s) == len(t)):
            # sorted() sorts lists, arrays, tuples, dicts in ascending order unlike .sort() which only is used for sorting lists
            sNew = sorted(s)  
            tNew = sorted(t)
            for item in s:
                if item not in s_map:
                    s_map[item] = 1
                else:
                    s_map[item] += 1

            for item in t:
                if item not in t_map:
                    t_map[item] = 1
                else:
                    t_map[item] += 1
            if (len(s_map) == len(t_map)):
                for key in s_map:
                    if key in t_map:
                        if (s_map[key] != t_map[key]):
                            return False
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False
