from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from django.views.decorators.http import require_POST
import json

# Create your views here.
# add here to your generated API key
genai.configure(api_key="AIzaSyB_PhVDJSNpDZMhnt4RdfdtLGDBwgMnvaU")


@require_POST
def my_ajax_function(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['request']
        print(f"Extracted {content} request data")

        #text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        chat = model.start_chat()
        
        response = chat.send_message(content)
        
        print(f"Response {response.text} request data")
        # Extract necessary data from response
        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
        }
        return JsonResponse({"data": response.text})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )  # Redirect to chat page for GET requests

@login_required
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chat_bot.html", {"chats": chats})