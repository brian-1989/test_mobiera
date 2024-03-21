from mobiera_app.domain import ConcatenateWordsDomain
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class ConcatenateWordsUseCases():

    def execute(self, domain: ConcatenateWordsDomain):
        try:
            word = ' '.join(domain.wor_lists)
            return Response(data={"concatenate_word": word})
        except AttributeError as error:
            raise ValidationError(error)
