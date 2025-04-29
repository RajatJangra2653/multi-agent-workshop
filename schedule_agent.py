import autogen

schedule_agent = autogen.AssistantAgent("ScheduleAgent", llm_config={"api_key": os.getenv('AZURE_OPENAI_KEY'), "endpoint": os.getenv('AZURE_OPENAI_ENDPOINT')})