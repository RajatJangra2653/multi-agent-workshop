import autogen
from reminder_agent import reminder_agent
from notes_agent import notes_agent

user_proxy = autogen.UserProxyAgent("user", human_input_mode="TERMINATE", llm_config={})
user_proxy.initiate_chat(reminder_agent, message="Remind me to submit the project report by 6 PM today.")