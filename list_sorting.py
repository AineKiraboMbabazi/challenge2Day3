def list_sort(list1):
    
    even=[]
    odd=[]
    characters=[]
    mydict=dict()
    
    for i in list1:
        if isinstance(i, str):
            characters.append(i)
            mydict['chars']=characters
        elif isinstance(i, int):

            if i%2==0:
                even.append(i)
                mydict['evens']=even
            else:
                odd.append(i)
                mydict['odds']=odd
        
           
    return mydict

if __name__ == '__main__':
    list1=[2,0,6,5,1,7,'z','a']
   
    print(list_sort(list1))