# Login view for user authentication using Django's built-in authentication system
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.utils import translation
from .gtrans import translate_text
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        #return render(request, 'login.html',{'LANGUAGE_CODE': translation.get_language()})
        #login(request, user)
            #return redirect('home')  # Change 'home' to your homepage URL name
        return redirect('home_page')
    else:
        return render(request, 'login.html',{'LANGUAGE_CODE': translation.get_language()})

def get_visible_texts(soup):
    # Remove script and style elements
    for script in soup(['script', 'style']):
        script.decompose()
    # Get all text, strip whitespace, and filter out empty strings
    texts = [t.strip() for t in soup.stripped_strings if t.strip()]
    return texts

def home_page(request):
    with open('/Users/kush/Desktop/db_finsrv/fin_app/templates/home_page_en.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    texts = get_visible_texts(soup)
    translated_texts = {}
    i = 0
    # Save to a file
    output_path = 'extracted_texts.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in texts:
            if ('{' not in line):
                f.write(line + '\n')
        for line in texts:
            if ('{' not in line):
                translated_texts[i] = line
                i += 1
    with open(output_path, 'a', encoding='utf-8') as f:
        for key, value in translated_texts.items():
            f.write(str(key) + '\n')
            f.write(str(value) + '\n')
    print(f"Extracted {len(texts)} lines of text to {output_path}")
    content = translated_texts
    page_lang = translation.get_language()
    if page_lang != 'en':
        for key,value in content.items():
            content[key] = translate_text(value, page_lang)
            #print('Language: ', translation.get_language())
            #print(GoogleTranslator(source='auto', target='hi').translate(value))
        return render(request, 'home_page.html',{'content': content, 'lang': page_lang})
    return render(request, 'home_page_en.html')    

def get_investments(request):
    return render(request, 'get_investments.html', {})    

def compute_plans(request):
    if request.method == "POST":
        savings = request.POST.get('savings')
        print("Received savings:", savings)
        request.session['savings'] = savings
    if 'savings' in request.session:
        savings = request.session['savings']
    else:
        savings = -1
    return render(request, 'compute_plans.html', {'savings': savings})