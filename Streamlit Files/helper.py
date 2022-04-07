import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Q7
import Q8

#Reading all 4 csv files neccesary for this project:
df_oa=pd.read_csv("Players_Medal_list_Olympics.csv") #Olympic athlete data
df_om=pd.read_csv("Medal_List_Olympics.csv") #Olympic medal data
df_aa=pd.read_csv("Players_Medal_List_Asian.csv") #Asian athlete data
df_am=pd.read_csv("Medal_List_Asian.csv") #Asian medal data

#---------Q1---------

## This is the block of code in which i am calculating the number of medals won by the asian counties in both "Asian" and 
##"Olympic" games.
##This is the helper funtion that will take the inputs as game : which game to analyze, country: which country to provide the
##analysis for and year: which year to consider for analysis.

def Helper1(game,game_df,country,year): 

    if(game == "Asian Games"):
       

        ##Earlier china was know as "Republic of china" and sri lanka was known as "Ceylon", hence changing their names as per the new 
        ##conventions.

        game_df.replace("Republic of China","China",inplace=True)
        game_df.replace("Ceylon","Sri Lanka",inplace=True)
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
    
    elif(game == "Olympic Games"):
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
     
    li3=[]
    df = game_df[game_df["Year"] == year]  ##Filtering the dataframe according to the input given by the user.
    countries = df["Country"].unique().tolist()  ##Collecting the names of the countries in a list.
    for nation in countries:  ##For every country i am calculating the sum of gold,silver,bronze seperately and also sum of all medals.
        df_c = df[df["Country"] == nation]
        li3.append((nation,year,df_c["Gold"].sum(),df_c["Silver"].sum(),df_c["Bronze"].sum(),df_c["Total"].sum()))
    li3.sort(key=lambda x : x[2],reverse=True)  ##Reverse sorting the list with respect to the number of gold medals won.
    ans3_df = pd.DataFrame(li3,columns=["Country","Year","Gold","Silver","Bronze","Total"])

    
    li4=[]
    countries = game_df["Country"].unique().tolist()
    for nation in countries:  ##Doing same as above, but here i am considering all years and calculating the number of medals won by a country in total.
        df_c = game_df[game_df["Country"] == nation]
        li4.append((nation,df_c["Gold"].sum(),df_c["Silver"].sum(),df_c["Bronze"].sum(),df_c["Total"].sum()))
    li4.sort(key=lambda x : x[1],reverse=True)  ##Reverse sorting the list with respect to the number of gold medals won.
    ans4_df = pd.DataFrame(li4,columns=["Country","Gold","Silver","Bronze","Total"])
    
    
    li5=[]
    years = game_df["Year"].unique()
    df_c = game_df[game_df["Country"] == country]
    for y in years:   ##Here for each country i am calculating the number of medals won year wise.
        df_y = df_c[df_c["Year"] == y]
        li5.append((country,y,df_y["Gold"].sum(),df_y["Silver"].sum(),df_y["Bronze"].sum(),df_y["Total"].sum()))
    li5.sort(key=lambda x : x[1],reverse=False)   ##Sorting the list with year.
    ans5_df = pd.DataFrame(li5,columns=["Country","Year","Gold","Silver","Bronze","Total"])
    

   
    if(year == "All years"):
        ##Plotting the bar graph and returning the dataframe if the user inputs year as "All years"
        fig = plt.figure(figsize = (15, 5))
        sns.barplot(ans5_df["Year"],ans5_df["Total"])
        plt.xticks(rotation = 45)
        plt.title("No Of Medals Won By "+country+" Year Wise in "+game,fontsize = 20)
        plt.xlabel("Year",fontsize=15)
        plt.ylabel("Total Medals",fontsize=15)
        for i in range(len(ans5_df["Year"].values)):  ##Adding labels to bars in bar graph.
            plt.text(i,ans5_df["Total"].values[i],ans5_df["Total"].values[i],ha='center')
        return (ans5_df,plt)
    
    elif(country == "Overall" and year != "Overall"):
    ##Plotting the bar graph and returning the dataframe if the user inputs year and wants the analysis for all the countries
        fig = plt.figure(figsize = (15, 5))
        sns.barplot(ans3_df["Country"],ans3_df["Total"])
        plt.xticks(rotation = 90)
        plt.title("No Of Medals Won By Each Country in "+str(year),fontsize = 20)
        plt.xlabel("Countries",fontsize=15)
        plt.ylabel("Total Medals",fontsize=15)
        for i in range(len(ans3_df["Country"].values)):  ##Adding labels to bars in bar graph.
            plt.text(i,ans3_df["Total"].values[i],ans3_df["Total"].values[i],ha='center')
        return (ans3_df,plt)
    
    elif(country == "Overall" and year == "Overall"):
    ##Plotting the bar graph and returning the dataframe if the user inputs year as overall and wants the analysis for all the countries
        fig = plt.figure(figsize = (15, 5))
        sns.barplot(ans4_df["Country"],ans4_df["Total"])
        plt.xticks(rotation = 90)
        plt.title("No Of Medals Won By Each Country in "+game,fontsize = 20)
        plt.xlabel("Countries",fontsize=15)
        plt.ylabel("Total Medals",fontsize=15)
        for i in range(len(ans4_df["Country"].values)):  ##Adding labels to bars in bar graph.
            plt.text(i,ans4_df["Total"].values[i],ans4_df["Total"].values[i],ha='center')
        return (ans4_df,plt)
    
    elif(country != "Overall" and year == "Overall"):
    ##Returning the total number of medals won by a country(user input).
        return ans4_df[ans4_df["Country"] == country]
    
    elif(country != "Overall" and year != "Overall"):
    ##Returning the total number of medals won by a country(user input) in a particular year(user input).
        return ans3_df[ans3_df["Country"] == country]
    
    
