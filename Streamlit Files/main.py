#Importing neccesary packages:
import streamlit as st
import numpy as np
import pandas as pd
import helper
import matplotlib.pyplot as plt
import seaborn as sns

#Reading all 4 csv files neccesary for this project:
df_oa=pd.read_csv("Players_Medal_list_Olympics.csv") #Olympic athlete data
df_om=pd.read_csv("Medal_List_Olympics.csv") #Olympic medal data
df_aa=pd.read_csv("Players_Medal_List_Asian.csv") #Asian athlete data
df_am=pd.read_csv("Medal_List_Asian.csv") #Asian medal data

#Created a list of Asian countries:
li_country=["Overall","Afghanistan","Bahrain","Bangladesh","Bhutan","Brunei","Cambodia","China",
"Hong Kong","India","Indonesia", "Iran","Iraq","Japan","Jordan","Kazakhastan","Kuwait",
"Kyrgystan","Laos","Lebanon","Macau","Malaysia","Maldives","Mongolia","Myanmar","Nepal",
"North Korea","Oman","Pakistan","Palestine","Philippines","Qatar","Saudi Arabia","Singapore",
"South Korea","Sri Lanka","Syria","Tajikistan","Thailand","Timor-Leste","Turkmenistan",
"United Arab Emirates","Uzbekistan","Vietnam","Yemen"]

#Adding Olympic games years only and storing in a list:
yr_o=["Overall","All years","1952","1956","1960","1964","1968","1972","1976","1980","1984","1988","1992",
	  "1996","2000","2004","2008","2012","2016","2020"]

#Adding Asian games years only and storing in a list:
yr_a=["Overall","All years","1951","1954","1958","1962","1966","1970","1974","1978","1982","1986","1990",
	  "1994","1998","2002","2006","2010","2014","2018"]

yr_both=["Overall","All years","1951","1952","1954","1956","1958","1960","1962","1964","1966",
		 "1968","1970","1972","1974","1976","1978","1980","1982","1984","1986","1988","1990","1992","1994",
	  "1996","1998","2000","2002","2004","2006","2008","2010","2012","2014","2016","2018","2020"]

sp_o=['Athletics','Gymnastics', 'Hockey', 'Swimming', 'Weightlifting', 'Wrestling',
       'Boxing', 'Shooting', 'Judo', 'Volleyball',
       'Football', 'Archery', 'Diving', 'Synchronized Swimming',
       'Handball', 'Basketball', 'Cycling', 'Fencing', 'Rowing',
       'Table Tennis', 'Badminton', 'Baseball', 'Sailing', 'Softball',
       'Tennis', 'Modern Pentathlon', 'Taekwondo', 'Equestrianism',
       'Canoeing', 'Trampolining', 'Beach Volleyball',
       'Rhythmic Gymnastics', 'Golf', 'Table tennis', 'Artistic swimming',
       'Karate', 'Field hockey', 'Skateboarding', 'Surfing',
       'Sport climbing', 'Modern pentathlon']

sp_a=['Athletics', 'Basketball', 'Cycling', 'Diving', 'Football',
       'Swimming', 'WaterPolo', 'Weightlifting', 'Boxing', 'Shooting',
       'Water polo', 'Wrestling', 'Field hockey', 'Table tennis',
       'Tennis', 'Volleyball', 'Badminton', 'Sailing', 'Fencing',
       'Gymnastics', 'Archery', 'Bowling', 'Equestrian', 'Golf',
       'Handball', 'Rowing', 'Judo', 'Taekwondo', 'Baseball', 'Canoeing',
       'Kabaddi', 'Softball', 'Wushu', 'Artistic swimming', 'Karate',
       'Modern pentathlon', 'Beach volleyball', 'Cue sports',
       'Rugby union', 'Sepak takraw', 'Squash', 'Bodybuilding', 'Chess',
       'Rugby sevens', 'Triathlon', 'Cricket', 'Dragon boat', 'Go',
       'Roller sports', 'Xiangqi', 'Soft tennis', 'Bridge', 'Jet ski',
       'Ju-jitsu', 'Kurash', 'Pencak silat', 'Sambo', 'Sport climbing']

li_country_a=['Overall','Afghanistan', 'Bahrain', 'Bangladesh', 'Brunei', 'Burma', 'Cambodia',
 'Ceylon', 'China', 'Chinese Taipei', 'Hong Kong', 'India', 'Indonesia', 'Iran',
 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Khmer Republic', 'Korea',
 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macau', 'Malaya', 'Malaysia', 'Mongolia',
 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines',
 'Qatar', 'Republic of China', 'Saudi Arabia', 'Singapore', 'South Korea', 'South Vietnam',
 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkmenistan', 'United Arab Emirates',
 'Uzbekistan', 'Vietnam', 'Yemen']

li_country_o=['Overall','Afghanistan', 'Bahrain', 'China', 'Chinese Taipei', 'Hong Kong', 'India',
 'Indonesia', 'Iran', 'Iraq', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan',
 'Malaysia', 'Mongolia', 'North Korea', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia',
 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkmenistan',
 'United Arab Emirates', 'Uzbekistan', 'Vietnam']

#Adding Asian games sports
sport_a = ["Overall",'Athletics', 'Basketball', 'Cycling', 'Diving', 'Football',
       'Swimming', 'WaterPolo', 'Weightlifting', 'Boxing', 'Shooting',
       'Water polo', 'Wrestling', 'Field hockey', 'Table tennis',
       'Tennis', 'Volleyball', 'Badminton', 'Sailing', 'Fencing',
       'Gymnastics', 'Archery', 'Bowling', 'Equestrian', 'Golf',
       'Handball', 'Rowing', 'Judo', 'Taekwondo', 'Baseball', 'Canoeing',
       'Kabaddi', 'Softball', 'Wushu', 'Artistic swimming', 'Karate',
       'Modern pentathlon', 'Beach volleyball', 'Cue sports',
       'Rugby union', 'Sepak takraw', 'Squash', 'Bodybuilding', 'Chess',
       'Rugby sevens', 'Triathlon', 'Cricket', 'Dragon boat', 'Go',
       'Roller sports', 'Xiangqi', 'Soft tennis', 'Bridge', 'Jet ski',
       'Ju-jitsu', 'Kurash', 'Pencak silat', 'Sambo', 'Sport climbing']

#Adding Olympic games sports
sport_o = ["Overall",'Gymnastics', 'Hockey', 'Swimming', 'Weightlifting', 'Wrestling',
       'Boxing', 'Athletics', 'Shooting', 'Judo', 'Volleyball',
       'Football', 'Archery', 'Diving', 'Synchronized Swimming',
       'Handball', 'Basketball', 'Cycling', 'Fencing', 'Rowing',
       'Table Tennis', 'Badminton', 'Baseball', 'Sailing', 'Softball',
       'Tennis', 'Modern Pentathlon', 'Taekwondo', 'Equestrianism',
       'Canoeing', 'Trampolining', 'Beach Volleyball',
       'Rhythmic Gymnastics', 'Golf', 'Table tennis', 'Artistic swimming',
       'Karate', 'Field hockey', 'Skateboarding', 'Surfing',
       'Sport climbing', 'Modern pentathlon']

medals = ["Total", "Gold", "Silver", "Bronze"]

add_type=st.sidebar.radio(
	"Select the type of analysis you want:", ('Medal tally overall analysis', 'Medal tally percentage analysis',
										   'Medal Tally sportswise analysis','Host vs Non host analysis',
										   'Top athletes overall analysis','Top athletes sportswise analysis',
										   'Asian Games Event vs Olympic Medals', 
										   'Male v/s Female Country-wise Medal Winning Comparision',
										   'Male v/s Female Year-wise Medal Winning Comparision',
										   'Individual v/s Team Country-wise Medal Winning Comparision',
										   'Successive Year Analysis','Medal winning/Not winning Analysis',
										   'Detailed Analysis of India',
										   'Countries winning atleast 1 medal in every sport in a year',
										   'Recession year for a country',
										   'Year(sport) in which country won minimum(maximum) medals')
	)

#Adding selection box in sidebar of web app for selecting Games:
add_sidebar=st.sidebar.selectbox(
	"Select the games you wish to analyse:",
	("Home Page","Olympic Games","Asian Games","Both"))

#Adding radio box in sidebar of web app for selecting type of analysis we want:
#add_type=st.sidebar.radio(
#	"Select the type of analysis you want:",
#	("General","Country-wise Analysis","Sports-wise Analysis","Athlete-wise analysis"))

