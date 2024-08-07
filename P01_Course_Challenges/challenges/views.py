from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for 20 minutes everyday!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for atleast 20 minutes every day!",
    "june": "Learn Django for 20 minutes everyday!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atleast 20 minutes every day!",
    "september": None,
    "october": "Eat no meat for the entire month!",
    "november": "Walk for atleast 20 minutes every day!",
    "december": "Learn Django for 20 minutes everyday!",
}

def index(request):
    # list_items=""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     month_capitlaized = month.capitalize()
    #     month_path = reverse("month-urlname", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month_capitlaized}</a></li>"
    #     response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_c_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("ERROR: There is no such month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-urlname", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        challenge_text = monthly_challenges.get(month)
        # response_data = f"<h1>Challenge for {month}: {challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "html_title": f"{month.capitalize()}'s Challenge",
            "html_h1": f"This is {month.capitalize()}'s Challenge:"
        })
    else:
        return HttpResponseNotFound("<h1>ERROR404: THERE IS NO SUCH PAGE</h1>")