def Medal_Tally(game,country,year):  ##This is the main function that will be called as soon as the user inputs something.
    
    if(game == "Asian Games"):  ##If the user wants the analysis for asian games then we call the helper function by proving it with asian games dataset.
        return Helper1(game,df_am.copy(),country,year)
    elif(game == "Olympic Games"):  ##If the user wants the analysis for olympic games then we call the helper function by proving it with olympic games dataset.
        return Helper1(game,df_om.copy(),country,year)
    elif(game == "Both"):  ##In this case the helper function will be called twice first for asian games and then for olympic games.
        return (Helper1("Asian Games",df_am.copy(),country,year),Helper1("Olympic Games",df_om.copy(),country,year))

#---------Q2---------
def Helper2(game,game_df,country,year):

    if(game == "Asian Games"):
           

        ##Earlier china was know as "Republic of china" and sri lanka was known as "Ceylon", hence changing their names as per the new 
        ##conventions.

        game_df.replace("Republic of China","China",inplace=True)
        game_df.replace("Ceylon","Sri Lanka",inplace=True)
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
    
    elif(game == "Olympic Games"):
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
    
    li3=[]
    df_y = game_df[game_df["Year"] == year]  ##Filtering the dataframe according to the year passed by the user.
    countries = df_y["Country"].unique().tolist()
    for nation in countries:   ##For every country i am calculating the percentage of gold,silver,bronze seperately and also percentage of total medals won.
        df_c = df_y[df_y["Country"] == nation]
        li3.append((nation,year,float(format((df_c["Gold"].sum()/df_y["Gold"].sum())*100,'0.2f')),float(format((df_c["Silver"].sum()/df_y["Silver"].sum())*100,'0.2f')),float(format((df_c["Bronze"].sum()/df_y["Bronze"].sum())*100,'0.2f')),float(format((df_c["Total"].sum()/df_y["Total"].sum())*100,'0.2f'))))
        li3.sort(key = lambda x : x[2],reverse=True)
    ans3_df = pd.DataFrame(li3,columns=["Country","Year","% Gold","% Silver","% Bronze","% Total"])
    
    ##Here i am considering all the years.
    li4=[]
    countries = game_df["Country"].unique().tolist()
    for nation in countries:  ##For every country i am calculating the percentage of gold,silver,bronze seperately and also percentage of total medals won.
        df_c = game_df[game_df["Country"] == nation]
        li4.append((nation,float(format((df_c["Gold"].sum()/game_df["Gold"].sum())*100,'0.2f')),float(format((df_c["Silver"].sum()/game_df["Silver"].sum())*100,'0.2f')),float(format((df_c["Bronze"].sum()/game_df["Bronze"].sum())*100,'0.2f')),float(format((df_c["Total"].sum()/game_df["Total"].sum())*100,'0.2f'))))
        li4.sort(key = lambda x : x[1],reverse=True)
    ans4_df = pd.DataFrame(li4,columns=["Country","% Gold","% Silver","% Bronze","% Total"])
    


    if(country == "Overall" and year == "Overall"):
    ##Plotting the graph and returning the dataframe if the user has asked the analysis for all the countries.
    
        b=[]
        for i in ans4_df["% Total"].values[:5]:
            b.append(i)
        b.append(ans4_df["% Total"].values[5:].sum())
        labels=[]
        for l in ans4_df["Country"].values[:5]:
            labels.append(l)
        labels.append("Others")
        plt.pie(b,labels=labels,autopct='%0.2f%%',radius=1.5)
        plt.title("Percentage Of Medals Won By Countries in "+str(game),pad=60)
        return (ans4_df,plt)
    
    elif(country == "Overall" and year != "Overall"):
    ##Plotting the graph and returning the dataframe if the user has asked the analysis for all the countries and a particular year.


        b=[]
        for i in ans3_df["% Total"].values[:5]:
            b.append(i)
        b.append(ans3_df["% Total"].values[5:].sum())
        labels=[]
        for l in ans3_df["Country"].values[:5]:
            labels.append(l)
        labels.append("Others")
        plt.pie(b,labels=labels,autopct='%0.2f%%',radius=1.5)
        plt.title("Percentage Of Medals Won By Countries in "+str(game)+" "+str(year),pad=60)
        return (ans3_df,plt)
    
    elif(country != "Overall" and year == "Overall"):
    ##returning the dataframe if the user has asked the analysis for a particular country and all years.
        return ans4_df[ans4_df["Country"] == country]
    
    elif(country != "Overall" and year != "Overall"):
    ##returning the dataframe if the user has asked the analysis for a particular country and a particular year.
        return ans3_df[ans3_df["Country"] == country]
    
def Medal_percentage(game,country,year):  ##This is the main function that will be called as soon as the user inputs something.
    
    if(game == "Asian Games"):  ##If the user wants the analysis for asian games then we call the helper function by proving it with asian games dataset.
        return Helper2(game,df_am.copy(),country,year)
    elif(game == "Olympic Games"):  ##If the user wants the analysis for olympic games then we call the helper function by proving it with olympic games dataset.
        return Helper2(game,df_om.copy(),country,year)
    else:  ##In this case the helper function will be called twice first for asian games and then for olympic games.
        return (Helper2("Asian Games",df_am.copy(),country,year),Helper2("Olympic Games",df_om.copy(),country,year))

