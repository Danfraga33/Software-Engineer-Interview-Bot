import json
import random

# Get Recent Messages
def get_recent_messages():
   # Define the file name and learn instructions
      file_name = 'stored_data.json'
      learn_instruction = {
            'role':'system',
            'content':'You are interviewing the user for a job as a software developer. Ask short questions that are relevant to the job. Your name is Rachel. The user is called Daniel. Keep your answers to under 100 words.'
      }

   # initialize messages
      messages = []

      x = random.uniform(0,1) 
      if x < 0.5: 
           learn_instruction["content"] = learn_instruction["content"] + 'Your response will include some dry humour'
      else:  
           learn_instruction["content"] = learn_instruction["content"] + 'Your response will include a rather challenging question'

      messages.append(learn_instruction)
      
      # Get last messages
      try: 
           with open(file_name) as user_file:
                data = json.load(user_file)
           
         #   Append last 5 items of data
                if data:
                  if len(data) < 5:
                     for item in data:
                      messages.append(item)
                  else: 
                     for item in data: 
                           messages.append[-5]   
      except Exception as e:
           print(e)
           pass
# return messages
      return messages   


#store_messages
def store_messages(request_message, response_message):
   
   #  Define the file name
   file_name = "stored_data.json"

   # Get Recent Messages
   messages = get_recent_messages()[1:]

   # Add Messages to data
   user_messages = {'role': "user","content": request_message}
   assistant_messages = {'role': "assistant","content": response_message}
   messages.append(user_messages)
   messages.append(assistant_messages)

   # Save the updated file
   with open(file_name, "w") as f:
      json.dump(messages, f)


   # Reset Messages
def resetMessages():


   # Overwrite current file with nothing 
   open('stored_data.json', "w") 