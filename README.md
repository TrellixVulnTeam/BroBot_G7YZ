BroBot is our Final Year Project for Fall 2020. It's an interactive chatbot able to have somewhat contextual
conversations with the user and store information using forms and then give recommendations based on preferences
and mood.

In order to run the Rasa backend server:
0. Clone Project
1. Activate python virtual env inside Backend/BroBots/BroBot v1
	virtualenv venv
	venv/Scripts/activate
2. Install rasa
	pip install rasa[full]
3. Go to dir: chatbot
	cd chatbot
4. Activate Server
	rasa run
