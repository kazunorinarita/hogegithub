from django.urls import path

from .models import Item
from .models import Item1
from .models import Item2
from .models import Item3
from .models import Item4
from .models import Item5
from .models import Item6
from .models import Item7
from .models import Item8

from .views import ItemFilterView,ItemlistView,PostExport,PasswordChange,PasswordChangeDone,ItemCreateView,ItemDeleteView, \
                   ItemUpdateView_1, ItemUpdateView_2, ItemUpdateView_3, ItemUpdateView_4, ItemUpdateView_5, ItemUpdateView_6, \
                   Item1UpdateView_1, Item1UpdateView_2, Item1UpdateView_3, Item1UpdateView_4, Item1UpdateView_5, Item1UpdateView_6, \
                   Item2UpdateView_1, Item2UpdateView_2, Item2UpdateView_3, Item2UpdateView_4, Item2UpdateView_5, Item2UpdateView_6, \
                   ItemUpdateView_1_1, ItemUpdateView_2_1, ItemUpdateView_3_1, ItemUpdateView_4_1, ItemUpdateView_5_1, ItemUpdateView_6_1,ItemUpdateView_7_1, \
                   Item1UpdateView_1_1,Item1UpdateView_2_1,Item1UpdateView_3_1,Item1UpdateView_4_1,Item1UpdateView_5_1, Item1UpdateView_6_1,Item1UpdateView_7_1,\
                   Item2UpdateView_1_1,Item2UpdateView_2_1,Item2UpdateView_3_1,Item2UpdateView_4_1,Item2UpdateView_5_1, Item2UpdateView_6_1,Item2UpdateView_7_1, \
                   ItemUpdateView_1_2, ItemUpdateView_2_2, ItemUpdateView_3_2, ItemUpdateView_4_2, ItemUpdateView_5_2, ItemUpdateView_6_2, \
                   Item1UpdateView_1_2,Item1UpdateView_2_2,Item1UpdateView_3_2,Item1UpdateView_4_2,Item1UpdateView_5_2, Item1UpdateView_6_2,\
                   Item2UpdateView_1_2,Item2UpdateView_2_2,Item2UpdateView_3_2,Item2UpdateView_4_2,Item2UpdateView_5_2, Item2UpdateView_6_2
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from app import views
#from django.contrib.auth import views as auth_views
#from accounts import views as accounts_views
#from boards import views

#from django.contrib.auth import views as auth_views

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

    path('update1_1/<int:pk>/', ItemUpdateView_1_1.as_view(), name='update1_1'),
    path('update2_1/<int:pk>/', ItemUpdateView_2_1.as_view(), name='update2_1'),
    path('update3_1/<int:pk>/', ItemUpdateView_3_1.as_view(), name='update3_1'),
    path('update4_1/<int:pk>/', ItemUpdateView_4_1.as_view(), name='update4_1'),
    path('update5_1/<int:pk>/', ItemUpdateView_5_1.as_view(), name='update5_1'),
    path('update6_1/<int:pk>/', ItemUpdateView_6_1.as_view(), name='update6_1'),
    path('update7_1/<int:pk>/', ItemUpdateView_7_1.as_view(), name='update7_1'),
    path('update11_1/<int:pk>/', Item1UpdateView_1_1.as_view(), name='update11_1'),
    path('update12_1/<int:pk>/', Item1UpdateView_2_1.as_view(), name='update12_1'),
    path('update13_1/<int:pk>/', Item1UpdateView_3_1.as_view(), name='update13_1'),
    path('update14_1/<int:pk>/', Item1UpdateView_4_1.as_view(), name='update14_1'),
    path('update15_1/<int:pk>/', Item1UpdateView_5_1.as_view(), name='update15_1'),
    path('update16_1/<int:pk>/', Item1UpdateView_6_1.as_view(), name='update16_1'),
    path('update17_1/<int:pk>/', Item1UpdateView_7_1.as_view(), name='update17_1'),
    path('update21_1/<int:pk>/', Item2UpdateView_1_1.as_view(), name='update21_1'),
    path('update22_1/<int:pk>/', Item2UpdateView_2_1.as_view(), name='update22_1'),
    path('update23_1/<int:pk>/', Item2UpdateView_3_1.as_view(), name='update23_1'),
    path('update24_1/<int:pk>/', Item2UpdateView_4_1.as_view(), name='update24_1'),
    path('update25_1/<int:pk>/', Item2UpdateView_5_1.as_view(), name='update25_1'),
    path('update26_1/<int:pk>/', Item2UpdateView_6_1.as_view(), name='update26_1'),
    path('update27_1/<int:pk>/', Item2UpdateView_7_1.as_view(), name='update27_1'),

    path('update1_2/<int:pk>/', ItemUpdateView_1_2.as_view(), name='update1_2'),
    path('update2_2/<int:pk>/', ItemUpdateView_2_2.as_view(), name='update2_2'),
    path('update3_2/<int:pk>/', ItemUpdateView_3_2.as_view(), name='update3_2'),
    path('update4_2/<int:pk>/', ItemUpdateView_4_2.as_view(), name='update4_2'),
    path('update5_2/<int:pk>/', ItemUpdateView_5_2.as_view(), name='update5_2'),
    path('update6_2/<int:pk>/', ItemUpdateView_6_2.as_view(), name='update6_2'),
    path('update11_2/<int:pk>/', Item1UpdateView_1_2.as_view(), name='update11_2'),
    path('update12_2/<int:pk>/', Item1UpdateView_2_2.as_view(), name='update12_2'),
    path('update13_2/<int:pk>/', Item1UpdateView_3_2.as_view(), name='update13_2'),
    path('update14_2/<int:pk>/', Item1UpdateView_4_2.as_view(), name='update14_2'),
    path('update15_2/<int:pk>/', Item1UpdateView_5_2.as_view(), name='update15_2'),
    path('update16_2/<int:pk>/', Item1UpdateView_6_2.as_view(), name='update16_2'),
    path('update21_2/<int:pk>/', Item2UpdateView_1_2.as_view(), name='update21_2'),
    path('update22_2/<int:pk>/', Item2UpdateView_2_2.as_view(), name='update22_2'),
    path('update23_2/<int:pk>/', Item2UpdateView_3_2.as_view(), name='update23_2'),
    path('update24_2/<int:pk>/', Item2UpdateView_4_2.as_view(), name='update24_2'),
    path('update25_2/<int:pk>/', Item2UpdateView_5_2.as_view(), name='update25_2'),
    path('update26_2/<int:pk>/', Item2UpdateView_6_2.as_view(), name='update26_2'),

    path('create/', ItemCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('list/',ItemlistView.as_view(), name='list'),
    path('export/',PostExport, name='output_csv'),
    path('', ItemFilterView.as_view(), name='index'),
    path('', views.index),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    #path('admin/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),

    #path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]