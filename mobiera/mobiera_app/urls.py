from rest_framework.urls import path
from mobiera_app.views import Mobiera, ConcatenateWords

urlpatterns = [

]

urlpatterns += [
    path('mobiera_test', Mobiera.as_view(), name="test_name"),
    path('concatenate_words', ConcatenateWords.as_view(), name="concatenate_words")
]