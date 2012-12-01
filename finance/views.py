from finance.models import FinanceItem
# from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    latest_finance_list = FinanceItem.objects.all()
    return render_to_response('finance/index.html', {'latest_finance_list': latest_finance_list})