#---------Q3---------

def Helper3(game,game_df,country,year):

    if(game == "Asian Games"):
           

        ##Earlier china was know as "Republic of china" and sri lanka was known as "Ceylon", hence changing their names as per the new 
        ##conventions.

        game_df.replace("Republic of China","China",inplace=True)
        game_df.replace("Ceylon","Sri Lanka",inplace=True)
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
    
    elif(game == "Olympic Games"):
        game_df.replace("Field hockey","Hockey",inplace=True)
        game_df = game_df.astype({"Year":'string'})
    
    if(year != "Overall"):  ##If user asks the analysis for a particular year.
        li3=[]
        df = game_df[game_df["Year"] == year]  ##Filtering the dataframe according to a particular year.
        countries = df["Country"].unique().tolist()
        ans3_df = pd.DataFrame()
        for nation in countries:  ##For every country i am calculating the total number of medals won sports wise.
            df_c = df[(df["Country"] == nation)]
            ans3_df = pd.concat([ans3_df,df_c[["Country","Sport","Year","Gold","Silver","Bronze","Total"]]])
        ans3_df.sort_values(["Country","Sport"],ascending=[True,True],inplace=True)
        ans3_df.reset_index(drop=True,inplace=True)
        
    
    ##Here i am calculating the total number of medals for all countries considering all years.
    li4=[]
    countries = game_df["Country"].unique().tolist()
    games = game_df["Sport"].unique().tolist()
    for nation in countries:
        for sport in games:
            df_c = game_df[(game_df["Sport"] == sport) & (game_df["Country"] == nation)]
            if(df_c.empty):
                continue
            li4.append((nation,sport,df_c["Gold"].sum(),df_c["Silver"].sum(),df_c["Bronze"].sum(),df_c["Total"].sum()))
    ans4_df = pd.DataFrame(li4,columns=["Country","Sport","Gold","Silver","Bronze","Total"])
    ans4_df.sort_values(["Country","Sport"],ascending=[True,True],inplace=True)
    ans4_df.reset_index(drop=True,inplace=True)
    
    
    
    if(country == "Overall" and year == "Overall"):
    ##returning the dataframe if user asks the analysis for all countries and all years.
        return ans4_df
    
    elif(country == "Overall" and year != "Overall"):
    ##returning the dataframe if user asks the analysis for all countries and a particular year.
        return ans3_df
    
    elif(country != "Overall" and year == "Overall"):
    ##plotting the graph and returning the dataframe if user asks the analysis for a particular country and all years.
        df =  ans4_df[ans4_df["Country"] == country]
        fig = plt.figure(figsize = (15, 5))
        sns.barplot(df["Sport"],df["Total"],ci=None,dodge=False)
        plt.xticks(rotation = 90)
        plt.title("No Of Medals Won By "+country+" Sports Wise in "+game,fontsize = 20)
        plt.xlabel("Sports",fontsize=15)
        plt.ylabel("Total Medals",fontsize=15)
        for i in range(len(df["Sport"].values)):  ##Adding labels to bars in bar graph.
            plt.text(i,df["Total"].values[i],df["Total"].values[i],ha='center')
        return (df,plt)
    
    elif(country != "Overall" and year != "Overall"):
    ##plotting the graph and returning the dataframe if user asks the analysis for a particular country and a particular year.
        df =  ans3_df[ans3_df["Country"] == country]
        fig = plt.figure(figsize = (15, 5))
        sns.barplot(df["Sport"],df["Total"],ci=None,dodge=False)
        plt.xticks(rotation = 90)
        plt.title("No Of Medals Won By "+country+" in "+str(year)+" Sport Wise",fontsize = 20)
        plt.xlabel("Sports",fontsize=15)
        plt.ylabel("Total Medals",fontsize=15)
        for i in range(len(df["Sport"].values)):  ##Adding labels to bars in bar graph.
            plt.text(i,df["Total"].values[i],df["Total"].values[i],ha='center')
        return (df,plt)
    
    
def Medal_sport_wise(game,country,year):  ##This is the main function that will be called as soon as the user inputs something.
    
    if(game == "Asian Games"):  ##If the user wants the analysis for asian games then we call the helper function by proving it with asian
        return Helper3(game,df_am.copy(),country,year)
    elif(game == "Olympic Games"):  ##If the user wants the analysis for olympic games then we call the helper function by proving it with olympic games dataset.
        return Helper3(game,df_om.copy(),country,year)
    elif(game == "Both"):  ##In this case the helper function will be called twice first for asian games and then for olympic games.
        return (Helper3("Asian Games",df_am.copy(),country,year),Helper3("Olympic Games",df_om.copy(),country,year))
