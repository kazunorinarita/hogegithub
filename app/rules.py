from django.db import models
from .models import Item
from .models import Item1
from .models import Item2
from .models import Item3
from .models import Item4
from .models import Item5
from .models import Item6
from .models import Item7
from .models import Item8

import rules
import guardian

import rules

@rules.predicate
def is_item_owner(user, item):
    return item.created_by == user
@rules.predicate
def has_model_level_permission(user):
    return user.has_perm('app.change_item')

@rules.predicate
def has_object_level_permission(user, item):
    return user.has_perm('app.change_item', item)

rules.add_perm('app.rules_change_item', has_object_level_permission )

@rules.predicate
def is_item1_owner(user, item1):
    return item1.created_by1 == user

@rules.predicate
def has_object1_level_permission1(user, item1):
    return user.has_perm('app.view_item', item1)

rules.add_perm('app.rules_view_item1', has_object1_level_permission1 )

@rules.predicate
def is_item2_owner(user, item2):
    return item2.created_by2 == user

@rules.predicate
def has_model2_level_permission(user):
    return user.has_perm('app.change_item2')

@rules.predicate
def has_object2_level_permission2(user, item2):
    return user.has_perm('app.add_item', item2)

rules.add_perm('app.rules_add_item2', has_object2_level_permission2 )