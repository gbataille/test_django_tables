import django_tables2 as tables

from simple_bug_case.models import TestModels


class DummyTableCallsMethodAsExpected(tables.Table):

    class Meta:
        model = TestModels
        fields = ('dummy_attribute', 'dummy_method')


class DummyTableShouldNotCallMethod(tables.Table):

    dummy_method = tables.TemplateColumn("baz")

    class Meta:
        model = TestModels
        fields = ('dummy_attribute', 'dummy_method')
