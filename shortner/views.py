from django.shortcuts import render,get_object_or_404,redirect#render_to_response,
from django.template import RequestContext
from .models import Link
from django.core.exceptions import ObjectDoesNotExist


import hashlib
from shortner.forms import LinkForm
from django.db.transaction import commit


def base62_encode(num):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    back_up = num
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    #return str(back_up)+"abcdef"
    return ''.join(arr)

def home(request):
    form = LinkForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            link = form.save(commit=False)
            #link.save()
            url_temp = form.data['url']
            try:
                check = Link.objects.get(url=url_temp)
                return redirect('shortner.views.display',pk=check.pk)
            except ObjectDoesNotExist:
                raw = url_temp.encode('utf-8')
                #hashed = hashlib.md5(raw).hexdigest() 
                last = Link.objects.last()
                try:
                    last_id = last.pk+1
                except AttributeError:
                    last_id = 0
                #link.save()
                link.hash = base62_encode(last_id)
                #link.hash = hashed[0:8]
                link.save()
                return redirect('shortner.views.display',pk=link.pk)
        #return render(request,'shortner/404.html')
    return render(request,'shortner/home.html',{'form':form})
def extract(request,hash):
    link = get_object_or_404(Link,hash=hash)
    url = link.url
    if not url.startswith('http'):
        url = 'http://'+url
    return redirect(url)
def display(request,pk):
    link = get_object_or_404(Link,pk=pk)
    return render(request,'shortner/display.html',{'link':link})
    #return render(request,'shortner/hash.html',{'link',link})
# def handler404(request):
#     response = render_to_response('shortner/404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response