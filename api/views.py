from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Test, IQ, EQ
from .serializers import TestSerializer, IQSerializer, EQSerializer


class TestCreateView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class SaveIQResultView(CreateAPIView):
    queryset = IQ.objects.all()
    serializer_class = IQSerializer


class SaveEQResultView(CreateAPIView):
    queryset = EQ.objects.all()
    serializer_class = EQSerializer


class ShowResultsView(APIView):

    def get(self, request, *args, **kwargs):
        login = self.kwargs['pk']
        test = Test.objects.filter(login=login).first()
        iq = IQ.objects.filter(test=test).values("score", "time")
        eq = EQ.objects.filter(test=test).values("letters", "time")
        data = {
            'login': login,
            'iq_results': list(iq),
            'eq_results': list(eq)
        }
        return Response(data)