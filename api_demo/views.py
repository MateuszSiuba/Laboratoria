from django.shortcuts import render
from django.http import JsonResponse

# To jest nasz widok API
def greet(request):
    # Pobieramy parametr 'name' z adresu URL, domyślnie 'Anon'
    name = request.GET.get("name", "Anon")
    # Zwracamy odpowiedź w formacie JSON (nie HTML!)
    return JsonResponse({"message": f"Hello, {name}!"})

# To jest widok dla strony HTML, gdzie będzie formularz
def index(request):
    return render(request, 'api_demo/index.html')