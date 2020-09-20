import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label,Button,Grid,mainloop

root = Tk()
root.configure(bg='blue')

def get_data(data):
    # global team1,team2,team1_score,team2_score
    team1, team2, team1_score, team2_score = data
    url='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    team_1 = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
    team_2 = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()

    team_1_score = soup.find_all(class_='cb-ovr-flo')[8].get_text()
    team_2_score = soup.find_all(class_='cb-ovr-flo')[10].get_text()
    team1.config(text=team_1)
    team2.config(text=team_2)
    team1_score.config(text=team_1_score)
    team2_score.config(text=team_2_score)

a = Label(text='IPL 2020 live score',font='arial 8')
a.grid(row=0,columnspan=2,pady=5)
team1 = Label(text='Team 1',font='arial 20')
team1.grid(row=1, column=0)
team2 = Label(text='Team 2',font='arial 20')
team2.grid(row=1,column=1)

team1_score= Label(root,text='hit refresh',font='arial 20')
team1_score.grid(row=2,column=0,padx=5)
team2_score= Label(text='hit refresh',font='arial 20')
team2_score.grid(row=2 , column=1,padx=5)
data = [team1,team2,team1_score,team2_score]
refresh = Button(text='Refresh',command=get_data(data),bg='orange')
refresh.grid(row=3, columnspan=2)

root.mainloop()
