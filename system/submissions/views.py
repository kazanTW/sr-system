from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .models import Submission
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def submit_form(request):
    if request.method == 'POST':
        submission_form = SubmissionForm(request.POST)

        if submission_form.is_valid():
            submission_form = submission_form.save()
            return redirect('/submissions/success/')
        else:
            print('Form is not valid: ', submission_form.errors)
    else:
        submission_form = SubmissionForm()

    return render(request, 'submissions/submit_form.html', {
        'form': submission_form
    })


def success(request):
    return render(request, 'submissions/success.html')


def case_status(request):
    student_id = request.GET.get('student_id')
    if student_id:
        submissions = Submission.objects.filter(student_id=student_id)
    else:
        submissions = None
    return render(request,
                  'submissions/case_status.html', {'submissions': submissions})
