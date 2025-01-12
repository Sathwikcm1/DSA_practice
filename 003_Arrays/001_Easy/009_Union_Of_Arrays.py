#FIXME: Union of Arrays: union of two arrays include all the elements of both of the array, but the elements are not repeated.
#TODO: well we can use sets for that, sets cannot contain the duplicate elements.
#add elements of both the arrays into the set and print it.
def brute_force(arr1,arr2):
    st = set()
    for i in range(len(arr1)):
        st.add(arr1[i])
    for i in range(len(arr2)):
        st.add(arr2[i])
    print(st)


def dictionaries(arr1,arr2):
    freq = {} #NOTE: initializing dictionary.
    union = [] #NOTE: The answer array.
    
    for num in arr1:
        freq[num] = freq.get(num,0) + 1

    for num in arr2:
        freq[num] = freq.get(num,0) + 1

    for num in freq:
        union.append(num)
    return union
#NOTE: Notes about dictionaries in python:
# declaration of dictionary: my_dic = {'key1' : 'value1', 'key2', 'value2'} or my_dic = dict(key1 = 'value1', key2 = 'value2')
# common dictionary methods. 
# get: returns the value for the specified key.ex: value = my_dic.get('key1','default value') , if the key doesn't exists it will return the default value itself.
# keys() : returns a view object that displays a list of all the keys in the dictionary.
# ex: keys = my_dic.keys() , returns (['key1,key2...']) etc.
# values(): Returns a view object that displays a list of all the values in the dictionary.
# ex: values = my_dic.values() , returns all the values (['value1','value2'...])
# items(): returns a view object that displays a list of dictionary's key-value pairs.
# update(): my_dic.update({'key3': 'value3'}), adds key3 to the dictionary.
# pop(key, default=None) , removes the specific key and returns it's value. if the key is not found, returns the default.



#TODO: Using two pointer method:
def two_pointer(arr1,arr2):
    i,j = 0,0 #NOTE: pointers.
    union = [] #Union list.


    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1

    while i < len(arr1):
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1 

    while j < len(arr2):
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6]
    arr2 = [4,5,6,3,2,4,6]
    brute_force(arr1,arr2)

    ans = dictionaries(arr1,arr2)
    print(*ans)
    ans2 = two_pointer(arr1,arr2)
    print(*ans2)
