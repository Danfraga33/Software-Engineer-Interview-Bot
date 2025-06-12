# functions/database.py - Make sure this function exists and works correctly

def get_recent_messages():
    """
    This function should return a list of recent messages in the format:
    [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
        {"role": "user", "content": "How are you?"}
    ]
    """
    try:
        # Replace this with your actual database logic
        # For now, return a basic system message if no messages exist
        messages = []
        
        # Add your database retrieval logic here
        # Example:
        # messages = retrieve_messages_from_database()
        
        # If no messages, start with a system message
        if not messages:
            messages = [
                {
                    "role": "system", 
                    "content": "Your name is Sarah, you are a helpful AI assistant conducting a software engineering interview."
                }
            ]
        
        print(f"Retrieved {len(messages)} messages from database")
        return messages
        
    except Exception as e:
        print(f"Error getting recent messages: {e}")
        # Return default system message on error
        return [
            {
                "role": "system", 
                "content": "You are a helpful AI assistant conducting a software engineering interview."
            }
        ]

def store_messages(user_message, assistant_message):
    """Store the conversation messages in database"""
    try:
        # Add your database storage logic here
        print(f"Storing messages - User: {user_message[:50]}...")
        print(f"Storing messages - Assistant: {assistant_message[:50]}...")
        
        # Your database storage code here
        # Example:
        # save_to_database(user_message, assistant_message)
        
        return True
    except Exception as e:
        print(f"Error storing messages: {e}")
        return False

def resetMessages():
    """Reset/clear all messages from database"""
    try:
        # Add your database reset logic here
        print("Resetting conversation messages")
        
        # Your database reset code here
        # Example:
        # clear_database_messages()
        
        return True
    except Exception as e:
        print(f"Error resetting messages: {e}")
        return False