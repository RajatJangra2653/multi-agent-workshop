import autogen

reminder_agent = autogen.AssistantAgent("ReminderAgent", llm_config={"api_key": os.getenv('AZURE_OPENAI_KEY'), "endpoint": os.getenv('AZURE_OPENAI_ENDPOINT')})