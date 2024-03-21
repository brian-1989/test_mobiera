from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from mobiera_app.serializer import ConcatenateWordsSerializer
from mobiera_app.domain import ConcatenateWordsDomain
from mobiera_app.use_cases import ConcatenateWordsUseCases

class Mobiera(APIView):
    def get(self, request):
        test_name = {"mobiera_test": "Brian Zapata"}
        return Response(data=test_name)

class ConcatenateWords(APIView):
    def post(self, request: Request):
        serializer = ConcatenateWordsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = ConcatenateWordsDomain(**serializer.data)
        uc = ConcatenateWordsUseCases()
        return uc.execute(domain)   


