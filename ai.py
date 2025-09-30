# Mental Health Support Chatbot
# Created by: [Your Name] and [Partner's Name]
# Group Project - Basic Chatbot Creation

def mental_health_bot():
    print("=" * 50)
    print("    🌈 MENTAL HEALTH SUPPORT BOT 🌈")
    print("=" * 50)
    print("I'm here to listen and provide support.")
    print("Type 'quit' to end the conversation")
    print("-" * 50)
    
    while True:
        user_input = input("\nHow are you feeling? ").lower().strip()
        
        # Exit condition
        if user_input == 'quit':
            print("Take care of yourself! 💙")
            break
            
        # 1. Stress
        elif 'stress' in user_input:
            print("Try deep breathing: 4 seconds in, 6 seconds out. Break tasks into small steps.")
            
        # 2. Anxiety
        elif 'anxious' in user_input or 'worry' in user_input:
            print("Practice grounding: Name 5 things you can see around you right now.")
            
        # 3. Sadness
        elif 'sad' in user_input or 'depressed' in user_input:
            print("Your feelings are valid. Try talking to a friend or doing one small nice thing for yourself.")
            
        # 4. Sleep problems
        elif 'sleep' in user_input or 'tired' in user_input:
            print("Create a bedtime routine: No screens 1 hour before bed, try reading or gentle music.")
            
        # 5. Anger
        elif 'angry' in user_input or 'mad' in user_input:
            print("Take a timeout. Count to 10 slowly. Go for a short walk if possible.")
            
        # 6. Loneliness
        elif 'lonely' in user_input or 'alone' in user_input:
            print("Consider joining online communities or reaching out to old friends. You matter.")
            
        # 7. Overwhelmed
        elif 'overwhelmed' in user_input:
            print("Make a priority list. Focus on just one thing at a time. You don't have to do everything at once.")
            
        # 8. Motivation
        elif 'motivation' in user_input or 'lazy' in user_input:
            print("Start with a 5-minute task. Often starting is the hardest part. Celebrate small wins!")
            
        # 9. Panic
        elif 'panic' in user_input or 'attack' in user_input:
            print("Focus on your breathing. Sit down if needed. This will pass. You're safe.")
            
        # 10. Default response
        else:
            print("Thank you for sharing. Remember to be kind to yourself today. Would you like to talk more about it?")

# Start the chatbot
if __name__ == "__main__":
    mental_health_bot()