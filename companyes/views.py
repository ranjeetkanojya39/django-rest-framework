from django.http import HttpResponse, JsonResponse

def home(request):
    print("home response")
    frinds = [
        "Ankit",
        "Alok",
        "Ashok",
        'ankt'
    ]
    return JsonResponse({"friends": frinds})