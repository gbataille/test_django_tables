from django.shortcuts import render

from simple_bug_case.tables import DummyTableCallsMethodAsExpected, DummyTableShouldNotCallMethod
from simple_bug_case.models import TestModels

# Create your views here.


def home(request):
  model = TestModels()
  table = DummyTableCallsMethodAsExpected([model])
  table2 = DummyTableShouldNotCallMethod([model])
  return render(request, 'home.html', {'table': table, 'table2': table2})
