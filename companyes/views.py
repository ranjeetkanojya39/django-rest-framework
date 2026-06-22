from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home response")
    frinds = [
        "Ankit",
        "Alok",
        "Ashok",
        'ankt'
    ]
    return JsonResponse({"friends": frinds})