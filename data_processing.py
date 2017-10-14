# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:46:39 2017

@author: Jay
"""

import pandas as pd
from sklearn import preprocessing


def clean_listings():

    listings=pd.read_csv("Data/listings.csv")

    # cleaning zip
    lis_zip=set(listings['zipcode'].values.tolist())
    lis_zip_c=[str(i)[0:5].lstrip('0') for i in lis_zip if len(str(i))>0]
    lis_zip_cl=[]
    for l in lis_zip_c:
        if l.isdigit():
            lis_zip_cl.append(int(l))
        else:
            lis_zip_cl.append(0)


    # dummy variable creation

    list_city=pd.get_dummies(listings['city'])
    list_metro=pd.get_dummies(listings['metropolitan'])
    list_proptype=pd.get_dummies(listings['property_type'])
    list_rotype=pd.get_dummies(listings['room_type'])
    list_cancel=pd.get_dummies(listings['cancellation_policy'])
    list_instant=listings['instant_bookable']=='t'
    list_instant=list_instant.astype('int')

    dum_var=pd.concat([list_city,list_metro,list_proptype,list_rotype,list_cancel,list_instant],axis=1)

    del listings['city']
    del listings['metropolitan']
    del listings['property_type']
    del listings['room_type']
    del listings['cancellation_policy']
    del listings['instant_bookable']
    listings=pd.concat([listings, dum_var], axis=1)
    # processing amenities
          
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
    # listings['weekly_price']=[float(re.sub("[$,]","",i)) for i in listings['weekly_price'].values.tolist()]


    # # GDP info
    # econ = pd.read_csv("Data/econ_state.csv", sep=",")
    # inc_srs = {"average": [176791615.7,
    # 39290291.13,
    # 249448704.6,
    # 108831696.7,
    # 1938410568,
    # 253766415.6,
    # 238263079.4,
    # 42112554.09,
    # 45290541.96,
    # 838566684.3,
    # 386351603,
    # 64817569.43,
    # 58951608.43,
    # 612544084.4,
    # 263205209.1,
    # 135754424.6,
    # 132372574.5,
    # 161425112.3,
    # 189804889.8,
    # 54469133.3,
    # 321742870.5,
    # 397760589.2,
    # 399937811.3,
    # 262641717.3,
    # 100691665.5,
    # 246204419.9,
    # 40949236.22,
    # 88230701.7,
    # 113101411.6,
    # 70531186,
    # 508790770.2,
    # 75523208.17,
    # 1094531210,
    # 385892535.2,
    # 39901185.96,
    # 481395422.6,
    # 165899137.9,
    # 162150640.8,
    # 604257968.4,
    # 50096894.61,
    # 174639436.4,
    # 38847129.74,
    # 260516938.4,
    # 1188915979,
    # 108187560.7,
    # 29093390.22,
    # 414091212,
    # 344361453.3,
    # 65545407.52,
    # 251480529.2,
    # 31149428.13
    # ]}
    # avg_inc = pd.DataFrame(inc_srs, index = ["AL", "AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS",
    # "KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY",'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX',
    # 'UT','VT','VA','WA','WV','WI','WY'])
        
    # gdp_state = {"average": [191991.9565,57137.13043,275708.7391,114656.913,2286225.043,292420.3478,244541.7391,64137.43478,
    # 115288.087,819574.4783,466072.6957,75951.78261,61720.52174,736587.7826,316920.2174,164064.2609,144765.6522,183692.2609,
    # 238869.5217,54654.56522,346141.8261,453538.0435,439186.3913,307783.6957,103050.2174,279151.7391,43625.30435,107732,132169.5217,70188,537377.8261,91781.30435,1354936.609,
    # 464976.1304,52697,576236.1739,180599.2174,206497.6957,669048.3913,53191.08696,186908.9565,44893.73913,293867.3478,1529511.913,137171.6522,
    # 29050.52174,457398.0435,414854.0435,72502.21739,285275.9565,40416.95652]}
    # avg_gdp = pd.DataFrame(gdp_state, index = ["AL", "AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS",
    # "KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY",'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX',
    # 'UT','VT','VA','WA','WV','WI','WY'])
        
    ur = {"average_unemployment": [6.916666667,
    7.241666667, 6.344444444,7.191666667,8.302777778,5.804166667,7.006944444,8.048611111,6.047222222,6.945833333,7.580555556,4.768055556,
    4.490277778,5.723611111,7.733333333,6.669444444,5.045833333,7.023611111,6.656944444,5.761111111,5.95,5.955555556,7.561111111,
    4.780555556,6.251388889,7.830555556,5.197222222,7.358333333,3.009722222,3.609722222,4.395833333,7.376388889,6.880555556,8.997222222,
    6.797222222,6.509722222,4.998611111,7.218055556,6.541666667,8.247222222,7.3625,3.669444444,6.859722222,5.772222222,4.548611111,
    5.276388889,4.254166667,6.891666667,5.904166667,6.913888889,4.902777778]}
    avg_ur = pd.DataFrame(ur, index = ["AL", "AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS",
    "KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY",'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX',
    'UT','VT','VA','WA','WV','WI','WY'])
        
    df_econ = avg_gdp.join(avg_inc, lsuffix='_gdp', rsuffix='_income')
    df_econ['state']= ["AL", "AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS",
    "KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY",'NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX',
    'UT','VT','VA','WA','WV','WI','WY']

    df_econ_2 = df_econ.join(avg_ur)

    listings = pd.merge(listings,df_econ_2.iloc[:,:],how="inner",left_on='state',right_on="state")

    listings = listings.drop(['weekly_price', 'amenities', 'bed_type', 'has_availability', 'host_id', 'id', 'latitude', 'longitude', 'name', 'state', 'zipcode'], 1)

    with pd.option_context('mode.use_inf_as_null', True):
       listings = listings.dropna()

    x = listings.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    listings = pd.DataFrame(x_scaled)

    return listings