#---------Q4---------
def Host_analysis(game):
    df_o2=df_om.copy()
    df_a2=df_am.copy()
    #We'll use it to generate host country by inputting year value later:
    #Since there is no clash in years of Olympic games and Asian games, we can include all in a single dictionary.
    dict={"1951":"India","1952":"Finland","1954":"Philippines","1956":"Australia","1958":"Japan","1960":"Italy","1962":"Indonesia",
  "1964":"Japan","1966":"Thailand","1968":"Mexico", "1970":"Thailand","1972":"Germany","1974":"Iran","1976":"Canada",
  "1978":"Thailand","1980":"Russia","1982":"India","1984":"USA","1986":"South Korea","1988":"South Korea","1990":"China",
  "1992":"Spain","1994":"Japan","1996":"USA","1998":"Thailand","2000":"Australia","2002":"South Korea","2004":"Greece",
  "2006":"Qatar","2008":"China", "2010":"China","2012":"UK","2014":"South Korea","2016":"Brazil","2018":"Indonesia",
  "2020":"Japan"}
    df_o2['Host_Country']=df_o2['Year'].astype(str)
    for i in range(len(df_o2)):
        df_o2['Host_Country'].loc[i]=dict[df_o2['Host_Country'].loc[i]]
    df_a2['Host_Country']=df_a2['Year'].astype(str)
    for i in range(len(df_a2)):
        df_a2['Host_Country'].loc[i]=dict[df_a2['Host_Country'].loc[i]]
    if(game == "Asian Games"):
        host=df_a2[df_a2['Country']==df_a2['Host_Country']].reset_index(drop=True)
        non_host=df_a2[df_a2['Country']!=df_a2['Host_Country']].reset_index(drop=True)
        host=host.groupby(['Year','Country'])['Gold','Silver','Bronze','Total'].agg(sum).reset_index()
        host=host.groupby(['Country'])['Gold','Silver','Bronze','Total'].mean().reset_index()
        host=host.rename(columns={'Gold':'Gold/Yr','Silver':'Silver/Yr','Bronze':'Bronze/Yr','Total':'Total/Yr'})
        non_host=non_host.groupby(['Year','Country'])['Gold','Silver','Bronze','Total'].agg(sum).reset_index()
        non_host=non_host.groupby(['Country'])['Gold','Silver','Bronze','Total'].mean().reset_index()
        non_host=non_host.rename(columns={'Gold':'Gold/Yr','Silver':'Silver/Yr','Bronze':'Bronze/Yr','Total':'Total/Yr'})
        non_host=non_host.sort_values(["Gold/Yr","Silver/Yr","Bronze/Yr"],ascending=False).reset_index(drop=True)
        #Creating a list that will only have the 9 host nations of Asian games.
        li=[]
        for item in host['Country']:
            li.append(item)
        #If any country in non_host doesn't belongs in the above list, then remove it out as it's of no use.
        for i in range(len(non_host)):
            if non_host['Country'].loc[i] not in li:
                non_host['Country'].loc[i]='Not_host'
        non_host=non_host[non_host['Country']!='Not_host'].reset_index(drop=True)
        non_host=non_host.sort_values(['Country']).reset_index(drop=True)
        host=host.sort_values(['Country']).reset_index(drop=True)
        return host,non_host


    elif(game == "Olympic Games"):
        #Splitting data into 2 dataframes:
        host=df_o2[df_o2['Country']==df_o2['Host_Country']].reset_index(drop=True) #Contains countries performance when they are host
        non_host=df_o2[df_o2['Country']!=df_o2['Host_Country']].reset_index(drop=True) #Contains countries performance when they are not host
        #Overall analysis for all years combined:
        host=host.groupby(['Year','Country'])['Gold','Silver','Bronze','Total'].agg(sum).reset_index()
        host=host.groupby(['Country'])['Gold','Silver','Bronze','Total'].mean().reset_index()
        #If a country has hosted for 2 years. Eg. Japan. Then, we'll aggreate it's medal tally by calculating their mean.
        #Means if a country wins 6 golds in 2 years as host, then upon aggregating, that country wins 3 gold medals/year.
        host=host.rename(columns={'Gold':'Gold/Yr','Silver':'Silver/Yr','Bronze':'Bronze/Yr','Total':'Total/Yr'})
        #Repeating same for non host countries:
        non_host=non_host.groupby(['Year','Country'])['Gold','Silver','Bronze','Total'].agg(sum).reset_index()
        non_host=non_host.groupby(['Country'])['Gold','Silver','Bronze','Total'].mean().reset_index()
        non_host=non_host.rename(columns={'Gold':'Gold/Yr','Silver':'Silver/Yr','Bronze':'Bronze/Yr','Total':'Total/Yr'})
        non_host=non_host.sort_values(["Gold/Yr","Silver/Yr","Bronze/Yr"],ascending=False).reset_index(drop=True)
        #Filtering data for only those Asian countries that have hosted Olympic games(China, Japan and South Korea):
        non_host=non_host[:3]
        return host,non_host
    else:
        print(3)
