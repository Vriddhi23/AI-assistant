import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email to boss for registration"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "id": "chatcmpl-7ikmMRL5gBTzzRwZPBuOffAt6L07h",
  "object": "chat.completion",
  "created": 1690900606,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Dear [Boss's Name],\n\nI hope this email finds you well. I am writing to request your approval and support for my upcoming registration for a professional training event.\n\nThe event, [Event Name], is scheduled to take place on [Event Date(s)] at [Event Location]. It specifically focuses on [topic(s) of the event] which directly relates to my current role and responsibilities at the company. Attending this training will not only enhance my existing skills but also equip me with the latest industry knowledge, enabling me to contribute more effectively to our team and overall company goals.\n\nI have extensively researched this training and received positive feedback from colleagues who have attended in the past. The event agenda encompasses a wide range of relevant workshops, expert panels, and networking opportunities that are invaluable for professional growth. Furthermore, it brings together industry leaders and experts, providing a platform for learning from their experiences and best practices.\n\nIn terms of logistics, the event registration fee is [Registration Fee] which covers all necessary materials, sessions, and access to networking events. I have also taken into consideration travel expenses and accommodation, ensuring that I stay within our allocated budget for professional development activities.\n\nI am confident that the knowledge gained from attending this event will contribute significantly to my performance and productivity in my role."
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 256,
    "total_tokens": 270
  }
}
'''