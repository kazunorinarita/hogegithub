from django.db import models

import django_filters
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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

from .forms import Item11Form
from .forms import Item12Form
from .forms import Item13Form
from .forms import Item14Form
from .forms import Item15Form
from .forms import Item16Form
from .models import Item1

from .forms import Item21Form
from .forms import Item22Form
from .forms import Item23Form
from .forms import Item24Form
from .forms import Item25Form
from .forms import Item26Form
from .models import Item2

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

# 未ログインのユーザーにアクセスを許可する場合は、LoginRequiredMixinを継承から外してください。
#
# LoginRequiredMixin：未ログインのユーザーをログイン画面に誘導するMixin
# 参考：https://docs.djangoproject.com/ja/2.1/topics/auth/default/#the-loginrequired-mixin

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

    # 1ページの表示
    paginate_by = 10

    def get(self, request, **kwargs):
        """
        リクエスト受付
        セッション変数の管理:一覧画面と詳細画面間の移動時に検索条件が維持されるようにする。
        """

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
        current_user = self.request.user

        key1 =  User.objects.values_list('id',flat=False).get(pk=current_user.id)
        key_list =[]
        key_list = list(key1)
                        
        #for obj1 in Key.objects.filter(Key_2__in=key1):
        #    key_list.append(obj1.Key_1)
        for obj1 in get_objects_for_user(self.request.user, 'app.view_item'):
            result = self.request.user.has_perm('app.view_item', obj1)
            if result:   
                key_list.append(obj1.created_by_id)
        for obj2 in get_objects_for_user(self.request.user, 'app.add_item'):
            result = self.request.user.has_perm('app.add_item', obj2)
            if result:   
                key_list.append(obj2.created_by_id)
        #    user = User.objects.filter(full_name=self.request.user)
        #    item1 = Item1.objects.filter(created_by1_id=self.request.user.id)
        #    if key1.has_perm('app.view_item', obj1):
        #print(projects)
        #for obj1 in get_objects_for_user(key1, 'app.view_item'):
        #    print(obj1)
        #    key_list.append(obj1.user_id)

        #for obj2 in Key.objects.filter(Key_3__in=key1):
        #    key_list.append(obj2.Key_1)


        if self.request.user.is_superuser: # スーパーユーザの場合、リストにすべてを表示する。
            return Item.objects.all().order_by('-created_at')
        else:# 一般ユーザは自分のレコードのみ表示する。
            return Item.objects.filter(created_by_id__in=key_list)

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

        return redirect('update2', pk=item.pk)

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

        return redirect('update3', pk=item.pk)

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

        return redirect('update4', pk=item.pk)

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

        return redirect('update5', pk=item.pk)

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

        return redirect('update6', pk=item.pk)

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

        return HttpResponseRedirect(self.success_url)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update12', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update13', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update14', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update15', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update16', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update22', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update23', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update24', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update25', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return redirect('update26', pk=item.pk)

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
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)

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
