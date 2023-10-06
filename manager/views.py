from email.mime.multipart import MIMEMultipart
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

    





def detail_services(request,content,year,month,day):

    detail = get_object_or_404(Content,
                               status = Content.Status.PUBLISHED,
                               publish__year= year,
                               publish__month=month,
                               publish__day = day,
                               slug = content)
    
    return render(request,'content/event/detail.html',{'detail':detail})



def service_request(request,service_id):

    service_application = get_object_or_404(Content,id=service_id,status = Content.Status.PUBLISHED)

    sent = False

    if request.method=='POST':

        form_share = EmailForm(request.POST)

        if form_share.is_valid():
            
            cd = form_share.cleaned_data

            post_url = request.build_absolute_uri(service_application.get_absolute_url())

            subject = f"{cd['name']} recommends you read {service_application.title}"

            message = f"Read {service_application.title} at {post_url}\n\n"
            f" {cd['name']} comments: {cd['comments']}"
        
            send_mail(subject,message,'',
                      [cd['to']])

            sent = True





    else:
        form_share = EmailForm()

    return render(request,'content/event/share.html',{'service_application':service_application,
                                                      'sent':sent,
                                                      'form_share':form_share})




def comment_service(request,service_id):
    pass

