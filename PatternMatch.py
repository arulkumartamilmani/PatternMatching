def patternMatching(pattern,phrase):
    #Split the pattern and Phrases into lists 
    # Assumption - Pattern is a single word and Phases are seperated with spaces
    s_pattern = split(pattern)
    s_phrase = phrase.split(" ")
    r_phase  = []
    kp_dict = {}
    res=False

    u_pattern = unique(s_pattern)  
    u_phrase = unique(s_phrase)
    if (len(u_pattern) == len(u_phrase)) and (len(s_pattern) == len(s_phrase)):
        # Create Key Pair value dictionary 
        for i in range(len(u_pattern)):
            kp_dict[u_pattern[i]] = u_phrase[i]
        # Decode with Key Pair Values
        for i in range(len(s_pattern)):
            r_phase.append(kp_dict.get(s_pattern[i]))
        # Compare the Lists
        if (s_phrase==r_phase):
            res=True
    
    return res

        

def split(text):
    return [char for char in text]

def unique(lst):
    unique_lst=[]
    for x in lst:
        if x not in unique_lst:
            unique_lst.append(x)
    return unique_lst

# Tests

print(patternMatching("abc","This is nice"))
print(patternMatching("xy", "Hello Hey Fox"))
print(patternMatching("xyz", "Hey Hey Hey"))
print(patternMatching("xyz","Hey Fox Fox"))
print(patternMatching("xtz","Test Now"))


assert patternMatching("abc","This is nice") == True
assert patternMatching("xy", "Hello Hey Fox") == False
assert patternMatching("xyz", "Hey Hey Hey") == False
assert patternMatching("xyz","Hey Fox Fox") == False
assert patternMatching("xtz","Test Now") == False