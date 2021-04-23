BroBot uses AI and Natural Language Processing (NLP) techniques to learn from therapeutic 
conversations to provide sympathetic encounters that are psychologically related. Our app in its 
essence is an interactive, contextual, and AI-assisted chatbot that simulates supportive 
conversation and encourages authentic disclosure and makes therapy readily accessible. The user 
creates an account to gain access to our app’s features like personalized recommendations, 
emotional state/history as well as individual context.
Features include:
- Users will be able to view dynamic mood/emotional history represented as a graph.
- Users will be able to benefit from personalized recommendations based on user preferences and 
context.
- Users will be able to enjoy and feel better with light but engaging conversations with our smart 
therapeutic chatbot.
- Users will be allowed to use text as well as voice as input for the chatbot.
- Users can write a journal about their day which will help model with recommendations and 
mood History.


0. Clone Project

Steps for setting up backend:

1. Run Django Backend
	* Sub cd Backend/Server/Django-server/Brobot
	* Sub Activate python virtual env
		* Sub virtualenv venv
		* Sub venv/Scripts/activate
	* Sub Install Django
		* Sub python -m pip install Django
	* Sub Install django-rest
		* Sub pip install djangorestframework
		* Sub pip install markdown       # Markdown support for the browsable API.
		* Sub pip install django-filter  # Filtering support
	* Sub Start django server
		* Sub python manage.py runserver <ip>:<port>
		
2. Run Dialogue Management Server
	* Sub cd Backend/DialogueManagement/BroBot_Gpt
	* Sub Activate python virtualenv
		* Sub virtualenv venv 
		* Sub venv/Scripts/activate
	* Sub Install rasa
		* Sub pip install rasa[full]
	* Sub cd chatbot -> Activate Server => a. rasa run actions b. rasa run
	* Sub Alternatively, after installing rasa, you can use bat files to run
		* Sub double_click: rasa_run_actions.bat
		* Sub double_click: rasa_run.bat

3.	Run Conversational AI Server:
	* Sub cd Backend/Server/Chitchat-Server/counsel-chat-server
	* Sub You can use bat files to run.
		* Sub double_click: command_for_interaction.bat
	
