def list_sort(lista):
    
    even=[]
    odd=[]
    characters=[]
    mydict=dict()
    if not isinstance(lista,list):
        return 'Invalid Input'

    if len(lista)==0:
        mydict['evens']=even 
        mydict['odds']=odd
        mydict['chars']=characters

    for i in lista:
        
        if isinstance(i, int):
            if i%2==0:
                even.append(i)
                mydict['evens']=sorted(even)
            else:
                odd.append(i)
                mydict['odds']=sorted(odd)
        
            
        elif isinstance(i, str):
            characters.append(i)
            mydict['chars']=sorted(characters)

        

        elif not(isinstance(i,str) and isinstance(i, int)):
            return 'invalid input type, the list should have either characters or intergers'
    
    if len(even)==0:   
        
        return mydict['evens']=even 

    if len(odd)==0:
        
        return mydict['odds']=odd

    if len(characters)==0:
        
        return mydict['chars']=characters
        
    
         
    return mydict

