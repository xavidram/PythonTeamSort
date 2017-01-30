# PythonTeamSort

###Purpose of the project:###
I am part of a League of Legends club down in South Texas.
The club hosts various tournaments for the members where they complete in a solo queue style 5v5 match making.
The problem is that RIOT does not provide any sort of team sorter. Before, the club allowed premaid teams to form
and complete together. The issue is that Teams with all Diamond players would wipe the tournament since it is open to players
of all ranks. In order to solve this, I was asked to develop a team sorter that will grab all the users, with their mmr, and form
teams of near even total MMR.

###Issue with the project:###
######I know I break a couple of RIOT's Policies when using their API's to develop something. ######
1. Scrape data from undocumented endpoints or any other sources outside of the provided Riot API Endpoints and other documented Third Party Developer Tools. (Except where otherwise noted in any official exceptions, if any.)

* Even though I could have manually gotten ever users mmr from either OP.GG or another MMR calculating site. 
Just the fact that I would rather automate the process than have to take the time and constantly search for users mmr was too tedious.
I build a scrapper with BeautifulSoup for Python to pull the players mmr from their user profile on the site. As this is not a "correct"
mmr calculation, I went with the numbers either was as they are the most reasonable. This allowed me to sort players based on MMR value.

2. Create alternatives for official skill ranking systems, such as Ranked Leagues (Prohibited alternatives include MMR or ELO calculators)

* This project gives each user an MMR value based on what is scrapped off OP.GG which in its case also breaks RIOTS Policies but I assume has an agreement with.
It is only used to sort the players and put them into teams where they should have an even advantage against other teams, allowing for a much more lasting and thrilling tournament.

### Use of the Python Application ###
######I wrote the application with Python 3.5######
1. Download or clone the Repo and open up the RIOTAPI.py file in a editor, paste your own Riot API key into the variable listed.
2. Under Players.txt, input vertically all the players that will be competing.
3. OPGG.py will scrape the site for the highest MMR for that player, whether it is the current MMR or past season MMR and return the highest.
4. Players.py will create the teams and sort them, any extra players, in the event there are more players than possible teams (players / 5 = teamnumber), will be stored as extras.
5. main.py will run the application and give you some feed back.

### Terms of Use ###
##### Please use this at your own discretion. This was made for education purposes as well as necesarry purposes. You can use this, but not sell as specified in RIOTS Policies, and expand on it if you wish. I know some of my code may be very robust and overcomplicated but this is my first draft of the project on a quick notice.#####
