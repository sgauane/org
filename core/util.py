from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect


def send_email(request):
    subject = request.POST.get('subject', 'teste')
    message = request.POST.get('message', 'hello')
    from_email = request.POST.get('from_email', 'sgauane@gmail.com')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['samgaus87@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')