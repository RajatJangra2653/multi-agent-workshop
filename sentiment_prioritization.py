from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def prioritize_task(task_description):
    client = TextAnalyticsClient(endpoint="<Your_Text_Analytics_Endpoint>", credential=AzureKeyCredential("<Your_Key>"))
    sentiment = client.analyze_sentiment(documents=[task_description])[0].sentiment
    priority = 'High' if sentiment == 'negative' else 'Normal'
    return priority