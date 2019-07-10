from django.db import models
from django.contrib import messages
from django.db.models import F
from django.db.models import Q

import django_filters
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django_filters.views import FilterView

from .filters import ItemFilterSet

from .forms import Item0Form

from .forms import Item1Form
from .forms import Item2Form
from .forms import Item3Form
from .forms import Item4Form
from .forms import Item5Form
from .forms import Item6Form
from .models import Item

from .forms import Item1Form_1
from .forms import Item2Form_1
from .forms import Item3Form_1
from .forms import Item4Form_1
from .forms import Item5Form_1
from .forms import Item6Form_1
from .forms import Item7Form_1
from .models import Item3

from .forms import Item1Form_2
from .forms import Item2Form_2
from .forms import Item3Form_2
from .forms import Item4Form_2
from .forms import Item5Form_2
from .forms import Item6Form_2
from .models import Item6

from .forms import Item11Form
from .forms import Item12Form
from .forms import Item13Form
from .forms import Item14Form
from .forms import Item15Form
from .forms import Item16Form
from .models import Item1

from .forms import Item11Form_1
from .forms import Item12Form_1
from .forms import Item13Form_1
from .forms import Item14Form_1
from .forms import Item15Form_1
from .forms import Item16Form_1
from .forms import Item17Form_1
from .models import Item4

from .forms import Item11Form_2
from .forms import Item12Form_2
from .forms import Item13Form_2
from .forms import Item14Form_2
from .forms import Item15Form_2
from .forms import Item16Form_2
from .models import Item7

from .forms import Item21Form
from .forms import Item22Form
from .forms import Item23Form
from .forms import Item24Form
from .forms import Item25Form
from .forms import Item26Form
from .models import Item2

from .forms import Item21Form_1
from .forms import Item22Form_1
from .forms import Item23Form_1
from .forms import Item24Form_1
from .forms import Item25Form_1
from .forms import Item26Form_1
from .forms import Item27Form_1
from .models import Item5

from .forms import Item21Form_2
from .forms import Item22Form_2
from .forms import Item23Form_2
from .forms import Item24Form_2
from .forms import Item25Form_2
from .forms import Item26Form_2
from .models import Item8

from users.models import User

#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.staticfiles.templatetags.staticfiles import static
from . import forms
from django.template.context_processors import csrf

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, InvalidPage
from django.core.paginator import PageNotAnInteger
from pure_pagination.mixins import PaginationMixin

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from django.template import Library

from django.http import HttpResponse

from rules.contrib.views import PermissionRequiredMixin

from guardian.shortcuts import get_objects_for_user
from guardian.shortcuts import assign_perm

from django.core.validators import MaxValueValidator, MinValueValidator

from operator import itemgetter
import itertools
import operator

# 未ログインのユーザーにアクセスを許可する場合は、LoginRequiredMixinを継承から外してください。
#
# LoginRequiredMixin：未ログインのユーザーをログイン画面に誘導するMixin
# 参考：https://docs.djangoproject.com/ja/2.1/topics/auth/default/#the-loginrequired-mixin

def index(self, request, **kwargs):

    return HttpResponseRedirect(reverse('password_change',args=request))