#---------Q5---------
def Athlete_countrywise(game,country,year):
    if year!='Overall':
        year=int(year)
    if game=="Asian Games":
        df1=df_aa.copy()
        df1['Total']=df1['Gold']+df1['Silver']+df1['Bronze']
        if country!='Overall':
            if year!='Overall':
                df1=df1[df1["Country"]==country]
                df1=df1[df1['Year']==year].reset_index(drop=True)
                df1=df1.groupby(['Player_Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
            else:
                df1=df1[df1["Country"]==country]
                df1=df1.groupby(['Player_Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
        else:
            if year!='Overall':
                df1=df1[df1['Year']==year]
                df1=df1.groupby(['Player_Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]   
            else:
                df1=df1.groupby(['Player_Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
    elif game=="Olympic Games":
        df1=df_oa.copy()
        df1['Total']=df1['Gold']+df1['Silver']+df1['Bronze']
        if country!='Overall':
            if year!='Overall':
                df1=df1[df1["Country"]==country]
                df1=df1[df1['Year']==year].reset_index(drop=True)
                df1=df1.groupby(['Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
            else:
                df1=df1[df1["Country"]==country]
                df1=df1.groupby(['Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
        else:
            if year!='Overall':
                df1=df1[df1['Year']==year]
                df1=df1.groupby(['Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]   
            else:
                df1=df1.groupby(['Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
    return df1
#---------Q6---------
def Athlete_sportwise(game,sports,country,year):
    if year!='Overall':
        year=int(year)
    if game=="Asian Games":
        df1=df_aa.copy()
        df1['Total']=df1['Gold']+df1['Silver']+df1['Bronze']
        if country!='Overall':
            if year!='Overall':
                df1=df1[df1['Sport']==sports]
                df1=df1[df1["Country"]==country]
                df1=df1[df1['Year']==year].reset_index(drop=True)
                df1=df1.groupby(['Player_Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
            else:
                df1=df1[df1['Sport']==sports]
                df1=df1[df1["Country"]==country]
                df1=df1.groupby(['Player_Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
        else:
            if year!='Overall':
                df1=df1[df1['Sport']==sports]
                df1=df1[df1['Year']==year]
                df1=df1.groupby(['Player_Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]   
            else:
                df1=df1[df1['Sport']==sports]
                df1=df1.groupby(['Player_Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
    elif game=="Olympic Games":
        df1=df_oa.copy()
        df1['Total']=df1['Gold']+df1['Silver']+df1['Bronze']
        if country!='Overall':
            if year!='Overall':
                df1=df1[df1['Sport']==sports]
                df1=df1[df1["Country"]==country]
                df1=df1[df1['Year']==year].reset_index(drop=True)
                df1=df1.groupby(['Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
            else:
                df1=df1[df1['Sport']==sports]
                df1=df1[df1["Country"]==country]
                df1=df1.groupby(['Name'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
        else:
            if year!='Overall':
                df1=df1[df1['Sport']==sports]
                df1=df1[df1['Year']==year]
                df1=df1.groupby(['Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]   
            else:
                df1=df1[df1['Sport']==sports]
                df1=df1.groupby(['Name','Gender','Country'])['Gold','Silver','Bronze','Total'].sum().reset_index()
                df1=df1.sort_values(['Gold','Silver','Bronze'], ascending=False)
                df1=df1.reset_index(drop=True)
                df1=df1[:5]
    return df1
#---------Q7---------
def Q7a():
	event_F = Q7.get_events(df_aa, "F")
	event_M = Q7.get_events(df_aa, "M")
	
	x_axis_A = pd.unique(df_aa["Year"])
	y_axis_f_A = [len(event_F[event_F["Year"] == y]) for y in x_axis_A]
	y_axis_m_A = [len(event_M[event_M["Year"] == y]) for y in x_axis_A]
	xlabel = "Years"
	ylabel = "No of events"
	title = "No of events of male and female over the years in Asian Games"
	
	fig1, ax1 = Q7.plotLine(x_axis_A, [y_axis_m_A, y_axis_f_A], ["Male", "Female"], xlabel, ylabel, title)
	
	events = df_oa.groupby(["Event", "Gender", "Country", "Year", "Sport", "Sport_Type", "Gold", "Silver", "Bronze"], as_index = False).agg("sum")
	events_m = events[events["Gender"] == "M"]
	events_f = events[events["Gender"] == "F"]
	
	x_axis_O = pd.unique(df_oa["Year"])
	y_axis_f_O = [len(events_f[events_f["Year"] == y]) for y in x_axis_O]
	y_axis_m_O = [len(events_m[events_m["Year"] == y]) for y in x_axis_O]
	
	xlabel = "Years"
	ylabel = "No of events"
	title = "No of Medals won by male and female over the years in Olympics"
	fig2, ax2 = Q7.plotLine(x_axis_O, [y_axis_m_O, y_axis_f_O], ["Male", "Female"], xlabel, ylabel, title)
	
	return fig1, fig2

def Q7b(df_p, game, year, sport, medal):
    events, fig = Q7.m_f_winning_ratio_countrywise(df_p, game, year, sport, medal)
    return events, fig

def Q7c(df_p, game, nation, sport, medal):
	events, fig = Q7.m_f_winning_ratio_yearwise(df_p, game, nation, sport, medal)
	return events, fig

#---------Q8---------

def Q8a(df_p, game, year, medal):
	events, fig = Q8.indi_team_table(df_p, game, year, medal)
	return events, fig
#---------Q9---------
#---------Q10---------
#---------Q11---------
def SuccessiveYearComparison():
    asian = pd.read_csv(
        "Players_Medal_List_Asian.csv"
    )  # Asian Players and Medals dataset
    olympic = pd.read_csv(
        "Players_Medal_list_Olympics.csv"
    )  # Olympic Players and Medal dataset

    asian_years = asian["Year"].unique()  # List contain asian game years
    olympic_years = olympic["Year"].unique()  # List contain olympic game yers

    df = pd.DataFrame(
        columns=[
            "Country",
            "Player",
            "Gender",
            "Year_Asian",
            "Year_Olympic",
            "Sport",
            "Gold_Olympic",
            "Gold_Asian",
            "Silver_Olympic",
            "Silver_Asian",
            "Bronze_Olympic",
            "Bronze_Asian",
        ]
    )  # This is how our resulting dataframe looks like

    for yasian, yolympic in zip(
        asian_years, olympic_years
    ):  # looping through pairs of year [asian year,next olympic year]
        asian_df1 = asian[(asian["Year"] == yasian)]
        olympic_df1 = olympic[(olympic["Year"] == yolympic)]

        asian_df1 = asian_df1[asian_df1["Sport_Type"] == "Single"]
        asian_df1.drop(columns=["Sport_Type", "Event"], inplace=True)

        asian_df1 = (
            asian_df1.groupby(by=["Year", "Country", "Gender", "Sport", "Player_Name"])
            .sum()
            .reset_index()
        )

        olympic_df1 = olympic_df1[olympic_df1["Sport_Type"] == "Individual"]
        olympic_df1.drop(columns=["Sport_Type", "Host_City", "Event"], inplace=True)

        olympic_df1 = (
            olympic_df1.groupby(by=["Year", "Country", "Gender", "Sport", "Name"])
            .sum()
            .reset_index()
        )

        result = olympic_df1.merge(
            asian_df1,
            left_on="Name",
            right_on="Player_Name",
            suffixes=("_Olympic", "_Asian"),
        )

        for x in result.values:
            df.loc[len(df.index)] = [
                x[1],
                x[4],
                x[2],
                x[8],
                x[0],
                x[11],
                x[5],
                x[13],
                x[6],
                x[14],
                x[7],
                x[15],
            ]

    return df
#---------Q12---------
#---------Q13---------
def olympicTotalVariation(olympic_medal):
    olympic_total_variation=olympic_medal[olympic_medal["Country"]=="India"][["Year","Gold","Silver","Bronze","Total"]]
    olympic_total_variation=olympic_total_variation.groupby(["Year"]).sum().reset_index()

    fig,ax=plt.subplots(figsize=(15,7))

    labels=olympic_total_variation["Year"].values
    y=olympic_total_variation["Total"].values
    x=np.arange(len(labels))

    ax.bar(x,y,width=0.65)

    ax.set_title("Variation of Total medals in Olympic Games over the years",fontdict={'fontsize':20})
    ax.set_xlabel("Year",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    for i,val in enumerate(y):
        ax.text(i-0.1,val+0.1,str(val))

    fig.tight_layout()
    return fig

def olympicGoldVariation(olympic_medal):
    olympic_total_variation=olympic_medal[olympic_medal["Country"]=="India"][["Year","Gold","Silver","Bronze","Total"]]
    olympic_total_variation=olympic_total_variation.groupby(["Year"]).sum().reset_index()

    fig,ax=plt.subplots(figsize=(15,7))

    labels=olympic_total_variation["Year"].values

    gold=olympic_total_variation["Gold"].values
    silver=olympic_total_variation["Silver"].values
    bronze=olympic_total_variation["Bronze"].values
    width=0.2

    x=np.arange(len(labels))

    rects1=ax.bar(x-0.2,gold,width=width,label='Gold',color='yellow')
    rects2=ax.bar(x,silver,width=width,label='Silver',color='gray')
    rects3=ax.bar(x+0.2,bronze,width=width,label='Bronze',color='orange')

    ax.set_title("Variation of (Gold,Silver,Bronze) medals in Olympic Games over the years",fontdict={'fontsize':15})
    ax.set_xlabel("Year",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    return(fig)

def olympicSportVariation(olympic_medal):
    olympics_sport_total=olympic_medal[olympic_medal["Country"]=="India"][["Sport","Gold","Silver","Bronze","Total"]]
    olympics_sport_total=olympics_sport_total.groupby("Sport").sum().reset_index()

    temp=olympics_sport_total[["Sport","Total"]]
    temp=temp.sort_values("Total",ascending=False)

    fig,ax=plt.subplots(figsize=(15,7))

    labels=temp["Sport"].values
    y=temp["Total"].values
    x=np.arange(len(labels))

    ax.bar(x,y,width=0.45)
    ax.set_title("Variation of Total medals in Olympic Games across sports",fontdict={'fontsize':20})
    ax.set_xlabel("Sports",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels,rotation=90)

    for i,val in enumerate(y):
        ax.text(i-0.1,val+0.1,str(val))

    fig.tight_layout()
    
    return fig

def asianTotalVariation(asian_medal):
    asian_total_variation=asian_medal[asian_medal["Country"]=="India"][["Year","Gold","Silver","Bronze","Total"]]
    asian_total_variation=asian_total_variation.groupby(["Year"]).sum().reset_index()

    fig,ax=plt.subplots(figsize=(15,7))

    labels=asian_total_variation["Year"].values
    y=asian_total_variation["Total"].values
    x=np.arange(len(labels))

    ax.bar(x,y,width=0.75)

    ax.set_title("Variation of Total medals in Asian Games over the years",fontdict={'fontsize':20})
    ax.set_xlabel("Year",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    for i,val in enumerate(y):
        ax.text(i-0.2,val+1,str(val))

    fig.tight_layout()
    return(fig)

def asianGoldVariation(asian_medal):
    asian_total_variation=asian_medal[asian_medal["Country"]=="India"][["Year","Gold","Silver","Bronze","Total"]]
    asian_total_variation=asian_total_variation.groupby(["Year"]).sum().reset_index()
    fig,ax=plt.subplots(figsize=(15,7))

    labels=asian_total_variation["Year"].values

    gold=asian_total_variation["Gold"].values
    silver=asian_total_variation["Silver"].values
    bronze=asian_total_variation["Bronze"].values
    width=0.2

    x=np.arange(len(labels))

    rects1=ax.bar(x-0.2,gold,width=width,label='Gold',color='yellow')
    rects2=ax.bar(x,silver,width=width,label='Silver',color='gray')
    rects3=ax.bar(x+0.2,bronze,width=width,label='Bronze',color='orange')

    ax.set_title("Variation of (Gold,Silver,Bronze) medals in Asian Games over the years",fontdict={'fontsize':20})
    ax.set_xlabel("Year",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    return fig

def asianSportVariation(asian_medal):
    asian_sport_total=asian_medal[asian_medal["Country"]=="India"][["Sport","Gold","Silver","Bronze","Total"]]
    asian_sport_total=asian_sport_total.groupby("Sport").sum().reset_index()

    temp=asian_sport_total[["Sport","Total"]]
    temp=temp.sort_values("Total",ascending=False)

    fig,ax=plt.subplots(figsize=(15,7))

    labels=temp["Sport"].values
    y=temp["Total"].values
    x=np.arange(len(labels))

    ax.bar(x,y,width=0.65)
    ax.set_title("Variation of Total medals in Asian Games across sports",fontdict={'fontsize':20})
    ax.set_xlabel("Sports",fontdict={'fontsize':15})
    ax.set_ylabel("Medal Count",fontdict={'fontsize':15})
    ax.set_xticks(x)
    ax.set_xticklabels(labels,rotation=90)

    for i,val in enumerate(y):
        ax.text(i-0.2,val+1,str(val))

    fig.tight_layout()
    return fig
#---------Q14---------
#---------Q15---------
def find_percentage(df):
    years = df.Year.unique()
    result = pd.DataFrame(columns = ['Year','Country','Total_Sports','Sports_Won','Sports_Lost','Percentage_Won','Percentage_Lost'])
    for year in years:
        df1 = df[df['Year']==year]
        total_sports = len(df1.Sport.unique())
        countries = df1.Country.unique()
        for country in countries:
            sports_won = len(df1[df1['Country']==country]['Sport'].unique())
            sports_lost = total_sports - sports_won
            percentage_won = (sports_won/total_sports)*100
            percentage_lost = (sports_lost/total_sports)*100
            result.loc[len(result)] = [year, country, total_sports, sports_won, sports_lost, percentage_won, percentage_lost]
    result.sort_values(['Year','Percentage_Won'],ascending=[True,False], inplace=True)
    return result

def Atleast_one(game):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        out=find_percentage(df_Asian)
        return out
    elif game=="Olympic Games":
        out=find_percentage(df_Olympics)
        return out
    elif game=="Both":
        out1=find_percentage(df_Asian)
        out2=find_percentage(df_Olympics)
        return (out1,out2)

def find_max_percentage_country(df):
    years = df.Year.unique()
    result = pd.DataFrame(columns = ['Year','Country','Total_Sports','Sports_Won','Sports_Lost','Percentage_Won','Percentage_Lost'])
    for year in years:
        df1 = df[df['Year']==year]
        total_sports = len(df1.Sport.unique())
        countries = df1.Country.unique()
        for country in countries:
            sports_won = len(df1[df1['Country']==country]['Sport'].unique())
            sports_lost = total_sports - sports_won
            percentage_won = (sports_won/total_sports)*100
            percentage_lost = (sports_lost/total_sports)*100
            result.loc[len(result)] = [year, country, total_sports, sports_won, sports_lost, percentage_won, percentage_lost]
    result.sort_values(['Year','Percentage_Won'],ascending=[True,False], inplace=True)
    idx = result.groupby(['Year'])['Percentage_Won'].transform(max) == result['Percentage_Won']
    return result.loc[idx]

def Atleast_one_country(game):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        out=find_max_percentage_country(df_Asian)
        return out
    elif game=="Olympic Games":
        out=find_max_percentage_country(df_Olympics)
        return out
    elif game=="Both":
        out1=find_max_percentage_country(df_Asian)
        out2=find_max_percentage_country(df_Olympics)
        return (out1,out2)
#---------Q16---------
def recession(x):
    rec_years= []
    temp = []
    last = float('inf')
    for i in x.index:
        medals = x.loc[i,'Total']
        year = x.loc[i,'Year']
        if medals<last:
            temp.append(year)
            last = medals
        else:
            if len(temp)>len(rec_years):
                rec_years = temp.copy()
            temp.clear()
            temp.append(year)
            last = medals
    if len(rec_years)>1:
        x['Year'] = str(rec_years[0])+" - "+str(rec_years[len(rec_years)-1])
    else:
        x['Year'] = str(x.loc[x[['Total']].idxmin(), 'Year'])
    x.drop(['Country','Total'],axis = 1, inplace =True)
    return x.iloc[0]

def find_recession_years(game):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        df=df_Asian.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_recession = df.groupby('Country').apply(recession).reset_index()
        for i in range(len(df_recession)):
            if 'Name' in df_recession['Year'].iloc[i]:
                df_recession['Year'].iloc[i]=df_recession['Year'].iloc[i].split()[1]

        return df_recession
    elif game=="Olympic Games":
        df=df_Olympics.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_recession = df.groupby('Country').apply(recession).reset_index()
        for i in range(len(df_recession)):
            if 'Name' in df_recession['Year'].iloc[i]:
                df_recession['Year'].iloc[i]=df_recession['Year'].iloc[i].split()[1]
        return df_recession
    elif game=="Both":
        df=df_Asian.copy()
        df1=df_Olympics.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_recession = df.groupby('Country').apply(recession).reset_index()
        for i in range(len(df_recession)):
            if 'Name' in df_recession['Year'].iloc[i]:
                df_recession['Year'].iloc[i]=df_recession['Year'].iloc[i].split()[1]

        df1 = df1[['Year','Country','Total']]
        df1 = df1.groupby(['Year','Country']).sum().reset_index()
        df_recession1 = df1.groupby('Country').apply(recession).reset_index()
        for i in range(len(df_recession1)):
            if 'Name' in df_recession1['Year'].iloc[i]:
                df_recession1['Year'].iloc[i]=df_recession1['Year'].iloc[i].split()[1]
        return df_recession,df_recession1
        
def boom(x):
    rec_years= []
    temp = []
    last = float('-inf')
    for i in x.index:
        medals = x.loc[i,'Total']
        year = x.loc[i,'Year']
        if medals>last:
            temp.append(year)
            last = medals
        else:
            if len(temp)>len(rec_years):
                rec_years = temp.copy()
            temp.clear()
            temp.append(year)
            last = medals
    if len(rec_years)>1:
        x['Year'] = str(rec_years[0])+" - "+str(rec_years[len(rec_years)-1])
    else:
        x['Year'] = str(x.loc[x[['Total']].idxmax(), 'Year'])
    x.drop(['Country','Total'],axis = 1, inplace =True)
    return x.iloc[0]

def find_boom_years(game):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        df=df_Asian.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_boom = df.groupby('Country').apply(boom).reset_index()
        for i in range(len(df_boom)):
            if 'Name' in df_boom['Year'].iloc[i]:
                df_boom['Year'].iloc[i]=df_boom['Year'].iloc[i].split()[1]
        return df_boom
    elif game=="Olympic Games":
        df=df_Olympics.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_boom = df.groupby('Country').apply(boom).reset_index()
        for i in range(len(df_boom)):
            if 'Name' in df_boom['Year'].iloc[i]:
                df_boom['Year'].iloc[i]=df_boom['Year'].iloc[i].split()[1]
        return df_boom
    elif game=="Both":
        df=df_Asian.copy()
        df1=df_Olympics.copy()
        df = df[['Year','Country','Total']]
        df = df.groupby(['Year','Country']).sum().reset_index()
        df_boom = df.groupby('Country').apply(boom).reset_index()
        for i in range(len(df_boom)):
            if 'Name' in df_boom['Year'].iloc[i]:
                df_boom['Year'].iloc[i]=df_boom['Year'].iloc[i].split()[1]

        df1 = df1[['Year','Country','Total']]
        df1 = df1.groupby(['Year','Country']).sum().reset_index()
        df_boom1 = df1.groupby('Country').apply(boom).reset_index()
        for i in range(len(df_boom1)):
            if 'Name' in df_boom1['Year'].iloc[i]:
                df_boom1['Year'].iloc[i]=df_boom1['Year'].iloc[i].split()[1]
        return df_boom,df_boom1
#---------Q17---------
def find_best_year(game,category):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        df=df_Asian.copy()
        df = df[['Year','Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Year','Country'], as_index = False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Year',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        df_temp = df_temp.drop_duplicates(subset=['Country'],keep='first')
        return df_temp

    elif game=="Olympic Games":
        df=df_Olympics.copy()
        df = df[['Year','Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Year','Country'], as_index = False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Year',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        df_temp = df_temp.drop_duplicates(subset=['Country'],keep='first')
        return df_temp
    elif game=="Both":
        df=df_Asian.copy()
        df1=df_Olympics.copy()

        df = df[['Year','Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Year','Country'], as_index = False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Year',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        df_temp = df_temp.drop_duplicates(subset=['Country'],keep='first')
        
        df1 = df1[['Year','Sport','Country','Gold','Silver','Bronze','Total']]
        df1 = df1.groupby(['Year','Country'], as_index = False).sum()
        idx1 = df1.groupby(['Country'])[category].transform(max)==df1[category]
        df_temp1 = df1[idx][['Country','Year',category]]
        df_temp1.sort_values(['Country'],inplace=True)
        df_temp1 = df_temp1.reset_index(drop = True)
        df_temp1 = df_temp1.drop_duplicates(subset=['Country'],keep='first')
        return df_temp,df_temp1

def find_best_sport(game,category):
    df_Asian = df_am.copy()
    df_Olympics = df_om.copy()
    if game=="Asian Games":
        df=df_Asian.copy()
        df = df[['Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Country','Sport'],as_index=False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Sport',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        return df_temp

    elif game=="Olympic Games":
        df=df_Olympics.copy()
        df = df[['Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Country','Sport'],as_index=False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Sport',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        return df_temp
    elif game=="Both":
        df=df_Asian.copy()
        df1=df_Olympics.copy()

        df = df[['Sport','Country','Gold','Silver','Bronze','Total']]
        df = df.groupby(['Country','Sport'],as_index=False).sum()
        idx = df.groupby(['Country'])[category].transform(max)==df[category]
        df_temp = df[idx][['Country','Sport',category]]
        df_temp.sort_values(['Country'],inplace=True)
        df_temp = df_temp.reset_index(drop = True)
        
        df1 = df1[['Sport','Country','Gold','Silver','Bronze','Total']]
        df1 = df1.groupby(['Country','Sport'],as_index=False).sum()
        idx1 = df1.groupby(['Country'])[category].transform(max)==df1[category]
        df_temp1 = df1[idx][['Country','Sport',category]]
        df_temp1.sort_values(['Country'],inplace=True)
        df_temp1 = df_temp1.reset_index(drop = True)
        return df_temp,df_temp1



#---------------------
