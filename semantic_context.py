import semantic_kernel as sk

kernel = sk.Kernel()
kernel.add_text_completion_service("openai", sk.openai.AzureChatCompletion(
    api_key=os.getenv('AZURE_OPENAI_KEY'),
    endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
))