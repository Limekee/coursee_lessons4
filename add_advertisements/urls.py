
from django.urls import path
from .views import index
#переменная которая хранит ссылки
#функция path создает ссылку и говорит какой оброботчик будет давать на нее ответ
urlpatterns = [
    path('home/', index)
]
