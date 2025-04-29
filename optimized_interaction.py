import autogen

manager = autogen.GroupChatManager()
group_chat = autogen.GroupChat(agents=[reminder_agent, notes_agent, schedule_agent], messages=[])
manager.manage(group_chat)