#Creating 4 containers for various headings within a page:
header=st.container()
medals_tally=st.container()
features=st.container()
model_training=st.container()
if add_type=='Medal tally overall analysis':
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
	elif add_sidebar=='Asian Games':
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_a
		)
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Medals Tally(1951 onwards):')
			st.header("Table")
			fig=None
			if(add_country == "Overall" or add_year == "All years"):
				df,fig = helper.Medal_Tally(add_sidebar,add_country,add_year)
			else:
    				df = helper.Medal_Tally(add_sidebar,add_country,add_year)
			st.write(df)
			plot = st.container()
			with plot:
				if(fig != None):
					st.header("Graph")	
					st.pyplot(fig)

	elif add_sidebar=='Olympic Games':
    		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_o
		)
		with header:
			st.title('Welcome to our Olympics games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		with medals_tally:
			st.header('Medals Tally(1951 onwards):')
			st.header("Table")
			fig=None
			if(add_country == "Overall" or add_year == "All years"):
				df,fig = helper.Medal_Tally(add_sidebar,add_country,add_year)
			else:
    				df = helper.Medal_Tally(add_sidebar,add_country,add_year)
			st.write(df)
			plot = st.container()
			with plot:
				if(fig != None):
					st.header("Graph")	
					st.pyplot(fig)

	elif add_sidebar=='Both':
    		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Asian Games Year:
		add_year_a=st.sidebar.selectbox(
		"Select the Asian Games year:", yr_a
		)
		#Adding selection box in sidebar of web app for selecting Olympic games Year:
		add_year_o=st.sidebar.selectbox(
		"Select the Olympic Games year:", yr_o
		)
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Medals Tally(1951 onwards):')
			st.subheader('Asian Games:')
			fig=None
			if(add_country == "Overall" or add_year_a == "All years"):
				df,fig = helper.Medal_Tally("Asian Games",add_country,add_year_a)
			else:
    				df = helper.Medal_Tally("Asian Games",add_country,add_year_a)
			st.write(df)
			plot = st.container()
			with plot:
				if(fig != None):
					st.header("Graph")	
					st.pyplot(fig)
			st.subheader('Olympic Games:')
			st.header("Table")
			fig=None
			if(add_country == "Overall" or add_year_o == "All years"):
				df,fig = helper.Medal_Tally("Olympic Games",add_country,add_year_o)
			else:
    				df = helper.Medal_Tally("Olympic Games",add_country,add_year_o)
			st.write(df)
			plot = st.container()
			with plot:
				if(fig != None):
					st.header("Graph")	
					st.pyplot(fig)

elif add_type=='Medal tally percentage analysis':
		if add_sidebar=='Home Page':
				with header:
					st.title('Welcome to our project')
					st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
					st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			#Adding selection box in sidebar of web app for selecting Country:
			add_country=st.sidebar.selectbox(
			"Select the country:", li_country
			)
			#Adding selection box in sidebar of web app for selecting Year:
			add_year=st.sidebar.selectbox(
			"Select the year:", yr_a
			)
			
			with header:
				st.title('Welcome to our Asian games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Medals Percentage(1951 onwards):')
				st.header("Table")
				fig=None
				if(add_country == "Overall"):
					df,fig = helper.Medal_percentage(add_sidebar,add_country,add_year)
				else:
						df = helper.Medal_percentage(add_sidebar,add_country,add_year)
				st.write(df)
				plot = st.container()
				with plot:
					if(fig != None):
						st.header("Graph")	
						st.pyplot(fig)

		elif add_sidebar=='Olympic Games':
    		#Adding selection box in sidebar of web app for selecting Country:
			add_country=st.sidebar.selectbox(
			"Select the country:", li_country
			)
			#Adding selection box in sidebar of web app for selecting Year:
			add_year=st.sidebar.selectbox(
			"Select the year:", yr_o
			)
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Medals Percentage(1951 onwards):')
				st.header("Table")
				fig=None
				if(add_country == "Overall" or add_year == "All years"):
					df,fig = helper.Medal_percentage(add_sidebar,add_country,add_year)
				else:
						df = helper.Medal_percentage(add_sidebar,add_country,add_year)
				st.write(df)
				plot = st.container()
				with plot:
					if(fig != None):
						st.header("Graph")	
						st.pyplot(fig)

		elif add_sidebar=='Both':
    		#Adding selection box in sidebar of web app for selecting Country:
			add_country=st.sidebar.selectbox(
			"Select the country:", li_country
			)
			#Adding selection box in sidebar of web app for selecting Asian Games Year:
			add_year_a=st.sidebar.selectbox(
			"Select the Asian Games year:", yr_a
			)
			#Adding selection box in sidebar of web app for selecting Olympic games Year:
			add_year_o=st.sidebar.selectbox(
			"Select the Olympic Games year:", yr_o
			)
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Medals Percentage(1951 onwards):')
				st.subheader('Asian Games:')
				st.header("Table")
				fig=None
				if(add_country == "Overall" or add_year_a == "All years"):
					df,fig = helper.Medal_percentage("Asian Games",add_country,add_year_a)
				else:
						df = helper.Medal_percentage("Asian Games",add_country,add_year_a)
				st.write(df)
				plot = st.container()
				with plot:
					if(fig != None):
						st.header("Graph")	
						st.pyplot(fig)
				st.subheader('Olympic Games:')
				st.header("Table")
				fig=None
				if(add_country == "Overall" or add_year_o == "All years"):
					df,fig = helper.Medal_percentage("Olympic Games",add_country,add_year_o)
				else:
						df = helper.Medal_percentage("Olympic Games",add_country,add_year_o)
				st.write(df)
				plot = st.container()
				with plot:
					if(fig != None):
						st.header("Graph")	
						st.pyplot(fig)

elif add_type=='Medal Tally sportswise analysis':
			if add_sidebar=='Home Page':
				with header:
					st.title('Welcome to our project')
					st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
					st.image('Homepage.jpg')
			
			elif add_sidebar=='Asian Games':
				#Adding selection box in sidebar of web app for selecting Country:
				add_country=st.sidebar.selectbox(
				"Select the country:", li_country
				)
				#Adding selection box in sidebar of web app for selecting Year:
				add_year=st.sidebar.selectbox(
				"Select the year:", yr_a
				)
					
				with header:
					st.title('Welcome to our Asian games analysis page:')
					st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
					
					
				with medals_tally:
					st.header('Medals Sport Wise(1951 onwards):')
					st.header("Table")
					fig=None
					if(add_country != "Overall"):
						df,fig = helper.Medal_sport_wise(add_sidebar,add_country,add_year)
					else:
						df = helper.Medal_sport_wise(add_sidebar,add_country,add_year)
					st.write(df)
					plot = st.container()
					with plot:
						if(fig != None):
							st.header("Graph")	
							st.pyplot(fig)

			elif add_sidebar=='Olympic Games':
        		#Adding selection box in sidebar of web app for selecting Country:
				add_country=st.sidebar.selectbox(
				"Select the country:", li_country
				)
				#Adding selection box in sidebar of web app for selecting Year:
				add_year=st.sidebar.selectbox(
				"Select the year:", yr_o
				)
				with header:
					st.title('Welcome to our Olympics games analysis page:')
					st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
				
				with medals_tally:
					st.header('Medals Sport Wise(1951 onwards):')
					st.header("Table")
					fig=None
					if(add_country != "Overall"):
						df,fig = helper.Medal_sport_wise(add_sidebar,add_country,add_year)
					else:
							df = helper.Medal_sport_wise(add_sidebar,add_country,add_year)
					st.write(df)
					plot = st.container()
					with plot:
						if(fig != None):
							st.header("Graph")	
							st.pyplot(fig)

			elif add_sidebar=='Both':
        		#Adding selection box in sidebar of web app for selecting Country:
				add_country=st.sidebar.selectbox(
				"Select the country:", li_country
				)
				#Adding selection box in sidebar of web app for selecting Asian Games Year:
				add_year_a=st.sidebar.selectbox(
				"Select the Asian Games year:", yr_a
				)
				#Adding selection box in sidebar of web app for selecting Olympic games Year:
				add_year_o=st.sidebar.selectbox(
				"Select the Olympic Games year:", yr_o
				)
				with header:
					st.title('Welcome to our comparative analysis page:')
					st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
				
				
				with medals_tally:
					st.header('Medals Sport Wise(1951 onwards):')
					st.subheader('Asian Games:')
					st.header("Table")
					fig=None
					if(add_country != "Overall"):
						df,fig = helper.Medal_sport_wise("Asian Games",add_country,add_year_a)
					else:
							df = helper.Medal_sport_wise("Asian Games",add_country,add_year_a)
					st.write(df)
					plot = st.container()
					with plot:
						if(fig != None):
							st.header("Graph")	
							st.pyplot(fig)
					st.subheader('Olympic Games:')
					st.header("Table")
					fig=None
					if(add_country != "Overall"):
						df,fig = helper.Medal_sport_wise("Olympic Games",add_country,add_year_o)
					else:
							df = helper.Medal_sport_wise("Olympic Games",add_country,add_year_o)
					st.write(df)
					plot = st.container()
					with plot:
						if(fig != None):
							st.header("Graph")	
							st.pyplot(fig)

elif add_type=='Host vs Non host analysis':
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
	elif add_sidebar=='Asian Games':
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:

			host,non_host=helper.Host_analysis(add_sidebar)
			st.subheader('Performance as host')
			st.write(host)
			st.subheader('Performance as non-host')
			st.write(non_host)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Total/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Total/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise gold medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Gold/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Gold/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise silver medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Silver/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Silver/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise bronze medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Bronze/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Bronze/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#All data comparison:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country:")
			
			X_axis = np.arange(len(host['Country']))
			plt.bar(X_axis - 0.2,host['Total/Yr'],width=0.1,label='host-Total',color='yellow')
			plt.bar(X_axis - 0.1,host['Gold/Yr'],width=0.1,label='host-Gold')
			plt.bar(X_axis + 0.0,host['Silver/Yr'],width=0.1,label='host-Silver')
			plt.bar(X_axis + 0.1,host['Bronze/Yr'],width=0.1,label='host-Bronze')
			plt.xticks(X_axis, host['Country'])
			
			plt.bar(X_axis - 0.2,non_host['Total/Yr'],width=0.1,label='non-host-Total')
			plt.bar(X_axis - 0.1,non_host['Gold/Yr'],width=0.1,label='non-host-Gold')
			plt.bar(X_axis + 0.0,non_host['Silver/Yr'],width=0.1,label='non-host-Silver')
			plt.bar(X_axis + 0.1,non_host['Bronze/Yr'],width=0.1,label='non-host-Bronze')
			plt.xticks(X_axis, non_host['Country'])
			
			plt.legend()
			st.pyplot(plt)
	elif add_sidebar=='Olympic Games':
		with header:
			st.title('Welcome to our Olympics games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		with medals_tally:

			host,non_host=helper.Host_analysis(add_sidebar)
			st.subheader('Performance as host')
			st.write(host)
			st.subheader('Performance as non-host')
			st.write(non_host)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Total/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Total/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise gold medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Gold/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Gold/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise silver medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Silver/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Silver/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#Medals won on an average as hosts and as non hosts comparison graphically:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise bronze medals won as host country and as non host country:")
			plt.bar(host['Country'],host['Bronze/Yr'],width=0.1,label='host')
			plt.bar(non_host['Country'],non_host['Bronze/Yr'],width=0.1,label='non-host')
			plt.legend()
			st.pyplot(plt)
			#All data comparison:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country:")
			
			X_axis = np.arange(len(host['Country']))
			plt.bar(X_axis - 0.2,host['Total/Yr'],width=0.1,label='host-Total',color='yellow')
			plt.bar(X_axis - 0.1,host['Gold/Yr'],width=0.1,label='host-Gold')
			plt.bar(X_axis + 0.0,host['Silver/Yr'],width=0.1,label='host-Silver')
			plt.bar(X_axis + 0.1,host['Bronze/Yr'],width=0.1,label='host-Bronze')
			plt.xticks(X_axis, host['Country'])
			
			plt.bar(X_axis - 0.2,non_host['Total/Yr'],width=0.1,label='non-host-Total')
			plt.bar(X_axis - 0.1,non_host['Gold/Yr'],width=0.1,label='non-host-Gold')
			plt.bar(X_axis + 0.0,non_host['Silver/Yr'],width=0.1,label='non-host-Silver')
			plt.bar(X_axis + 0.1,non_host['Bronze/Yr'],width=0.1,label='non-host-Bronze')
			plt.xticks(X_axis, non_host['Country'])
			
			plt.legend()
			st.pyplot(plt)
	elif add_sidebar=='Both':
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			host_a,non_host_a=helper.Host_analysis('Asian Games')
			st.subheader('Performance as host in Asian Games')
			st.write(host_a)
			st.subheader('Performance as non-host in Asian Games')
			st.write(non_host_a)
			host_o,non_host_o=helper.Host_analysis('Olympic Games')
			st.subheader('Performance as host in Olympic Games')
			st.write(host_o)
			st.subheader('Performance as non-host in Olympic Games')
			st.write(non_host_o)
			#All data comparison:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country in Asian Games:")
			
			X_axis = np.arange(len(host_a['Country']))
			plt.bar(X_axis - 0.2,host_a['Total/Yr'],width=0.1,label='host-Total',color='yellow')
			plt.bar(X_axis - 0.1,host_a['Gold/Yr'],width=0.1,label='host-Gold')
			plt.bar(X_axis + 0.0,host_a['Silver/Yr'],width=0.1,label='host-Silver')
			plt.bar(X_axis + 0.1,host_a['Bronze/Yr'],width=0.1,label='host-Bronze')
			plt.xticks(X_axis, host_a['Country'])
			
			plt.bar(X_axis - 0.2,non_host_a['Total/Yr'],width=0.1,label='non-host-Total')
			plt.bar(X_axis - 0.1,non_host_a['Gold/Yr'],width=0.1,label='non-host-Gold')
			plt.bar(X_axis + 0.0,non_host_a['Silver/Yr'],width=0.1,label='non-host-Silver')
			plt.bar(X_axis + 0.1,non_host_a['Bronze/Yr'],width=0.1,label='non-host-Bronze')
			plt.xticks(X_axis, non_host_a['Country'])
			
			plt.legend()
			st.pyplot(plt)
			#All data comparison:
			plt.figure(figsize=(15,5))
			plt.title("Yearwise total medals won as host country and as non host country in Olympics:")
			
			X_axis = np.arange(len(host_o['Country']))
			plt.bar(X_axis - 0.2,host_o['Total/Yr'],width=0.1,label='host-Total',color='yellow')
			plt.bar(X_axis - 0.1,host_o['Gold/Yr'],width=0.1,label='host-Gold')
			plt.bar(X_axis + 0.0,host_o['Silver/Yr'],width=0.1,label='host-Silver')
			plt.bar(X_axis + 0.1,host_o['Bronze/Yr'],width=0.1,label='host-Bronze')
			plt.xticks(X_axis, host_o['Country'])
			
			plt.bar(X_axis - 0.2,non_host_o['Total/Yr'],width=0.1,label='non-host-Total')
			plt.bar(X_axis - 0.1,non_host_o['Gold/Yr'],width=0.1,label='non-host-Gold')
			plt.bar(X_axis + 0.0,non_host_o['Silver/Yr'],width=0.1,label='non-host-Silver')
			plt.bar(X_axis + 0.1,non_host_o['Bronze/Yr'],width=0.1,label='non-host-Bronze')
			plt.xticks(X_axis, non_host_o['Country'])
			
			plt.legend()
			st.pyplot(plt)
			
elif add_type=='Top athletes overall analysis':
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
	elif add_sidebar=='Asian Games':
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_a
		)
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')

		with medals_tally:
			st.header('Top 5 athletes on the basis of user inputs:')
			df_5=helper.Athlete_countrywise(add_sidebar,add_country,add_year)
			st.write(df_5)
	elif add_sidebar=='Olympic Games':
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_o
		)
		with header:
			st.title('Welcome to our Olympics games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		with medals_tally:
			st.header('Top 5 athletes on the basis of user inputs:')
			df_5=helper.Athlete_countrywise(add_sidebar,add_country,add_year)
			st.write(df_5)

	elif add_sidebar=='Both':
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Asian Games Year:
		add_year_a=st.sidebar.selectbox(
		"Select the Asian Games year:", yr_a
		)
		#Adding selection box in sidebar of web app for selecting Olympic games Year:
		add_year_o=st.sidebar.selectbox(
		"Select the Olympic Games year:", yr_o
		)
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Top 5 athletes in Asian Games and Olympics on the basis of user inputs:')
			st.subheader('Asian Games:')
			df_5=helper.Athlete_countrywise('Asian Games',add_country,add_year_a)
			st.write(df_5)
			st.subheader('Olympic Games:')
			df_5b=helper.Athlete_countrywise('Olympic Games',add_country,add_year_o)
			st.write(df_5b)

elif add_type=='Top athletes sportswise analysis':
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
	elif add_sidebar=='Asian Games':
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sp_a
		)
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_a
		)
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')

		with medals_tally:
			st.header('Top 5 athletes sportswise on the basis of user inputs:')
			df_6=helper.Athlete_sportwise(add_sidebar,add_sport,add_country,add_year)
			st.write(df_6)
	elif add_sidebar=='Olympic Games':
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sp_o
		)
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_o
		)
		with header:
			st.title('Welcome to our Olympics games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		with medals_tally:
			st.header('Top 5 athletes sportswise on the basis of user inputs:')
			df_6=helper.Athlete_sportwise(add_sidebar,add_sport,add_country,add_year)
			st.write(df_6)

	elif add_sidebar=='Both':
		add_sport_a=st.sidebar.selectbox(
		"Select the Asian sport:", sp_a
		)
		add_sport_o=st.sidebar.selectbox(
		"Select the Olympic sport:", sp_o
		)
		#Adding selection box in sidebar of web app for selecting Country:
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country
		)
		#Adding selection box in sidebar of web app for selecting Asian Games Year:
		add_year_a=st.sidebar.selectbox(
		"Select the Asian Games year:", yr_a
		)
		#Adding selection box in sidebar of web app for selecting Olympic games Year:
		add_year_o=st.sidebar.selectbox(
		"Select the Olympic Games year:", yr_o
		)
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Top 5 athletes in selected sport in Asian Games and Olympics on the basis of user inputs:')
			st.subheader('Asian Games:')
			df_6=helper.Athlete_sportwise('Asian Games',add_sport_a,add_country,add_year_a)
			st.write(df_6)
			st.subheader('Olympic Games:')
			df_6b=helper.Athlete_sportwise('Olympic Games',add_sport_o,add_country,add_year_o)
			st.write(df_6b)

