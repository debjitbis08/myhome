# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from myhome.blog.models import Entry, CommentSubscriber
from django.http import HttpResponseRedirect
from myhome.blog.forms import CommentSubscriberForm
import re
from django.db.models import Q

def redirect_old_urls(request, object_id):
    entry = Entry.objects.get(pk=object_id)
    url = entry.get_absolute_url()
    return HttpResponseRedirect(url)

def subcribe_by_email(request, entry_id):
    if request.method == "POST":
        form = CommentSubscriberForm(request.POST)
        if form.is_valid():
            entry = Entry.objects.get(pk=entry_id)
            subscriber_email = form.cleaned_data['email'] 
            try:
                subscriber = CommentSubscriber.objects.get(email=subscriber_email)
                subscriber.entries.add(entry)
            except:
                subscriber = CommentSubscriber(
                    email = subscriber_email,
                )
                subscriber.save()
                entry.commentsubscriber_set.add(subscriber)
            return HttpResponseRedirect(entry.get_absolute_url())

    else:
        form = CommentSubscriberForm()

    return render_to_response('blog/subscribe.html', {
            'form': form,
        },
        context_instance=RequestContext(request),
    )

# Stop Words courtesy of http://www.dcs.gla.ac.uk/idom/ir_resources/linguistic_utils/stop_words
STOP_WORDS = r"""\b(a|about|above|across|after|afterwards|again|against|all|almost|alone|along|already|also|
although|always|am|among|amongst|amoungst|amount|an|and|another|any|anyhow|anyone|anything|anyway|anywhere|are|
around|as|at|back|be|became|because|become|becomes|becoming|been|before|beforehand|behind|being|below|beside|
besides|between|beyond|bill|both|bottom|but|by|call|can|cannot|cant|co|computer|con|could|couldnt|cry|de|describe|
detail|do|done|down|due|during|each|eg|eight|either|eleven|else|elsewhere|empty|enough|etc|even|ever|every|everyone|
everything|everywhere|except|few|fifteen|fify|fill|find|fire|first|five|for|former|formerly|forty|found|four|from|
front|full|further|get|give|go|had|has|hasnt|have|he|hence|her|here|hereafter|hereby|herein|hereupon|hers|herself|
him|himself|his|how|however|hundred|i|ie|if|in|inc|indeed|interest|into|is|it|its|itself|keep|last|latter|latterly|
least|less|ltd|made|many|may|me|meanwhile|might|mill|mine|more|moreover|most|mostly|move|much|must|my|myself|name|
namely|neither|never|nevertheless|next|nine|no|nobody|none|noone|nor|not|nothing|now|nowhere|of|off|often|on|once|
one|only|onto|or|other|others|otherwise|our|ours|ourselves|out|over|own|part|per|perhaps|please|put|rather|re|same|
see|seem|seemed|seeming|seems|serious|several|she|should|show|side|since|sincere|six|sixty|so|some|somehow|someone|
something|sometime|sometimes|somewhere|still|such|system|take|ten|than|that|the|their|them|themselves|then|thence|
there|thereafter|thereby|therefore|therein|thereupon|these|they|thick|thin|third|this|those|though|three|through|
throughout|thru|thus|to|together|too|top|toward|towards|twelve|twenty|two|un|under|until|up|upon|us|very|via|was|
we|well|were|what|whatever|when|whence|whenever|where|whereafter|whereas|whereby|wherein|whereupon|wherever|whether|
which|while|whither|who|whoever|whole|whom|whose|why|will|with|within|without|would|yet|you|your|yours|yourself|
yourselves)\b"""

def search(request, template_name='blog/search.html'):
    """
    Search for proxy objects. 99.99 percent borrowed from basic-blog's search.

    This template will allow you to setup a simple search form that will try to return results based on
    given search strings. The queries will be put through a stop words filter to remove words like
    'the', 'a', or 'have' to help imporve the result set.

    Template: ``blog/search.html``
    Context:
        object_list
        List of blog posts that match given search term(s).
    search_term
        Given search term.
    """
    context = {}
    if request.GET:
        stop_word_list = re.compile(STOP_WORDS, re.IGNORECASE)
        search_term = '%s' % request.GET['q']
        cleaned_search_term = stop_word_list.sub('', search_term)
        cleaned_search_term = cleaned_search_term.strip()
        if len(cleaned_search_term) != 0:
            """
            entry_list = Entry.objects.filter(Q(title__icontains=cleaned_search_term) | Q(tags__icontains=cleaned_search_term) | Q(body_text__icontains=cleaned_search_term)).order_by('-pub_date')
            """
            entry_list = Entry.objects.filter(Q(title__icontains=cleaned_search_term) | Q(body_text__icontains=cleaned_search_term)).order_by('-pub_date')
            context = {'object_list': entry_list, 'search_term':search_term}
        else:
            message = 'Search term was too vague. Please try again.'
            context = {'message':message}
    return render_to_response(template_name, context, context_instance=RequestContext(request))
