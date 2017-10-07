        
        

''' listings add amenities '''        
import re
unique_amen=[]
uni_counts=[]
amen=listings['amenities'].values.tolist()
for a in amen:
    #print(a)
    if type(a)==str:
        coun=a.split(",")
        lis=[re.sub('["{}]','',i) for i in coun]
        for l in lis:
            unique_amen.append(l)
        uni_counts.append(len(lis))    
        
uni_coun=list(set(unique_amen))[1:]

#print(len(uni_counts))
                
amen_count={}    
for u in uni_coun:
    cnt=[]
    #print (u)
    for a in amen:
            coun=a.split(",")
            lis=[re.sub('["{}]','',i) for i in coun]
            if u in lis:
                cnt.append(1)
            else:
                cnt.append(0)
    amen_count[u]=cnt
    
for k in amen_count.keys():
    listings[k]=amen_count[k]
    
'''total amenities'''
listings['total_amenities']=uni_counts

listings['price']=[float(re.sub("[$,]","",i)) for i in listings['price'].values.tolist()]
            
        
        

        
        





    







