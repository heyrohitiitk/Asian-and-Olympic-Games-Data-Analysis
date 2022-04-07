#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#Reading all 4 csv files neccesary for this project:
df3=pd.read_csv("Players_Medal_list_Olympics.csv") #Olympic athlete data
df4=pd.read_csv("Medal_List_Olympics.csv") #Olympic medal data
df1=pd.read_csv("Players_Medal_List_Asian.csv") #Asian athlete data
df2=pd.read_csv("Medal_List_Asian.csv") #Asian medal data


# # Individual vs Team Sports

# In[4]:


def plotBar(x, y, labels, xlabel = "", ylabel = "", title = "", figs = (15,10)):
    fig, ax = plt.subplots(figsize = figs)
    width = 1.0/(len(y)+2)
    x_axis = np.arange(len(x))
    p = []
    for idx,y_axis in enumerate(y):
        p.append(ax.bar(x_axis + idx*width, y_axis, width, label=labels[idx]))

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x_axis + width/len(y))
    ax.set_xticklabels(x, rotation = 90)
    ax.legend()

    #for i in p:
     #   ax.bar_label(i, label_type='edge')

    return fig


# In[27]:


def indi_team_table(df_p, game, year = "Overall", medal = "Total"):

    cols = ["Country", "Sport_Type"]
    if year != "Overall":
        cols.append("Year")
        df_p = df_p[df_p["Year"] == year]
    
    sol = df_p.groupby(["Event", "Country", "Year", "Sport", "Sport_Type", "Gold", "Silver", "Bronze"], as_index = False).agg("sum")
    sol = sol.groupby(cols, as_index = False).agg("sum")
    if year == "Overall":
        sol = sol.drop("Year", axis = 1)
    
    tot = [(row["Gold"] + row["Silver"] + row["Bronze"]) for idx, row in sol.iterrows()]
    sol["Total"] = tot
    
    #total medals
    tot_i = sol[sol["Sport_Type"] != "Team"][medal].sum()
    tot_t = sol[sol["Sport_Type"] == "Team"][medal].sum()
    
    countries = pd.unique(sol["Country"]).tolist()
    
    #percentage of Individual medals country-wise
    tot_i_c = []
    for country in countries:
        temp = sol[(sol["Country"] == country) & (sol["Sport_Type"] != "Team")]
        tot = temp[medal].sum()
        tot_i_c.append(round(tot/tot_i * 100, 1))
    
    #percentage of Team medals country-wise
    tot_t_c = []
    for country in countries:
        temp = sol[(sol["Country"] == country) & (sol["Sport_Type"] == "Team")]
        tot = temp[medal].sum()
        tot_t_c.append(round(tot/tot_t * 100, 1))
        
    #Ploting Graph
    fsize = (20,10)
    
    xlabel = "Countries"
    ylabel = "Percentage of medals"
    
    if year == "Overall":
        year = ""
    
    output = {"Country": countries, "Individual-Medal-Percent": tot_i_c, "Team-Medal-Percent": tot_t_c}
    output = pd.DataFrame(output)
    output.sort_values(by=['Individual-Medal-Percent', 'Team-Medal-Percent', 'Country'], ignore_index = True, ascending=False, inplace = True)
    if len(output) > 10:
        i_c = 0
        t_c = 0
        for i in range(10, len(output)):
            i_c += output["Individual-Medal-Percent"][i]
            t_c += output["Team-Medal-Percent"][i]
        output.drop([i for i in range(10, len(output))], inplace = True)
        output.loc[len(output.index)] = ['Others', i_c, t_c]
    #output.set_index("Country", inplace = True)
        
    title = f"Percentage of {medal} Medals won in Individual and Team Sports Country-wise in {game} {year}"
    fig = plotBar(output["Country"], [output["Individual-Medal-Percent"], output["Team-Medal-Percent"]], ["Individual", "Team"], xlabel, ylabel, title, figs = fsize)
    
    return sol, fig


# Here, graph shows the the country-wise percentage of individual medals to team medals. 
# 
# We can see, China, South Korea are some of the top countries who performs better in team sports as compared to individual sport. Top performing countries like Japan, performs better in individual sports compared to team sports. India does slightly better in team sports to individual sports.
# 
# We can alse see same traits in both Asian games as well as Olympics.
# 
# Here, table shows medal count of individual and team sports country-wise.

# In[28]:


indi_team_table(df1, "Asian Games")


# In[ ]:




