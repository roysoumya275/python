from google import genai
client = genai.Client(api_key="AQ.Ab8RN6LXdE99Cz49h9Q0bVbYZMGn5npuzwEEpbMSuM953Zf41g")
models = client.models.list()
for m in models:
    print(m)