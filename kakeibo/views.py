from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from .models import *
from .serializers import *

# Create your views here.


class ICategoryViewSet(viewsets.ModelViewSet):
    queryset = ICategory.objects.all()
    serializer_class = ICategorySerializer


class OCategoryViewSet(viewsets.ModelViewSet):
    queryset = OCategory.objects.all()
    serializer_class = OCategorySerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        cate = self.request.query_params.get('cate')
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        memo = self.request.query_params.get('memo')

        qs = Income.objects.all()

        if cate and cate.isdigit():
            qs = qs.filter(category__exact=cate)

        if year and year.isdigit():
            qs = qs.filter(date__year=year)

        if month and month.isdigit():
            qs = qs.filter(date__month=month)

        if memo:
            qs = qs.filter(memo__icontains=memo)

        return qs


class OutgoViewSet(viewsets.ModelViewSet):
    serializer_class = OutgoSerializer

    def get_queryset(self):
        cate = self.request.query_params.get('cate')
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        store = self.request.query_params.get('store')
        memo = self.request.query_params.get('memo')

        qs = Outgo.objects.all()

        if cate and cate.isdigit():
            qs = qs.filter(category__exact=cate)

        if year and year.isdigit():
            qs = qs.filter(date__year=year)

        if month and month.isdigit():
            qs = qs.filter(date__month=month)

        if store and store.isdigit():
            qs = qs.filter(store__exact=store)

        if memo:
            qs = qs.filter(memo__icontains=memo)

        return qs

    @action(detail=False)
    def sum(self, request):
        sum = self.get_queryset().aggregate(sum=Sum('price'))
        return Response(sum)