class ItemFilterView(LoginRequiredMixin, FilterView):
    """
    ビュー：一覧表示画面

    以下のパッケージを使用
    ・django-filter 一覧画面(ListView)に検索機能を追加
    https://django-filter.readthedocs.io/en/master/
    """

    #model = Item
    model = Item
    # django-filter 設定
    filterset_class = ItemFilterSet
    # django-filter ver2.0対応 クエリ未設定時に全件表示する設定
    strict = False

    num_chairs = 0

    # 1ページの表示
    paginate_by = 10

    def get(self, request, **kwargs):
        """
        リクエスト受付
        セッション変数の管理:一覧画面と詳細画面間の移動時に検索条件が維持されるようにする。
        """

        if self.request.user.updated_at == None: 
           return HttpResponseRedirect(reverse('password_change',args=request))

        # 一覧画面内の遷移(GETクエリがある)ならクエリを保存する
        if request.GET:
            request.session['query'] = request.GET
        # 詳細画面・登録画面からの遷移(GETクエリはない)ならクエリを復元する
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_queryset(self):
        """
        ソート順・デフォルトの絞り込みを指定
        """
        key_list =[]
        key_list1 =[]
        key_list2 =[]
        key_list3 =[]

        current_user = self.request.user

        key1 =  User.objects.values_list('id',flat=False).get(pk=current_user.id)

        key_list = list(key1)
        key_list1 = list(key1)

        #item_out1 = Item.objects.get(created_by_id=key1)
        #item_out1.itemsort="1"
        #item_out1.save()

        #item_out1 = Item.objects.filter(created_by_id__in=key_list1).order_by('keyname').annotate(order_KEY=F('order') * 1)
        item_out1 = Item.objects.filter(created_by_id__in=key_list1).order_by('keyname')

        #item_out1.order = F('order') + 1
        #item_out1.order_KEY = F('order') + 1

        #Item = Item.objects.filter(created_by_id__in=key_list1).order_by('keyname')
        #Item.sortkey = "1"
        #Item.save()

        #item_out1 = Item.objects.filter(created_by_id__in=key1).order_by('keyname')
        #item_out1 = Item.objects.filter(created_by_id__in=key1,name='1').order_by('keyname')
                        
        #for obj1 in Key.objects.filter(Key_2__in=key1):
        #    key_list.append(obj1.Key_1)
        for obj1 in get_objects_for_user(self.request.user, 'app.view_item'):
            result = self.request.user.has_perm('app.view_item', obj1)
        
            if result:   
               key_list.append(obj1.created_by_id)
               key_list2.append(obj1.created_by_id)

        #       item_out2 = Item.objects.get(created_by_id=obj1.created_by_id)
        #       item_out2.itemsort="2"
        #       item_out2.save()
        #       item_out2 = Item.objects.filter(created_by_id__in=key_list2).order_by('keyname')

        #       Item.sortkey = "2"
        #       Item.save()
        
        for obj2 in get_objects_for_user(self.request.user, 'app.add_item'):
            result = self.request.user.has_perm('app.add_item', obj2)
            if result:   
               key_list.append(obj2.created_by_id)
               key_list3.append(obj2.created_by_id)

        #       item_out3 = Item.objects.filter(created_by_id__in=key_list3).order_by('keyname')
        #       Item.sortkey = "3"
        #       Item.save()

        #    user = User.objects.filter(full_name=self.request.user)
        #    item1 = Item1.objects.filter(created_by1_id=self.request.user.id)
        #    if key1.has_perm('app.view_item', obj1):
        #print(projects)
        #for obj1 in get_objects_for_user(key1, 'app.view_item'):
        #    print(obj1)
        #    key_list.append(obj1.user_id)

        #for obj2 in Key.objects.filter(Key_3__in=key1):
        #    key_list.append(obj2.Key_1)

        #item_out = item_out1
        #print("11")
        #print(key_list1)
        #print(item_out1)
        #if item_out1:
        #    item_out = item_out1

        #print("12")
        #print(key_list2)
        #print(item_out2)
        #item_out2 = Item.objects.filter(created_by_id__in=key_list2).order_by('keyname').annotate(order_KEY=F('order')*2)
        item_out2 = Item.objects.filter(created_by_id__in=key_list2).order_by('keyname')
        #item_out2.order = F('order') + 2
        #item_out2.order_KEY = F('order') + 2
        #if item_out2:
        #    item_out = item_out2.union(item_out1)
        #    print("5")
        #    print(item_out)

        #print("13")
        #print(key_list3)
        #print(item_out3)
        #item_out3 = Item.objects.filter(created_by_id__in=key_list3).order_by('keyname').annotate(order_KEY=F('order')*3)
        item_out3 = Item.objects.filter(created_by_id__in=key_list3).order_by('keyname')
        #item_out3.order = F('order') + 3
        #item_out3.order_KEY = F('order') + 3

        #if item_out3:
        #    item_out = item_out1.union(item_out2.union(item_out3))
        #    sorted(item_out, key=lambda x: x[1])
        #    print("6")
        #    print(item_out)

        if self.request.user.is_superuser: # スーパーユーザの場合、リストにすべてを表示する。
        #    return Item.objects.select_related('Itemkey').all().order_by('keyname')
            return Item.objects.all().order_by('keyname')
        else:# 一般ユーザは自分のレコードのみ表示する。
        #    return Item.objects.filter(created_by_id__in=key_list3).order_by('updated_by_id','keyname') | Item.objects.filter(created_by_id__in=key_list2).order_by('updated_by_id','keyname')
        #    print(item_out1.updated_by_id)
        #    print(item_out2.updated_by_id)
        #    print(item_out3.updated_by_id)
        #    return(Item.objects.filter(created_by_id__in=key_list1).order_by('keyname')
        #    return(Item.objects.filter(created_by_id__in=key_list1).order_by(F('num_chairs')) | Item.objects.filter(created_by_id__in=key_list2).order_by(F('num_chairs')) | Item.objects.filter(created_by_id__in=key_list3).order_by(F('num_chairs'))
        #    return(Item.objects.filter(created_by_id__in=key_list1).order_by(F('order')+1.asc(nulls_last=True)) | Item.objects.filter(created_by_id__in=key_list2).order_by(F('order')+2.asc(nulls_last=True)) | Item.objects.filter(created_by_id__in=key_list3).order_by(F('order')+3.asc(nulls_last=True)))
        #    return(item_out1.filter(created_by_id__in=key_list1).order_by('updated_by_id') | item_out2.filter(created_by_id__in=key_list2).order_by('updated_by_id') | item_out3.filter(created_by_id__in=key_list3).order_by('updated_by_id'))
            item_out = item_out1 | item_out2 | item_out3
        #    result = item_out.objects.values('order',flat=False).get(pk=current_user.id)
        #    result1 = item_out.values('name')
        #    result2 = item_out.values(F'order_KEY')
        #    for data in result:
        #        print('order = ' + data.order)
        #    return item_out.all().order_by(F('order_KEY').desc(nulls_last=True))
        #    return item_out.all().order_by(F('order_KEY').asc(nulls_last=True))
            return item_out.all().order_by('keyname')
        #    auths = item_out1.union(item_out2.union(item_out3))
        #    item_outa = sorted(auths, key=itemgetter('updated_by_id'), reverse=True)
        #    print(item_out.values('updated_by_id'))
        #    return item_out.objects.filter(created_by_id__in=key_list).order_by('-updated_by_id','-created_by_id')
        #    return item_outa



        #    return item_out1.filter(created_by_id__in=key_list1).order_by('updated_by_id') | item_out2.filter(created_by_id__in=key_list2).order_by('updated_by_id') | item_out3.filter(created_by_id__in=key_list3).order_by('updated_by_id')
        #    return item_out
        #    return Item.objects.filter(id=current_user.id)
        #    return Item.objects.filter(id__in=key1)

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        表示データの設定
        """
        # 表示データを追加したい場合は、ここでキーを追加しテンプレート上で表示する
        # 例：kwargs['sample'] = 'sample'
        return super().get_context_data(object_list=object_list, **kwargs)

class ItemCreateView(LoginRequiredMixin, CreateView):
    """
    ビュー：登録画面
    """
    model = Item
    form_class = Item0Form
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.name = self.request.user
        item.created_by = self.request.user
        item.created_at = timezone.now()
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        item1 = Item1(keyname=Item,name=item.name,created_by1=item.created_by)
        item1.save()

        item2 = Item2(keyname=Item,name=item.name,created_by2=item.created_by)
        item2.save()

        return HttpResponseRedirect(self.success_url)

class ItemUpdateView_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item1Form
    success_url = reverse_lazy('update2')
    permission_required = 'app.rules_change_item'

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        return redirect('update2', pk=item.pk)
 
    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_1_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item1Form_1
    success_url = reverse_lazy('update2_1')
    permission_required = 'app.rules_change_item_1'

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update2_1', pk=item.pk)
 
    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_1_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item1Form_2
    success_url = reverse_lazy('update2_2')
    permission_required = 'app.rules_change_item_2'

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update2_2', pk=item.pk)
 
    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item2Form
    success_url = reverse_lazy('update3')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        return redirect('update3', pk=item.pk)
        
    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_2_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item2Form_1
    success_url = reverse_lazy('update3_1')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update3_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チームワーク】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_2_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item2Form_2
    success_url = reverse_lazy('update3_2')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update3_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_3(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item3Form
    success_url = reverse_lazy('update4')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        return redirect('update4', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【人材育成】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_3_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item3Form_1
    success_url = reverse_lazy('update4_1')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update4_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【向上心】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_3_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item3Form_2
    success_url = reverse_lazy('update4_2')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update4_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【診療に対する熱意】（自己研鑽・倫理観・顧客思考）に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_4(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item4Form
    success_url = reverse_lazy('update5')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        return redirect('update5', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【企画推進力】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_4_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item4Form_1
    success_url = reverse_lazy('update5_1')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update5_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【行動力】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_4_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item4Form_2
    success_url = reverse_lazy('update5_2')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update5_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チャレンジ精神】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_5(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item5Form
    success_url = reverse_lazy('update6')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        return redirect('update6', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_5_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item5Form_1
    success_url = reverse_lazy('update6_1')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update6_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【柔軟性】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_5_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item5Form_2
    success_url = reverse_lazy('update6_2')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update6_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_6(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item6Form
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item.objects.filter(updated_by = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item.flag = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【マネジメント力・組織管理能力】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_6_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item6Form_1
    success_url = reverse_lazy('update7_1')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by3_id
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        return redirect('update7_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_6_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item6
    form_class = Item6Form_2
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by6 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by6_id
        item.save()

        entries = Item6.objects.filter(updated_by6 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【チーム医療】（柔軟性・協調性）に対する未入力があります。')
        return super().form_invalid(form)


class Item1UpdateView_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item11Form
    success_url = reverse_lazy('update12')
    permission_required = 'app.rules_change_item1'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update12', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_1_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item11Form_1
    success_url = reverse_lazy('update12_1')
    permission_required = 'app.rules_change_item1_1'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update12_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_1_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item11Form_1
    success_url = reverse_lazy('update12_2')
    permission_required = 'app.rules_change_item1_2'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update12_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item12Form
    success_url = reverse_lazy('update13')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update13', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_2_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item12Form_1
    success_url = reverse_lazy('update13_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update13_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チームワーク】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_2_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item12Form_2
    success_url = reverse_lazy('update13_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update13_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_3(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item13Form
    success_url = reverse_lazy('update14')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update14', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【人材育成】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_3_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item13Form_1
    success_url = reverse_lazy('update14_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update14_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【向上心】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_3_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item13Form_2
    success_url = reverse_lazy('update14_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update14_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【診療に対する熱意】（自己研鑽・倫理観・顧客思考）に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_4(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item14Form
    success_url = reverse_lazy('update15')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update15', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【企画推進力】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_4_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item14Form_1
    success_url = reverse_lazy('update15_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update15_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【行動力】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_4_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item14Form_2
    success_url = reverse_lazy('update15_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update15_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チャレンジ精神】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_5(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item15Form
    success_url = reverse_lazy('update16')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update16', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_5_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item15Form_1
    success_url = reverse_lazy('update16_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update16_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【柔軟性】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_5_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item15Form_2
    success_url = reverse_lazy('update16_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update16_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_6(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item1
    form_class = Item16Form
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by1 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by1_id
        item.save()

        entries = Item1.objects.filter(created_by1 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【マネジメント力・組織管理能力】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_6_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item16Form_1
    success_url = reverse_lazy('update17_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        return redirect('update17_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_6_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item7
    form_class = Item16Form_2
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by7 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by7_id
        item.save()

        entries = Item7.objects.filter(created_by7 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【チーム医療】（柔軟性・協調性）に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item21Form
    success_url = reverse_lazy('update22')
    permission_required = 'app.rules_change_item2'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update22', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_1_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """    
    model = Item5
    form_class = Item21Form_1
    success_url = reverse_lazy('update22_1')
    permission_required = 'app.rules_change_item2_1'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update22_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_1_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """    
    model = Item8
    form_class = Item21Form_2
    success_url = reverse_lazy('update22_2')
    permission_required = 'app.rules_change_item2_2'

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update22_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【コミュニケーション力】（情報伝達・発信力）に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item22Form
    success_url = reverse_lazy('update23')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update23', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_2_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item22Form_1
    success_url = reverse_lazy('update23_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update23_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チームワーク】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_2_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item8
    form_class = Item22Form_2
    success_url = reverse_lazy('update23_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update23_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_3(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item23Form
    success_url = reverse_lazy('update24')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update24', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【人材育成】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_3_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item23Form_1
    success_url = reverse_lazy('update24_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update24_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【向上心】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_3_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item8
    form_class = Item23Form_2
    success_url = reverse_lazy('update24_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update24_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【診療に対する熱意】（自己研鑽・倫理観・顧客思考）に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_4(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item24Form
    success_url = reverse_lazy('update25')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update25', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【企画推進力】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_4_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item24Form_1
    success_url = reverse_lazy('update25_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update25_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【行動力】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_4_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item8
    form_class = Item24Form_2
    success_url = reverse_lazy('update25_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update25_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【チャレンジ精神】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_5(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item25Form
    success_url = reverse_lazy('update26')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update26', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_5_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item25Form_1
    success_url = reverse_lazy('update26_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update26_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【柔軟性】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_5_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item8
    form_class = Item25Form_2
    success_url = reverse_lazy('update26_2')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update26_2', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【経営感覚・経営貢献】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_6(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item2
    form_class = Item26Form
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by2 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by2_id
        item.save()

        entries = Item2.objects.filter(created_by2 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【マネジメント力・組織管理能力】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_6_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item26Form_1
    success_url = reverse_lazy('update27_1')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        return redirect('update27_1', pk=item.pk)

    def form_invalid(self, form):
        messages.error(self.request, '【責任感】に対する未入力があります。')
        return super().form_invalid(form)

class Item2UpdateView_6_2(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item8
    form_class = Item26Form_2
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by8 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by8_id
        item.save()

        entries = Item8.objects.filter(created_by8 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1')
        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【チーム医療】（柔軟性・協調性）に対する未入力があります。')
        return super().form_invalid(form)

class ItemUpdateView_7_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item3
    form_class = Item7Form_1
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by3 = self.request.user
        item.updated_at = timezone.now()
        item.save()

        entries = Item3.objects.filter(updated_by3 = self.request.user ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【社会人基礎力チェック】に対する未入力があります。')
        return super().form_invalid(form)

class Item1UpdateView_7_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item4
    form_class = Item17Form_1
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by4 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by4_id
        item.save()

        entries = Item4.objects.filter(created_by4 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag1 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【社会人基礎力チェック】に対する未入力があります。')
        return self.request
    #    return super().form_invalid(form)

class Item2UpdateView_7_1(LoginRequiredMixin, UpdateView):
    """
    ビュー：自己評価画面
    """
    model = Item5
    form_class = Item27Form_1
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        自己評価処理
        """
        item = form.save(commit=False)
        item.updated_by5 = self.request.user
        item.updated_at = timezone.now()
        key = item.created_by5_id
        item.save()

        entries = Item5.objects.filter(created_by5 = key ,
                    Q1_1__gte='1', Q1_2__gte='1', Q1_3__gte='1', Q1_4__gte='1', Q1_5__gte='1',
                    Q2_1__gte='1', Q2_2__gte='1', Q2_3__gte='1', Q2_4__gte='1', Q2_5__gte='1',
                    Q3_1__gte='1', Q3_2__gte='1', Q3_3__gte='1', Q3_4__gte='1', Q3_5__gte='1',
                    Q4_1__gte='1', Q4_2__gte='1', Q4_3__gte='1', Q4_4__gte='1', Q4_5__gte='1',
                    Q5_1__gte='1', Q5_2__gte='1', Q5_3__gte='1', Q5_4__gte='1', Q5_5__gte='1',
                    Q6_1__gte='1', Q6_2__gte='1', Q6_3__gte='1', Q6_4__gte='1', Q6_5__gte='1',
                    Q7_1__gte='1', Q7_2__gte='1', Q7_3__gte='1', Q7_4__gte='1', Q7_5__gte='1',
                    Q7_6__gte='1', Q7_7__gte='1', Q7_8__gte='1', Q7_9__gte='1', Q7_10__gte='1')

        if entries:   
            item = Item.objects.get(created_by = key)
            item.flag2 = 1
            item.save()

        messages.success(self.request, '更新内容を保存しました')
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, '【社会人基礎力チェック】に対する未入力があります。')
        return super().form_invalid(form)

class ItemDeleteView(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = Item1Form
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)



class ItemUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Item
    form_class = Item1Form
    success_url = reverse_lazy('index')
    permission_required = 'app.rules_change_item'

class Item1UpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Item1
    form_class = Item1Form
    success_url = reverse_lazy('index')
    permission_required = 'app.rules_change_item1'

class Item2UpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Item2
    form_class = Item1Form
    success_url = reverse_lazy('index')
    permission_required = 'app.rules_change_item2'
