from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
def show_base(request):
    title = 'Site'
    head_text = 'Hello'

    return render(request, "base.html", locals())


def show_main(request):
    title = 'Site'
    head_text = 'Main'
    main_text = "This is main prog"

    return render(request, "main.html", locals())


def show_info(request):
    title = 'SiteInfo'
    head_text = 'This is information'
    main_text = "Look! This is information"

    return render(request, "info.html", locals())


def goods_view(request):
    good_id = ""
    goods_list = "Goods_list"
    data = {'goodlist': []}
    for i in range(1, 10):
        data['goodlist'].append(
            {
                'id': i,
                'title': '{0}{1}'.format('Good ', i),
                'description': 'Very useful description №{}'.format(i),
                'text': 'Very useful text №{}'.format(i),
                'date': '29.12.2017'
            }
        )
    return render(request, "goods.html", locals())


def good_view(request):
    good_id = "Good site"
    # good_id = good_id1
    return render(request, "goods.html", locals())


def good_view1(request, id):
    good_id = id
    # good_id = good_id1
    return render(request, "goods.html", locals())


def good_char(request, id):
    good_id = id
    # good_id = good_id1
    q = request.GET["id"]
    return render(request, "goods.html", locals())


class OrderView(View):
    def get(self, request):
        q = self.kwargs.get("id")
        # q = request.GET.get("id")
        return render(request, 'order.html', locals())
