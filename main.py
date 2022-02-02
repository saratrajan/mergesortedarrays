class Solution(object):
    
    arr3 = []
    
    '''
    This function accepts both the arrays as input, taking for granted that they are already sorted in ascending order
    '''
    
    def merged_array(arr1, arr2):
        i = 0 #first array's pointer
        j = 0 #second array's pointer
        k = 0 #third array's pointer
        ## Checking if both arrays are empty        
        if(len(arr1) == 0 and len(arr2) == 0):
            print("Both arrays are empty!")
            print("Merged array is []")
        else:
            ## Getting desired length of merged array
            desired_length = len(arr1) + len(arr2)
            arr3 = [0] * desired_length  
        while(i < len(arr1) and j < len(arr2)):
        ## Checking if current element of arr1 is smaller than that in arr2  
            if(arr1[i] < arr2[j]):
                arr3[k] = arr1[i]
                i += 1
                k += 1
            else:
                arr3[k] = arr2[j]
                j += 1
                k += 1
        ## Checking for the remaining elements in arr1        
        while i < len(arr1):
            arr3[k] = arr1[i]
            i += 1
            k += 1
        ## Checking for the remaining elements in arr2
        while j < len(arr2):
            arr3[k] = arr2[j]
            j += 1
            k += 1
        ## printing the merged array
        print(arr3)        
            
    arr1 = [1,3,4,5,6]
    arr2 = [1,2,5,6]
    merged_array(arr1,arr2)
