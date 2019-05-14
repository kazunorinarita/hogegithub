from django.urls import path

from .models import Item
from .models import Item2
from .views import ItemFilterView, ItemUpdateView_1, ItemUpdateView_2, ItemUpdateView_3, ItemUpdateView_4, ItemUpdateView_5, ItemUpdateView_6, ItemCreateView, Item2UpdateView_1, Item2UpdateView_2, Item2UpdateView_3, Item2UpdateView_4, Item2UpdateView_5, Item2UpdateView_6, Item1UpdateView_1, Item1UpdateView_2, Item1UpdateView_3, Item1UpdateView_4, Item1UpdateView_5, Item1UpdateView_6, ItemDeleteView

# アプリケーションのルーティング設定

urlpatterns = [
    path('update1/<int:pk>/', ItemUpdateView_1.as_view(), name='update1'),
    path('update2/<int:pk>/', ItemUpdateView_2.as_view(), name='update2'),
    path('update3/<int:pk>/', ItemUpdateView_3.as_view(), name='update3'),
    path('update4/<int:pk>/', ItemUpdateView_4.as_view(), name='update4'),
    path('update5/<int:pk>/', ItemUpdateView_5.as_view(), name='update5'),
    path('update6/<int:pk>/', ItemUpdateView_6.as_view(), name='update6'),
    path('update11/<int:pk>/', Item1UpdateView_1.as_view(), name='update11'),
    path('update12/<int:pk>/', Item1UpdateView_2.as_view(), name='update12'),
    path('update13/<int:pk>/', Item1UpdateView_3.as_view(), name='update13'),
    path('update14/<int:pk>/', Item1UpdateView_4.as_view(), name='update14'),
    path('update15/<int:pk>/', Item1UpdateView_5.as_view(), name='update15'),
    path('update16/<int:pk>/', Item1UpdateView_6.as_view(), name='update16'),
    path('update21/<int:pk>/', Item2UpdateView_1.as_view(), name='update21'),
    path('update22/<int:pk>/', Item2UpdateView_2.as_view(), name='update22'),
    path('update23/<int:pk>/', Item2UpdateView_3.as_view(), name='update23'),
    path('update24/<int:pk>/', Item2UpdateView_4.as_view(), name='update24'),
    path('update25/<int:pk>/', Item2UpdateView_5.as_view(), name='update25'),
    path('update26/<int:pk>/', Item2UpdateView_6.as_view(), name='update26'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('', ItemFilterView.as_view(), name='index'),
]