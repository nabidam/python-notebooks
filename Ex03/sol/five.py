# Take input for the two strings
str1 = input("Enter the first string: ").strip()
str2 = input("Enter the second string: ").strip()

# Check if the lengths of the strings are different
if len(str1) != len(str2):
    print("The strings are not isomorphic (different lengths).")
    exit()

# Create dictionaries to store mappings from str1 to str2 and vice versa
mapping_str1_to_str2 = {}
mapping_str2_to_str1 = {}

# Iterate through the characters of both strings
for char1, char2 in zip(str1, str2):
    # Check if char1 has already been mapped
    if char1 in mapping_str1_to_str2:
        if mapping_str1_to_str2[char1] != char2:
            print("The strings are not isomorphic.")
            exit()
    else:
        mapping_str1_to_str2[char1] = char2
    
    # Check if char2 has already been mapped
    if char2 in mapping_str2_to_str1:
        if mapping_str2_to_str1[char2] != char1:
            print("The strings are not isomorphic.")
            exit()
    else:
        mapping_str2_to_str1[char2] = char1

# If all checks pass, the strings are isomorphic
print("The strings are isomorphic.")