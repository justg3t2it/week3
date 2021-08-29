#Assignment:

Reverse an integer
Input: string
Output: string 

Example use cases: 
1245    = 5421
1,245.2 = 2,542.1
3,200   = 23 

Breakdown: 

Will need to convert the string to a list to manipulate string characters or slice string 


Pseudocode: 

1. check for an empty string, if empty return string

2. initate var to length of the string 
    a. use the length of string to initiate a list 

3. traverse all characters in original string, if they have special characters, assign to empty
    a. this would turn: 1,023,555 into 1023555

4. turn list into string with all elements joined by empty space to keep string the same
    a. reverse the string, string should now be:
        1023555 = 5553201

5. compare reversed string to original string (have same char) 
    a. if the char in position x in original string is "," or "." split string from start to position x, add the comma or period, then add back the string from position x to end 

    b. have two if statements to account for comma or decimal

return the string

Thoughts: 

1. need to account for leading 0s cases, 3,2000 is currently returning 0,0023 not 23

2. convert to list after address leading 0s? 

3. potentially have a flag after going through the string originally: 

flip it, check for leading 0s, 
while flipped, check for punction

if leading 0s and punctuation == true, remove leading zeros, return list (do not need commas,periods) and convert to string 

if no leading 0s and punctuation == true, compare to original string, add punctiation, return list and convert to string 



    









