# gpt-prompts

This is a simple Flask project that demonstrates how to create a chatbot using the OpenAI API and the GPT-3.5 language model.

Prerequisites
Before you begin, 
- You must have a valid OpenAI API key. If not, you can sign up for one on the OpenAI website.
- Python 3.9 or later is installed.
- Clone Project and change to working directory.
- Install the required Python packages using pip:    
	pip install -r requirements.txt
- Place your OpenAI API key to .env file 
- Run the project using:     
	python app.py



POSTMAN COLLECTION LINK:				
	
https://api.postman.com/collections/29086855-36b87c59-2c72-4d7e-9489-19d9ef79d516?access_key=PMAT-01H91D2YGAQPVFJ6V595GNG3M1



Given Below are the URL for the Project
- GET {BaseUrl}/prompts

				
- POST {BaseUrl}/prompts			
	json data :
	{
 	   "prompt_text":"explain solar technology "
	}			

				
- PATCH {BaseUrl}/prompts/{promptID}		
	json data :
	{
 	   "new_prompt":"explain solar technology "
	}			

					
- DELETE {BaseUrl}/prompts/{promptID}			

						
- GET {BaseUrl}/prompts/{promptID}/generate
