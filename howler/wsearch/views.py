from django.shortcuts import render
from django.http import HttpResponse
from wally.elastic.search import Search


def index(request):
    res_strings = ["Hello, world. You're at the search index.<br><br>"]

    res_strings.append("Search for Japanese text: 何か調整が必要でしょうか?<br><br>")
    response = Search().search('何か調整が必要でしょうか?')

    for hit in response:
        if hasattr(hit, 'buildNum'):
            continue
        res_strings.append('<br><br><hr>{0}, {1}, {2} <br> {3}<hr>'.format(hit.meta.score, hit.langCode, hit.langPercent, hit.subject))
        if hasattr(hit.meta.highlight, 'body'):
            for fragment in hit.meta.highlight.body:
                res_strings.append('{0}<br>'.format(fragment))
        if hasattr(hit.meta.highlight, 'subject'):
            for fragment in hit.meta.highlight.subject:
                res_strings.append('{0}<br>'.format(fragment))

    return HttpResponse(''.join(res_strings))