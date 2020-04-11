from django.shortcuts import render, redirect
from .models import Club, Feedback
from .forms import FeedbackModelForm

def clubs_list(request):
    clubs = Club.objects.all().order_by('-grade')
    return render(request, 'scqf/clubs_list.html', {'clubs': clubs, 'username': request.user.username})


def club(request, identify):
    feedback_inst = Feedback()
    club = Club.objects.get(pk=identify)
    if request.method == 'POST':
        form = FeedbackModelForm(request.POST)

        feedback_inst.author = request.user.username
        feedback_inst.text = form.data['text']
        feedback_inst.grade = str(6 - int(form.data['grade']))
        feedback_inst.club_id = identify

        # update feedback rating
        count = Feedback.objects.filter(club_id=identify).count()
        new_rating = ((club.grade * count) + int(feedback_inst.grade)) / (count + 1)
        club.grade = round(new_rating, 1)
        club.save()

        feedback_inst.save()
        form = FeedbackModelForm()
        return redirect(request.path_info)
    else:
        form = FeedbackModelForm()
    feedbacks = Feedback.objects.filter(club_id=identify)
    print(feedbacks)
    return render(request, 'scqf/club.html', {'club': club, 'form': form, 'feedbacks': feedbacks, 'username': request.user.username})
