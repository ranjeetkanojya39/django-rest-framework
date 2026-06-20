from django.http import HttpResponse, JsonResponse

def home(request):
    print("home response")
    frinds = [
        "Ankit",
        "Alok",
        "Ashok"
    ]
    return JsonResponse({"friends": frinds})