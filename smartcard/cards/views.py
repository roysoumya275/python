from django.shortcuts import render,redirect,get_object_or_404
from google import genai
# Create your views here.
from .models import SmartCard
from .forms import SmartCardForm
client = genai.Client(api_key="AQ.Ab8RN6LXdE99Cz49h9Q0bVbYZMGn5npuzwEEpbMSuM953Zf41g")
def add_card(request):
    if request.method == "POST":
        form = SmartCardForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = SmartCardForm()

    return render(request, 'add.html', {'form': form})


def card_list(request):
    cards = SmartCard.objects.all()
    return render(request, 'list.html', {'cards': cards})


# EDIT CARD
def edit_card(request, id):
    card = get_object_or_404(SmartCard, id=id)

    if request.method == "POST":
        form = SmartCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = SmartCardForm(instance=card)

    return render(request, 'edit.html', {'form': form})


# DELETE CARD
def delete_card(request, id):
    card = get_object_or_404(SmartCard, id=id)

    if request.method == "POST":
        card.delete()
        return redirect('card_list')

    return render(request, 'delete.html', {'card': card})


def search(query):
    cards = SmartCard.objects.all()
    data = "\n".join([
        f"Name: {s.name}, Card Number: {s.card_number}, Balance: {s.balance}"
        for s in cards
    ])
    prompt = f"""
    Database Records:
    {data}
    User Search:
    {query}
    Return matching records only.
    """
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    


def search_view(request):
    result = ""
    if request.method == "POST":
        query = request.POST.get("query")
        result = search(query)

    return render(
        request,
        "search.html",
        {"result": result}
    )