elif add_type=='Male v/s Female Country-wise Medal Winning Comparision':
		
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
		
	elif add_sidebar=='Asian Games':
		yr_a_1 = yr_a
		yr_a_1.remove("All years")
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_a_1
		)
		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_a
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries(1951 onwards):')
			df_1, fig = helper.Q7b(df_aa, "Asian Games", year = add_year, sport = add_sport, medal = add_medal)
			st.write(df_1)
			st.pyplot(fig)
			
	elif add_sidebar=='Olympic Games':
		yr_o_1 = yr_o
		yr_o_1.remove("All years")
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_o_1
		)
		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_o
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Olympic games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries(1951 onwards):')
			df_1, fig = helper.Q7b(df_oa, "Olympic Games", year = add_year, sport = add_sport, medal = add_medal)
			st.write(df_1)
			st.pyplot(fig)

	elif add_sidebar=='Both':
		sport_b = [value for value in sport_a if value in sport_o]

		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_b
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries(1951 onwards):')
			df_1, fig1 = helper.Q7b(df_aa, "Asian Games", year = "Overall", sport = add_sport, medal = add_medal)
			df_2, fig2 = helper.Q7b(df_oa, "Olympic Games", year = "Overall", sport = add_sport, medal = add_medal)
			col1, col2 = st.columns(2)
			col1.write(df_1)
			col2.write(df_2)
			st.success("This are the tables")
			col1, col2 = st.columns(2)
			col1.pyplot(fig1)
			col2.pyplot(fig2)

