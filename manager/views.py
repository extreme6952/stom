from django.shortcuts import render,get_object_or_404

from django.views.generic import ListView

from django.views.decorators.http import require_POST

from .models import Content

from .forms import CommentForm,EmailForm

from django.core.mail import send_mail

from django.template.loader import render_to_string







class ListHome(ListView):

    queryset = Content.published.all()

    context_object_name = 'contents'

    template_name = 'content/event/list.html'

    





def detail_services(request,year,month,day,content):

    detail_services = get_object_or_404(Content,
                                        status = Content.Status.PUBLISHED,
                                        publish__year = year,
                                        publish__month = month,
                                        publish__day = day,
                                        slug = content)
    
    return render(request,'content/event/detail.html',{'detail':detail_services})








def send_an_aplication(request,send_aplication_id):

    application = get_object_or_404(Content,id=send_aplication_id,status = Content.Status.PUBLISHED)

    sent = False

    if request.method=='POST':

        form_share = EmailForm(request.POST)

        if form_share.is_valid():

            cd = form_share.cleaned_data

            application_url = request.get_absolute_uri(application.get_absolute_url())

            subject = f"{cd['name']} reccomends you read {application.title}"

            message = f"Read {application.title} at {application_url}"

            send_mail(subject,message,'kaznacheev724@gmail.com',to=['kaznacheev724'])

            sent = True

    else:
        form_share = EmailForm()

    return render(request,'content/event/share.html',{'form_share':form_share,
                                                      'sent':sent,
                                                      'application':application})



def comment_application(request,application_id):

    pass