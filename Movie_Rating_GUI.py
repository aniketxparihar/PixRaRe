import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import requests
from bs4 import BeautifulSoup


def Movie_Rating(inp):
	print()
	Movie_Content=""
	Movie_Content+="\n"
    #request the IMDB Movie search Page content
	page= requests.get("https://www.imdb.com/find?q="+inp+"&ref_=nv_sr_sm")  
	soup = BeautifulSoup(page.content,'html.parser')   
    
        
    #Fetch the Link to IMDB Movie Page
	soup=soup.find(class_='result_text').find('a').get('href')
    
    
    #IMDB Movie page Link
	imdb_movie_link="https://www.imdb.com/"+soup
 
    #Fetch Movie Page Content
	imdbpage=requests.get(imdb_movie_link)
	soup=BeautifulSoup(imdbpage.content,'html.parser')
    #movie_name
	Correct_Name = soup.find(class_="title_wrapper").find_all('h1')[0].getText().strip()
	print(Correct_Name+"\n")
	Movie_Content+=Correct_Name+"\n\n"

	#Fetch the Rating 
	Rating= soup.find(class_="ratingValue")
	if(Rating==None):
		Movie_Content+="Not Rated\n\n"
		print("Not Rated\n")
	else:
		movie_rating = Rating.find('span').getText()
		#print(find_rating_class.prettify())
		Movie_Content+="Rating : "+movie_rating+"/10\n\n"
		print("Rating : "+movie_rating+"/10\n")

	#Genre of the Movie
	Genre = soup.find(class_="subtext").find_all('a')
	#print(type(Genre))
	#print(len(Genre))
	Movie_Content+=("Genre : ")
	print("Genre :",end=" ")
	for index in range(0,len(Genre)-1): 
		Movie_Content+=(Genre[index].getText()+" , ")
		print(Genre[index].getText(),end=" , ")
	Movie_Content+="\n\n"	
	print("\n")
	#release year and date
	#release_year = soup.find(id="titleYear").find('a').getText()
	#print("Release Year : "+release_year)
	Movie_Content+= ("Release date : "+Genre[len(Genre)-1].getText().strip()+"\n\n")
	print("Release date : "+Genre[len(Genre)-1].getText().strip()+"\n")

	if(soup.find(class_="subtext").find_all('time')==[]):
		Movie_Content+="Time duration not avialable yet.\n\n"
		print("Time duration not avialable yet.\n")
	else:
		Run_Time = soup.find(class_="subtext").find_all('time')[0].getText().strip()
		Movie_Content+="Time Duration : "+Run_Time+"\n\n"
		print("Time Duration : "+Run_Time+"\n")
  
	#Gist of the Movie
	Movie_Content+=" Gist: "
	print("Gist :",end=" ")
	Gist= soup.find(class_="summary_text").getText().strip()
	print(Gist+"\n\n")
	Movie_Content+=Gist+"\n\n"


	#fetch director , writers and cast
	if(soup.find(class_="credit_summary_item").find('a')==None):
		Movie_Content+="Director data not avialable\n\n"
		print("Director data not avialable\n")
	else:	
		director_name = soup.find(class_="credit_summary_item").find('a').getText().strip()
		Movie_Content+="Director : "+director_name+"\n\n"
		print("Director : "+director_name+"\n")


	if(len(soup.find_all(class_="credit_summary_item")) < 2):
		Movie_Content+="Writers data not avialable\n\n"
		print("Writers data not avialable\n")
	else:		
		writers = soup.find_all(class_="credit_summary_item")[1].find_all('a')
		Movie_Content+="\nWriters : "
		print("Writers :",end=" ")
		for index in writers:
			Movie_Content+=index.getText().strip()+" , "
			print(index.getText().strip(), end=" , ")
		Movie_Content+="\n \n"	
		print('\n')
	if(len(soup.find_all(class_="credit_summary_item")) < 3):
		Movie_Content+="StarCast data not avialable\n\n"
		print("StarCast data not avialable\n")
	else:		
		starcast_names = soup.find_all(class_="credit_summary_item")[2].find_all('a')
		Movie_Content+="StarCast : "
		print("StarCast :",end=" ")
		for names in starcast_names:
			Movie_Content+=names.getText().strip()+" , "
			print(names.getText().strip(), end=" , ")

		Movie_Content+="\n\n"	
		print('\n')
		
		return Movie_Content



#Tkinter GUI Part
window = tk.Tk()
message=tk.Label(text="Hey Movie Lover,Bonjour!",foreground="white",  # Set the text color to white
background="black",width=30 )
message2=tk.Label(text="Search a Movie Name",foreground="white",  # Set the text color to white
background="black",width=30)
message.pack()
message2.pack()
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Movie Name?:")

Content=Movie_Rating(USER_INP)
tkinter.messagebox.showinfo("Result",Content)
window.mainloop()