elif add_type=='Male v/s Female Year-wise Medal Winning Comparision':
	
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
		
	elif add_sidebar=='Asian Games':
		#Adding selection box in sidebar of web app for selecting Year:
		li_country_1 = li_country_a
		li_country_1.remove("Overall")
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country_1
		)
		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_o
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries(1951 onwards):')
			df_1, output = helper.Q7c(df_aa, "Asian", nation = add_country, sport = add_sport, medal = add_medal)
			st.write(df_1)
			st.line_chart(output)
			
	elif add_sidebar=='Olympic Games':
		#Adding selection box in sidebar of web app for selecting Year:
		li_country_1 = li_country_o
		li_country_1.remove("Overall")
		
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country_1
		)
		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_o
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Olympic games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries(1951 onwards):')
			df_1, output = helper.Q7c(df_oa, "Olympic games", nation = add_country, sport = add_sport, medal = add_medal)
			st.write(df_1)
			st.line_chart(output)

	elif add_sidebar=='Both':
		li_country_1 = [value for value in li_country_a if value in li_country_o]
		li_country_1.remove("Overall")

		
		add_country=st.sidebar.selectbox(
		"Select the country:", li_country_1
		)
		#Adding selection box in sidebar of web app for selecting Sport:
		add_sport=st.sidebar.selectbox(
		"Select the sport:", sport_o
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Gender-wise Medals Tally for Countries Yearwise(1951 onwards):')
			df_1, output1 = helper.Q7c(df_aa, "Asian games", nation = add_country, sport = add_sport, medal = add_medal)
			df_2, output2 = helper.Q7c(df_oa, "Olympic games", nation = add_country, sport = add_sport, medal = add_medal)
			col1, col2 = st.columns(2)
			col1.write(df_1)
			col2.write(df_2)
			st.success("Table of Asian games and Olympics having year-wise medal count for male and female")
			st.line_chart(output1)
			st.success("Asian games")
			st.line_chart(output2)
			st.success("Olympic Games")

elif add_type=='Individual v/s Team Country-wise Medal Winning Comparision':
	if add_sidebar=='Home Page':
		with header:
			st.title('Welcome to our project')
			st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
		st.image('Homepage.jpg')
		
	elif add_sidebar=='Asian Games':
		yr_a_1 = yr_a
		yr_a_1.remove("All years")
		
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_a_1
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Asian games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Individual v/s Team Sports Medal Tally in Asian Games for Countries(1951 onwards):')
			df_1, fig = helper.Q8a(df_aa, "Asian", year = add_year, medal = add_medal)
			st.write(df_1)
			st.pyplot(fig)
			
	elif add_sidebar=='Olympic Games':
		yr_o_1 = yr_o
		yr_o_1.remove("All years")
		
		#Adding selection box in sidebar of web app for selecting Year:
		add_year=st.sidebar.selectbox(
		"Select the year:", yr_o_1
		)
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our Olympic games analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Individual v/s Team Sports Medal Tally in Olympic Games for Countries(1951 onwards):')
			df_1, fig = helper.Q8a(df_oa, "Olympic Games", year = add_year, medal = add_medal)
			st.write(df_1)
			st.pyplot(fig)

	elif add_sidebar=='Both':
	
		#Adding selection box in sidebar of web app for selecting Medal:
		add_medal=st.sidebar.selectbox(
		"Select the medal type:", medals
		)
		
		
		with header:
			st.title('Welcome to our comparative analysis page:')
			st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
		
		
		with medals_tally:
			st.header('Individual v/s Team Sports Comparision(1951 onwards):')
			df_1, fig1 = helper.Q8a(df_aa, "Asian Games", year = "Overall", medal = add_medal)
			df_2, fig2 = helper.Q8a(df_oa, "Olympic Games", year = "Overall", medal = add_medal)
			col1, col2 = st.columns(2)
			col1.write(df_1)
			col2.write(df_2)
			st.success("This are the tables")
			col1, col2 = st.columns(2)
			col1.pyplot(fig1)
			col2.pyplot(fig2)


elif add_type=='Asian Games Event vs Olympic Medals':
	with header:
		st.title('Welcome to our Asian games analysis page:')
		st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
	
	st.header("Effect of number of events in Asian games to the increase of medals in Olympics")
	
	fig1, fig2 = helper.Q7a()
	col1, col2 = st.columns(2)
	col1.pyplot(fig1)
	col2.pyplot(fig2)
	st.success('''The first graph shows the number of events for male and female athletes over the years
in Asian games. The second graph shows the number of medals won by Asian male
and female athletes in Olympics from 1952(After the Asian games have started).
With the increase in games for males and females in Asian games, there is an increase
in the number of medals won in the Olympics by males and females. Also, the gap
between medals won by males and females in the Olympics decreases as the gap
between the number of games in Asian games decreases.''')


#......................................................................................................................

elif add_type == "Successive Year Analysis":
    add_type_sub = st.sidebar.selectbox(
        "Select the type of analysis you want:",
        (
            "General analysis",
            "Country-wise analysis",
            "Sport-wise analysis",
        ),
    )
    result = helper.SuccessiveYearComparison()

    with header:
        st.title(
            "Comparative Analysis between Asian and Olympic games for successive years"
        )
        st.write(
            "Here, the primary thing that needs to be done is the comparison between the Asian and Olympic games across the years, i.e. the comparison is made between the years in which Asian games take place and immediate next year in which Olympic games take place."
        )

    if add_type_sub == "General analysis":
        add_year_type = st.sidebar.selectbox(
        "Select the Asian Year:",
        yr_a[1:]
        )

        with medals_tally:
            st.subheader("Final Overall Table for all Countries")
            if add_year_type!="All years":
                year=int(add_year_type)
                result = result[result["Year_Asian"]==year]
            st.write(result)
            if len(result)==0:
                st.text("No Info")
            else:
                st.write("Now, we got the final summary table and by using this table we derive various insights, like we can find the players who wom medal in asian and immediate next olympic, we can also find males and females participation in asian and compare it with immediate next olympic")

            st.subheader("Players winning Atleast one medal Successively in Asian and Olympics")
            overall_comparison=result[["Player","Country","Year_Asian","Year_Olympic","Sport"]]
            overall_comparison["Total_Asian"]=result["Gold_Asian"]+result["Silver_Asian"]+result["Bronze_Asian"]
            overall_comparison["Total_Olympic"]=result["Gold_Olympic"]+result["Silver_Olympic"]+result["Bronze_Olympic"]
            st.write(overall_comparison)

            if len(overall_comparison)==0:
                st.text("No Info")
            else:
                st.write("So here we can see those players who wins atleast one medal in the asian and immediate next olympic games,and from this we get to know about the sports in which players win medals successively in asian and olympic games.")

            st.subheader("Gold medal comparison Successively in Asian and Olympics")
            gold_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic"]]
            gold_comparison=gold_comparison.sort_values(by=["Gold_Asian","Gold_Olympic"],ascending=False)
            st.write(gold_comparison)

            st.subheader("Silver medal comparison Successively in Asian and Olympics")
            silver_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Silver_Asian","Silver_Olympic"]]
            silver_comparison=silver_comparison.sort_values(by=["Silver_Asian","Silver_Olympic"],ascending=False)
            st.write(silver_comparison)

            st.subheader("Bronze comparison medal Successively in Asian and Olympics")
            bronze_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Bronze_Asian","Bronze_Olympic"]]
            bronze_comparison=bronze_comparison.sort_values(by=["Bronze_Asian","Bronze_Olympic"],ascending=False)
            st.write(bronze_comparison)

            st.subheader("Females winning Atleast one medal Successively in Asian and Olympics")
            female_comparison=result[result["Gender"]=="F"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(female_comparison)

            st.subheader("Males winning Atleast one medal Successively in Asian and Olympics")
            male_comparison=result[result["Gender"]=="M"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(male_comparison)

            st.subheader("Country with Maximum number of Players winning Successively in Asian and Olympics")

            countries=result["Country"].unique()
            max_player_country=[]

            for x in countries:
                result_country=result[result["Country"]==x]
                max_player_country.append([x,len(result_country)])
            max_player_country=sorted(max_player_country,key=lambda x:x[1])
            if len(max_player_country)==0 or max_player_country[-1][1]==0:
                st.text("No Country")
            else:
                st.text(f"{max_player_country[-1][0]} : {max_player_country[-1][1]} players")

            st.subheader("Country with Maximum number of Players winning Gold Medal Successively in Asian and Olympics")

            max_player_gold_country=[]
            for x in countries:
                result_country=result[result["Country"]==x]
                result_country=result_country[(result_country["Gold_Asian"]>=1) & (result_country["Gold_Olympic"]>=1)]
                max_player_gold_country.append([x,len(result_country)])
            max_player_gold_country=sorted(max_player_gold_country,key=lambda x:x[1])


            if len(max_player_gold_country)==0 or max_player_gold_country[-1][1]==0:
                st.text("No Country")
            else:
                st.text(f"{max_player_gold_country[-1][0]} : {max_player_gold_country[-1][1]} players")

    elif add_type_sub=="Country-wise analysis":
        add_country_type = st.sidebar.selectbox(
        "Select the Country:",
        li_country[1:],
        )
        add_year_type = st.sidebar.selectbox(
        "Select the Asian Year:",
        yr_a[1:]
        )
        with medals_tally:
            st.subheader(f"Final Overall Table for {add_country_type}")
            country=add_country_type
            result=result[result["Country"]==country]

            if add_year_type!="All years":
                year=int(add_year_type)
                result = result[result["Year_Asian"]==year]
            
            st.write(result)
            if len(result)==0:
                st.text("No Info")
            else:
                st.write(f"Now, we got the final summary table for {add_country_type} and by using this table we derive various insights, like we can find the players who won medal in asian and immediate next olympic, we can also find males and females participation in asian and compare it with immediate next olympic")

            st.subheader("Players winning Atleast one medal Successively in Asian and Olympics")
            overall_comparison=result[["Player","Country","Year_Asian","Year_Olympic","Sport"]]
            overall_comparison["Total_Asian"]=result["Gold_Asian"]+result["Silver_Asian"]+result["Bronze_Asian"]
            overall_comparison["Total_Olympic"]=result["Gold_Olympic"]+result["Silver_Olympic"]+result["Bronze_Olympic"]
            st.write(overall_comparison)

            if len(overall_comparison)==0:
                st.text("No Info")
            else:
                st.write("So here we can see those players who wins atleast one medal in the asian and immediate next olympic games,and from this we get to know about the sports in which players win medals successively in asian and olympic games.")

            st.subheader("Gold medal comparison Successively in Asian and Olympics")
            gold_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic"]]
            gold_comparison=gold_comparison.sort_values(by=["Gold_Asian","Gold_Olympic"],ascending=False)
            st.write(gold_comparison)

            st.subheader("Silver medal comparison Successively in Asian and Olympics")
            silver_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Silver_Asian","Silver_Olympic"]]
            silver_comparison=silver_comparison.sort_values(by=["Silver_Asian","Silver_Olympic"],ascending=False)
            st.write(silver_comparison)

            st.subheader("Bronze comparison medal Successively in Asian and Olympics")
            bronze_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Bronze_Asian","Bronze_Olympic"]]
            bronze_comparison=bronze_comparison.sort_values(by=["Bronze_Asian","Bronze_Olympic"],ascending=False)
            st.write(bronze_comparison)

            st.subheader("Females winning Atleast one medal Successively in Asian and Olympics")
            female_comparison=result[result["Gender"]=="F"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(female_comparison)

            st.subheader("Males winning Atleast one medal Successively in Asian and Olympics")
            male_comparison=result[result["Gender"]=="M"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(male_comparison)

    elif add_type_sub=="Sport-wise analysis":
        add_country_type = st.sidebar.selectbox(
        "Select the Country:",
        li_country,
        )

        sports=list(result["Sport"].unique())
        sports.insert(0,"All Sports")

        add_sport_type = st.sidebar.selectbox(
        "Select the Sport:",
            sports
        )

        add_year_type = st.sidebar.selectbox(
        "Select the Asian Year:",
        yr_a[1:]
        )
        with medals_tally:
            st.subheader(f"Final Summary Table")
            country=add_country_type
            if country!="Overall":
                result=result[result["Country"]==country]

            if add_sport_type!="All Sports":
                result=result[result["Sport"]==add_sport_type]
            
            if add_year_type!="All years":
                year=int(add_year_type)
                result = result[result["Year_Asian"]==year]
            
            st.write(result)
            if len(result)==0:
                st.text("No Info")
            else:
                st.write(f"Now, we got the final summary table and by using this table we derive various insights, like we can find the players who won medal in asian and immediate next olympic, we can also find males and females participation in asian and compare it with immediate next olympic")

            st.subheader("Players winning Atleast one medal Successively in Asian and Olympics")
            overall_comparison=result[["Player","Country","Year_Asian","Year_Olympic","Sport"]]
            overall_comparison["Total_Asian"]=result["Gold_Asian"]+result["Silver_Asian"]+result["Bronze_Asian"]
            overall_comparison["Total_Olympic"]=result["Gold_Olympic"]+result["Silver_Olympic"]+result["Bronze_Olympic"]
            st.write(overall_comparison)

            if len(overall_comparison)==0:
                st.text("No Info")
            else:
                st.write("So here we can see those players who wins atleast one medal in the asian and immediate next olympic games,and from this we get to know about the sports in which players win medals successively in asian and olympic games.")

            st.subheader("Gold medal comparison Successively in Asian and Olympics")
            gold_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic"]]
            gold_comparison=gold_comparison.sort_values(by=["Gold_Asian","Gold_Olympic"],ascending=False)
            st.write(gold_comparison)

            st.subheader("Silver medal comparison Successively in Asian and Olympics")
            silver_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Silver_Asian","Silver_Olympic"]]
            silver_comparison=silver_comparison.sort_values(by=["Silver_Asian","Silver_Olympic"],ascending=False)
            st.write(silver_comparison)

            st.subheader("Bronze comparison medal Successively in Asian and Olympics")
            bronze_comparison=result[["Player","Year_Asian","Year_Olympic","Sport","Bronze_Asian","Bronze_Olympic"]]
            bronze_comparison=bronze_comparison.sort_values(by=["Bronze_Asian","Bronze_Olympic"],ascending=False)
            st.write(bronze_comparison)

            st.subheader("Females winning Atleast one medal Successively in Asian and Olympics")
            female_comparison=result[result["Gender"]=="F"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(female_comparison)

            st.subheader("Males winning Atleast one medal Successively in Asian and Olympics")
            male_comparison=result[result["Gender"]=="M"][["Player","Year_Asian","Year_Olympic","Sport","Gold_Asian","Gold_Olympic","Silver_Asian","Silver_Olympic","Bronze_Asian","Bronze_Olympic"]]
            st.write(male_comparison)

            if add_sport_type=="All Sports":
                st.subheader("Top Sports with Maximum number of players won medal successively in Asian and Olympics")
                games=result["Sport"].unique()
                max_player_sport=[]

                for x in games:
                    result_sport=result[result["Sport"]==x]
                    max_player_sport.append([x,len(result_sport)])
                max_player_sport=sorted(max_player_sport,key=lambda x:x[1])

                for x in max_player_sport[-5:]:
                    st.text(f"{x[0]} : {x[1]} Players")

                st.subheader("Top Sports with Maximum number of players won Gold medal successively in Asian and Olympics")
                max_player_gold_sport=[]

                for x in games:
                    result_sport=result[result["Sport"]==x]
                    result_sport=result_sport[(result_sport["Gold_Asian"]>=1) & (result_sport["Gold_Olympic"]>=1)]
                    max_player_gold_sport.append([x,len(result_sport)])
                max_player_gold_sport=sorted(max_player_gold_sport,key=lambda x:x[1])

                for x in max_player_gold_sport[-5:]:
                    st.text(f"{x[0]} : {x[1]} Player")


elif add_type=="Medal winning/Not winning Analysis":
    add_type_sub = st.sidebar.radio(
        "Select the type of analysis you want:",
        (
            "Country analysis",
            "Player analysis",
        ),
    )

    add_game_type = st.sidebar.selectbox(
        "Select the type of analysis you want:",
        (
            "Olympic games",
            "Asian games",
            "Both"
        ),
    )

    with header:
        st.title(
            "Analysis of Countries and Players in terms medal winning/Not winning"
        )
        st.write("In it the primary thing that needs to be done is to do country wise and player wise analysis with respect to the type of medal won(Year wise and overall),so we need find the countries who never won a gold or never won a silver medal or never won a bronze medal and this needs to be done for both asian and olympic games, and also we find the players who never won a gold or never won a silver medal or never won a bronze medal and this needs also to be done for both asian and olympic games.")

    with medals_tally:
        if add_type_sub=="Country analysis":
            if add_game_type=="Olympic games":
                add_year_type = st.sidebar.selectbox(
                    "Select the type of analysis you want:",
                    yr_o,
                )
                oly_medal=pd.read_csv("Medal_List_Olympics.csv")
                oly_medal2=oly_medal.drop(columns=["Host_City","Sport"])
                if add_year_type=="All years":
                    oly_medal3=oly_medal2.groupby(by=["Year","Country"]).sum().reset_index()
                elif add_year_type=="Overall":
                    oly_medal3=oly_medal2.drop(columns=["Year"])
                    oly_medal3=oly_medal3.groupby(by=["Country"]).sum().reset_index()
                else:
                    y=int(add_year_type)
                    oly_medal3=oly_medal2.groupby(by=["Year","Country"]).sum().reset_index()
                    oly_medal3=oly_medal3[oly_medal3["Year"]==y]

                df1=oly_medal3[(oly_medal3["Total"]>=1) & (oly_medal3["Gold"]==0)]
                df2=oly_medal3[(oly_medal3["Total"]>=1) & (oly_medal3["Silver"]==0)]
                df3=oly_medal3[(oly_medal3["Total"]>=1) & (oly_medal3["Bronze"]==0)]

                st.subheader("Countries Who never won a Gold Medal")
                st.write(df1)

                st.subheader("Countries Who never won a Silver Medal")
                st.write(df2)

                st.subheader("Countries Who never won a Bronze Medal")
                st.write(df3)

            elif add_game_type=="Asian games":
                add_year_type = st.sidebar.selectbox(
                    "Select the type of analysis you want:",
                    yr_a,
                )
                asian_medal=pd.read_csv("Medal_List_Asian.csv")
                asian_medal["Year"]=asian_medal["Year"].astype('int64')

                asian_medal2=asian_medal.drop(columns=["Sport","Rank"])
        
                if add_year_type=="All years":
                    asian_medal3=asian_medal2.groupby(by=["Year","Country"]).sum().reset_index()
                elif add_year_type=="Overall":
                    asian_medal3=asian_medal2.drop(columns=["Year"])
                    asian_medal3=asian_medal3.groupby(by=["Country"]).sum().reset_index()
                else:
                    y=int(add_year_type)
                    asian_medal3=asian_medal2.groupby(by=["Year","Country"]).sum().reset_index()
                    asian_medal3=asian_medal3[asian_medal3["Year"]==y]

                df_gold=asian_medal3[(asian_medal3["Total"]>=1) & (asian_medal3["Gold"]==0)]
                df_silver=asian_medal3[(asian_medal3["Total"]>=1) & (asian_medal3["Silver"]==0)]
                df_bronze=asian_medal3[(asian_medal3["Total"]>=1) & (asian_medal3["Bronze"]==0)]

                st.subheader("Countries Who never won a Gold Medal")
                st.write(df_gold)

                st.subheader("Countries Who never won a Silver Medal")
                st.write(df_silver)

                st.subheader("Countries Who never won a Bronze Medal")
                st.write(df_bronze)

            elif add_game_type=="Both":
                oly_medal=pd.read_csv("Medal_List_Olympics.csv")
                oly_medal=oly_medal.drop(columns=["Year","Host_City","Sport"])
                oly_medal=oly_medal.groupby(by=["Country"]).sum().reset_index()

                asian_medal=pd.read_csv("Medal_List_Asian.csv")
                asian_medal=asian_medal.drop(columns=["Year","Sport","Rank"])

                asian_medal=asian_medal.groupby(by=["Country"]).sum().reset_index()

                asia_olympic=pd.merge(asian_medal,oly_medal,on="Country",suffixes=('_Asian',"_Olympic"))

                gold_both=asia_olympic[(asia_olympic["Gold_Asian"]>=1) & (asia_olympic["Gold_Olympic"]>=1)]
                gold_both=gold_both[["Country","Gold_Asian","Gold_Olympic"]]

                st.subheader("Country won Gold in Both Asian and Olympics")
                st.write(gold_both)

                gold_asia=asia_olympic[(asia_olympic["Gold_Asian"]>=1) & (asia_olympic["Gold_Olympic"]==0)]
                gold_asia=gold_asia[["Country","Gold_Asian","Gold_Olympic"]]

                st.subheader("Country won Gold in Asian but not in Olympic")
                st.write(gold_asia)

                gold_olympic=asia_olympic[(asia_olympic["Gold_Asian"]==0) & (asia_olympic["Gold_Olympic"]>=1)]
                gold_olympic=gold_olympic[["Country","Gold_Asian","Gold_Olympic"]]

                st.subheader("Country won Gold in Olympic but not in Asian")
                st.write(gold_olympic)

        elif add_type_sub=="Player analysis":
            if add_game_type=="Olympic games":
         
                add_year_type = st.sidebar.selectbox(
                    "Select the year:",
                    yr_o,
                )
                add_country_type = st.sidebar.selectbox(
                    "Select the country:",
                    li_country,
                )
                oly_player=pd.read_csv("Players_Medal_list_Olympics.csv")
                sports=list(oly_player["Sport"].unique())
                sports.insert(0,"Overall")
                add_sport_type = st.sidebar.selectbox(
                    "Select the sport:",
                    sports,
                )

                  # Olympic Player and Medal data
                oly_player2=oly_player[oly_player["Sport_Type"]=="Individual"].drop(columns=["Host_City","Event","Sport_Type"])
                oly_player2["Total"]=oly_player2["Gold"]+oly_player2["Silver"]+oly_player2["Bronze"]

                if add_year_type=="All years":
                    oly_player3=oly_player2.groupby(by=["Year","Country","Sport","Gender","Name"]).sum().reset_index()
                elif add_year_type=="Overall":
                    oly_player3=oly_player2.drop(columns=["Year"])
                    oly_player3=oly_player3.groupby(by=["Country","Sport","Gender","Name"]).sum().reset_index()
                else:
                    y=int(add_year_type)
                    oly_player3=oly_player2.groupby(by=["Year","Country","Sport","Gender","Name"]).sum().reset_index()
                    oly_player3=oly_player3[oly_player3["Year"]==y]

                if add_country_type!="Overall":
                    oly_player3=oly_player3[oly_player3["Country"]==add_country_type]

                if add_sport_type!="Overall":
                    oly_player3=oly_player3[oly_player3["Sport"]==add_sport_type]


                df_gold=oly_player3[(oly_player3["Total"]>=1) & (oly_player3["Gold"]==0)]
                df_silver=oly_player3[(oly_player3["Total"]>=1) & (oly_player3["Silver"]==0)]
                df_bronze=oly_player3[(oly_player3["Total"]>=1) & (oly_player3["Bronze"]==0)]


                st.subheader("Players Who never won a Gold Medal")
                st.write(df_gold)

                st.subheader("Players Who never won a Silver Medal")
                st.write(df_silver)

                st.subheader("Players Who never won a Bronze Medal")
                st.write(df_bronze)

            elif add_game_type=="Asian games":
                add_year_type = st.sidebar.selectbox(
                    "Select the year:",
                    yr_a,
                )
                add_country_type = st.sidebar.selectbox(
                    "Select the country:",
                    li_country,
                )
                asian_player=pd.read_csv("Players_Medal_list_Asian.csv")
                sports=list(asian_player["Sport"].unique())
                sports.insert(0,"Overall")
                add_sport_type = st.sidebar.selectbox(
                    "Select the sport:",
                    sports,
                )

                  # Olympic Player and Medal data
                asian_player2=asian_player[asian_player["Sport_Type"]=="Single"].drop(columns=["Event","Sport_Type"])
                asian_player2["Total"]=asian_player2["Gold"]+asian_player2["Silver"]+asian_player2["Bronze"]

                if add_year_type=="All years":
                    asian_player3=asian_player2.groupby(by=["Year","Country","Sport","Gender","Player_Name"]).sum().reset_index()
                elif add_year_type=="Overall":
                    asian_player3=asian_player2.drop(columns=["Year"])
                    asian_player3=asian_player3.groupby(by=["Country","Sport","Gender","Player_Name"]).sum().reset_index()
                else:
                    y=int(add_year_type)
                    asian_player3=asian_player2.groupby(by=["Year","Country","Sport","Gender","Player_Name"]).sum().reset_index()
                    asian_player3=asian_player3[asian_player3["Year"]==y]

                if add_country_type!="Overall":
                    asian_player3=asian_player3[asian_player3["Country"]==add_country_type]

                if add_sport_type!="Overall":
                    asian_player3=asian_player3[asian_player3["Sport"]==add_sport_type]


                df_gold=asian_player3[(asian_player3["Total"]>=1) & (asian_player3["Gold"]==0)]
                df_silver=asian_player3[(asian_player3["Total"]>=1) & (asian_player3["Silver"]==0)]
                df_bronze=asian_player3[(asian_player3["Total"]>=1) & (asian_player3["Bronze"]==0)]


                st.subheader("Players Who never won a Gold Medal")
                st.write(df_gold)

                st.subheader("Players Who never won a Silver Medal")
                st.write(df_silver)



                st.subheader("Players Who never won a Bronze Medal")
                st.write(df_bronze)

            elif add_game_type=="Both":
                oly_player=pd.read_csv("Players_Medal_list_Olympics.csv")
                asian_player=pd.read_csv("Players_Medal_list_Asian.csv")
                oly_player=oly_player[oly_player["Sport_Type"]=="Individual"]
                asian_player=asian_player[asian_player["Sport_Type"]=="Single"]

                oly_player=oly_player.drop(columns=["Year","Host_City","Event","Sport_Type"])
                oly_player=oly_player.groupby(by=["Country","Sport","Gender","Name"]).sum().reset_index()

                asian_player=asian_player.drop(columns=["Year","Event","Sport_Type"])
                asian_player=asian_player.groupby(by=["Country","Sport","Gender","Player_Name"]).sum().reset_index()

                add_country_type = st.sidebar.selectbox(
                    "Select the country:",
                    li_country,
                )
                
                sports=list(oly_player["Sport"].unique())
                sports.insert(0,"Overall")
                add_sport_type = st.sidebar.selectbox(
                    "Select the sport:",
                    sports,
                )

                if add_country_type!="Overall":
                    asian_player=asian_player[asian_player["Country"]==add_country_type]
                    oly_player=oly_player[oly_player["Country"]==add_country_type]
                if add_sport_type!="Overall":
                    asian_player=asian_player[asian_player["Sport"]==add_sport_type]
                    oly_player=oly_player[oly_player["Sport"]==add_sport_type]

                asia_olympic=asian_player.merge(oly_player,left_on="Player_Name",right_on="Name",suffixes=('_Asian','_Olympic'))

                df1=asia_olympic[(asia_olympic["Gold_Asian"]>=1) & (asia_olympic["Gold_Olympic"]>=1)]
                df1=df1[["Player_Name","Country_Asian","Sport_Asian","Gender_Asian","Gold_Asian","Gold_Olympic"]]
                df1.columns=["Name","Country","Sport","Gender","Gold_Asian","Gold_Olympic"]

                df2=asia_olympic[(asia_olympic["Gold_Asian"]==0) & (asia_olympic["Gold_Olympic"]>=1)]
                df2=df2[["Player_Name","Country_Asian","Sport_Asian","Gender_Asian","Gold_Asian","Gold_Olympic"]]
                df2.columns=["Name","Country","Sport","Gender","Gold_Asian","Gold_Olympic"]

                df3=asia_olympic[(asia_olympic["Gold_Asian"]>=1) & (asia_olympic["Gold_Olympic"]==0)]
                df3=df3[["Player_Name","Country_Asian","Sport_Asian","Gender_Asian","Gold_Asian","Gold_Olympic"]]
                df3.columns=["Name","Country","Sport","Gender","Gold_Asian","Gold_Olympic"]

                st.subheader("Player won Gold Both in Asian and Olympic")
                st.write(df1)

                st.subheader("Player won Gold in Olympic but not in Asian")
                st.write(df2)



                st.subheader("Player won Gold in Asian but not in Olympic")
                st.write(df3)

elif add_type=="Detailed Analysis of India":
    add_game_type = st.sidebar.selectbox(
        "Select the type of analysis you want:",
        (
            "Olympic games",
            "Asian games",
        ),
    )

    with header:
        st.title(
            "Detailed Analysis of India"
        )
        st.text("In this section we try to find something like percentage of medals won by india in\nasian and olympic games, we can also find top n-players in india and top n-players\nin a particular year in both asian and olympic games,we can also find sportwise\nperformance of India and many such insights we can derive in this section.")

    with medals_tally:
        if add_game_type=="Olympic games":
            olympic_player=pd.read_csv("Players_Medal_list_Olympics.csv")
            olympic_medal=pd.read_csv("Medal_List_Olympics.csv")

            total=olympic_medal[olympic_medal["Country"]=="India"]["Total"].sum()
            gold=olympic_medal[olympic_medal["Country"]=="India"]["Gold"].sum()
            silver=olympic_medal[olympic_medal["Country"]=="India"]["Silver"].sum()
            bronze=olympic_medal[olympic_medal["Country"]=="India"]["Bronze"].sum()

            total_medal=olympic_medal["Total"].sum()
            total_gold=olympic_medal["Gold"].sum()
            total_silver=olympic_medal["Silver"].sum()
            total_bronze=olympic_medal["Bronze"].sum()


            t=(total/total_medal)*100
            g=(gold/total_gold)*100
            s=(silver/total_silver)*100
            b=(bronze/total_bronze)*100

            st.subheader("Percentage Medal Share")
            st.text(f"Percentage of Total Medal won : {round(t,2)}%")
            st.text(f"Percentage of Gold Medal won : {round(g,2)}%")
            st.text(f"Percentage of Silver Medal won : {round(s,2)}%")
            st.text(f"Percentage of Bronze Medal won : {round(b,2)}%")

            st.subheader("Total medal variation")
            total_o=helper.olympicTotalVariation(olympic_medal)
            st.pyplot(total_o)

            st.subheader("Gold/Silver/Bronze medal variation")
            gold_o=helper.olympicGoldVariation(olympic_medal)
            st.pyplot(gold_o)

            st.subheader("Sport-wise medal variation")
            sport_o=helper.olympicSportVariation(olympic_medal)
            st.pyplot(sport_o)

            top_player_oly=olympic_player[(olympic_player["Country"]=="India") & (olympic_player["Sport_Type"]=="Individual")][["Name","Year","Sport","Gender","Gold","Silver","Bronze"]]
            top_player_oly=top_player_oly.groupby(["Year","Sport","Gender","Name"]).sum().reset_index()
            top_player_oly["Total"]=top_player_oly["Gold"]+top_player_oly["Silver"]+top_player_oly["Bronze"]

            top_index=top_player_oly.groupby(["Year"])["Total"].nlargest(3).reset_index()
            top_index=top_index["level_1"].values

            olympic_top_player=top_player_oly.loc[top_index]
            olympic_top_player=olympic_top_player.reset_index(drop=True)

            st.subheader("Top 3 Players year wise")
            st.write(olympic_top_player)

            top_player_oly=olympic_player[(olympic_player["Country"]=="India") & (olympic_player["Sport_Type"]=="Individual")][["Sport","Name","Gender","Gold","Silver","Bronze"]]
            top_player_oly=top_player_oly.groupby(["Sport","Gender","Name"]).sum().reset_index()
            top_player_oly["Total"]=top_player_oly["Gold"]+top_player_oly["Silver"]+top_player_oly["Bronze"]

            olympic_top_player=top_player_oly.nlargest(5,columns=["Total"])
            olympic_top_player=olympic_top_player.sort_values(by=["Gold","Silver","Bronze"],ascending=False)

            st.subheader("Top 5 Players till now")
            st.write(olympic_top_player)

        elif add_game_type=="Asian games":
            asian_player=pd.read_csv("Players_Medal_List_Asian.csv")
            asian_medal=pd.read_csv("Medal_List_Asian.csv")

            total=asian_medal[asian_medal["Country"]=="India"]["Total"].sum()
            gold=asian_medal[asian_medal["Country"]=="India"]["Gold"].sum()
            silver=asian_medal[asian_medal["Country"]=="India"]["Silver"].sum()
            bronze=asian_medal[asian_medal["Country"]=="India"]["Bronze"].sum()

            total_medal=asian_medal["Total"].sum()
            total_gold=asian_medal["Gold"].sum()
            total_silver=asian_medal["Silver"].sum()
            total_bronze=asian_medal["Bronze"].sum()


            t=(total/total_medal)*100
            g=(gold/total_gold)*100
            s=(silver/total_silver)*100
            b=(bronze/total_bronze)*100

            st.subheader("Percentage Medal Share")
            st.text(f"Percentage of Total Medal won : {round(t,2)}%")
            st.text(f"Percentage of Gold Medal won : {round(g,2)}%")
            st.text(f"Percentage of Silver Medal won : {round(s,2)}%")
            st.text(f"Percentage of Bronze Medal won : {round(b,2)}%")

            st.subheader("Total medal variation")
            total_a=helper.asianTotalVariation(asian_medal)
            st.pyplot(total_a)

            st.subheader("Gold/Silver/Bronze medal variation")
            gold_a=helper.asianGoldVariation(asian_medal)
            st.pyplot(gold_a)

            st.subheader("Sport-wise medal variation")
            sport_a=helper.asianSportVariation(asian_medal)
            st.pyplot(sport_a)

            top_player=asian_player[(asian_player["Country"]=="India") & (asian_player["Sport_Type"]=="Single")][["Player_Name","Year","Sport","Gender","Gold","Silver","Bronze"]]
            top_player=top_player.groupby(["Year","Sport",'Gender',"Player_Name"]).sum().reset_index()
            top_player["Total"]=top_player["Gold"]+top_player["Silver"]+top_player["Bronze"]

            top_index=top_player.groupby(["Year"])["Total"].nlargest(3).reset_index()
            top_index=top_index["level_1"].values

            asian_top_player=top_player.loc[top_index]
            asian_top_player=asian_top_player.reset_index(drop=True)

            st.subheader("Top 3 Players year wise")
            st.write(asian_top_player)

            top_player_asia=asian_player[(asian_player["Country"]=="India") & (asian_player["Sport_Type"]=="Single")][["Sport","Player_Name","Gender","Gold","Silver","Bronze"]]
            top_player_asia=top_player_asia.groupby(["Sport","Gender","Player_Name"]).sum().reset_index()
            top_player_asia["Total"]=top_player_asia["Gold"]+top_player_asia["Silver"]+top_player_asia["Bronze"]

            asian_top_player=top_player_asia.nlargest(5,columns=["Total"])
            asian_top_player=asian_top_player.sort_values(by=["Gold","Silver","Bronze"],ascending=False)

            st.subheader("Top 5 Players till now")
            st.write(asian_top_player)

elif add_type=='Countries winning atleast 1 medal in every sport in a year':
	select_criteria=st.sidebar.selectbox("Select the type of analysis:",
									  ['Overall','Year-wise'])
	if select_criteria=="Overall":
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Countries winning atleast 1 medal in every sport in a year analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year')
				out=helper.Atleast_one(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')

		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year')
				out=helper.Atleast_one(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year:')
				out1,out2=helper.Atleast_one(add_sidebar)
				st.write(out1)
				st.write(out2)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')
	elif select_criteria=="Year-wise":
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Countries winning atleast 1 medal in every sport in a year analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year')
				out=helper.Atleast_one_country(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')
		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year')
				out=helper.Atleast_one_country(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries winning atleast 1 medal in every sport in a year:')
				out1,out2=helper.Atleast_one_country(add_sidebar)
				st.write(out1)
				st.write(out2)
				st.subheader('This table contains information about number of sports organized in any particular year. Also, it contains percentage of medal won sportswise. It is calculated by dividing total sports events in which a particular country won atleast 1 medal  by total sports events held in that particular year.')
elif add_type=='Recession year for a country':
	select_criteria=st.sidebar.selectbox("Select the type of analysis:",
									  ['Recession Years','Booming Years'])
	if select_criteria=="Recession Years":
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Countries winning atleast 1 medal in every sport in a year analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries Recession years in which its medal winning rate decreased over time:')
				out=helper.find_recession_years(add_sidebar)
				st.subheader('Table:')
				st.write(out)

		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Countries Recession years in which its medal winning rate decreased over time:')
				out=helper.find_recession_years(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries Recession years in which its medal winning rate decreased over time:')
				out1,out2=helper.find_recession_years(add_sidebar)
				st.subheader('Asian Games')
				st.write(out1)
				st.subheader('Olympic Games')
				st.write(out2)

	elif select_criteria=="Booming Years":
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Asian Games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries Booming years in which its medal winning rate increased over time:')
				out=helper.find_boom_years(add_sidebar)
				st.subheader('Table:')
				st.write(out)

		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Countries Booming years in which its medal winning rate increased over time:')
				out=helper.find_boom_years(add_sidebar)
				st.subheader('Table:')
				st.write(out)
				
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Countries Booming years in which its medal winning rate increased over time:')
				out1,out2=helper.find_boom_years(add_sidebar)
				st.subheader('Asian Games')
				st.write(out1)
				st.subheader('Olympic Games')
				st.write(out2)

elif add_type=='Year(sport) in which country won minimum(maximum) medals':
	type=st.sidebar.selectbox("Select the medal type:",
									  ['Best Year','Best Sport'])
	medal_type=st.sidebar.selectbox("Select the medal type:",
									  medals)
	if type=='Best Year':
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Asian Games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Best performing year for any country on the basis of medal type selected:')
				out=helper.find_best_year(add_sidebar,medal_type)
				st.subheader('Table:')
				st.write(out)

		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Best performing year for any country on the basis of medal type selected:')
				out=helper.find_best_year(add_sidebar,medal_type)
				st.subheader('Table:')
				st.write(out)
				
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Best performing year for any country on the basis of medal type selected:')
				out1,out2=helper.find_best_year(add_sidebar,medal_type)
				st.subheader('Asian Games')
				st.write(out1)
				st.subheader('Olympic Games')
				st.write(out2)

	elif type=='Best Sport':
		if add_sidebar=='Home Page':
			with header:
				st.title('Welcome to our project')
				st.text('This project contains detailed analysis of performance of Asian countries in Olympic\n games and Asian games.')
			st.image('Homepage.jpg')
		elif add_sidebar=='Asian Games':
			with header:
				st.title('Welcome to our Asian Games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Best performing sport for any country on the basis of medal type selected:')
				out=helper.find_best_sport(add_sidebar,medal_type)
				st.subheader('Table:')
				st.write(out)

		elif add_sidebar=='Olympic Games':
			with header:
				st.title('Welcome to our Olympics games analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			with medals_tally:
				st.header('Best performing sport for any country on the basis of medal type selected:')
				out=helper.find_best_sport(add_sidebar,medal_type)
				st.subheader('Table:')
				st.write(out)
				
		elif add_sidebar=='Both':
			with header:
				st.title('Welcome to our comparative analysis page:')
				st.text('In this project, we analysed performance of \nasian countries in Olympic games and Asian games.')
			
			
			with medals_tally:
				st.header('Best performing sport for any country on the basis of medal type selected:')
				out1,out2=helper.find_best_sport(add_sidebar,medal_type)
				st.subheader('Asian Games')
				st.write(out1)
				st.subheader('Olympic Games')
				st.write(out2)


