##FIXME: Find the maximum number of fruits one can pick given the basket constraint(at most two types of fruit.).
#Examples:
#
#Input: arr[]= [2, 1, 2]
#Output: 3
#Explanation: The entire array [2, 1, 2] contains at most two distinct integers (2 and 1). Hence, the length of the longest subarray is 3.
#example 2:
# Input: arr[] = [3, 1, 2, 2, 2, 2]
# Output: 5
# Explanation: The longest subarray containing at most two distinct integers is [1, 2, 2, 2, 2], which has a length of 5. The subarray starts at the second element 1 and ends at the last element. It contains at most two distinct integers (1 and 2).
# #FIXME: so we gotta find maximum length of a subarray with atmost two types of numbers.


#TODO: The brute force solution, we go through every single subarray and then check if the subarray element is limited to two only using a set data structure. if the length of the set is greater than 2, we skip and continue.
#NOTE: if not we check the maxlen and then we return it at the end.

def brute(nums:list[str]) -> int:

    n = len(nums)
    max_fruits = 0 #NOTE: initialise this to 0, this is the answer holder.

    for i in range(n):
        for j in range(i,n):
            sub_array = nums[i:j+1] #NOTE: instead of doing it manually, we are just assigning it to a variable.
            unique_fruits = set(sub_array) #NOTE: using a set to efficiently find unique fruits.

            #NOTE: if the length of the set is less than or equal to two , then we check the maxlength 
            if len(unique_fruits) <= 2:
                max_fruits = max(max_fruits,len(sub_array))
    return max_fruits

#HACK : This will take O(N^2) Time complexity since there are two for loops.
#HACK: This will take O(3), as space complexity since the max numbers in the set is only 3.






#TODO: This obviosly uses sliding window protocol, 
#NOTE: in this optimal version we use a dictionary rather than using a set data structure.
def optimal(fruits: list[str]) -> int:
    left = 0 #NOTE: this is the left pointer for the window.
    fruit_count = {} #NOTE: This is a dictionary, that counts the frequency of each type of fruit.
    n = len(fruits)
    max_fruits = 0 #NOTE: answer holder.

    for right in range(n): 
        fruit = fruits[right] #NOTE: this holds the current fruit or element, in the array.
        #NOTE: in the dictionary we update the frequency of the current fruit by first getting the value of the current fruit and then updating it.
        fruit_count[fruit] = fruit_count.get(fruit,0) + 1
 
        #NOTE: while loop for window resizing.
        while len(fruit_count) > 2: #NOTE: while the fruit_count is greater than 2, which is not optimal.
            left_fruit = fruits[left] #NOTE: take the first fruit of the current sub_array and then decrement the frequency of that fruit indication of removing one element from the dictionary.
            fruit_count[left_fruit] -= 1

        #NOTE:this part contains if the frequency of a fruit is zero, then we should delete it from the dictionary.
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1 #NOTE: and then we increment the left pointer , decreasing the size of the window.

        max_fruits = max(max_fruits, right-left + 1) #NOTE: counting the max_fruits that sub_array can accomodate at the end.
    return max_fruits

def main():
    """
    Main function to demonstrate the fruit_into_baskets_optimal function.
    """

    test_cases = [
        ["A", "B", "C", "A", "C", "B", "B"],
        ["A", "B", "A", "B", "C", "B", "A"],
        ["A", "A", "A", "B", "B", "B", "C", "C", "C"],  # Test case with long sequences
        ["A", "B", "C", "D"],  # Test case with more than 2 types
        ["A", "A", "A"],  # Test case with only one type
        [],  # Test case with empty input
        ["A", "B"] # Test case with 2 types
    ]

    for fruits in test_cases:
        result = optimal(fruits)
        print(f"Fruits: {fruits}, Max Fruits: {result}")


if __name__ == "__main__":  # Ensures main() is called only when the script is run directly
    main()

