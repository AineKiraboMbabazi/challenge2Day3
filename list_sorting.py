def list_sort(list1):
    
    even=[]
    odd=[]
    characters=[]
    mydict=dict()
    
    for i in list1:
        if isinstance(i, str):
            characters.append(i)
            mydict['chars']=sorted(characters)

        elif isinstance(i, int):
            if i%2==0:
                even.append(i)
                mydict['evens']=sorted(even)
            else:
                odd.append(i)
                mydict['odds']=sorted(odd)

        elif not(isinstance(i,str) and isinstance(i, int)):
            return 'invalid input type, the list should have either characters or intergers'
           
    return mydict

if __name__ == '__main__':
    list1=[2,0,6,5,1,7,'z','a']
   
    print(list_sort(list1))
    print(list_sort([2,3,4,{3:9,4:16}]))