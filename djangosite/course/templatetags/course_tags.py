from django import template
from course.models import *

register = template.Library()


@register.inclusion_tag('course/groups_list.html')
def groups_list(class_selected=0, subject_selected='all'):
    class_list = Group.objects.all().order_by('-number')
    return {'class_list': class_list, 'class_selected': class_selected, 'subject_selected': subject_selected}


@register.inclusion_tag('course/subjects_list.html')
def subjects_list(class_selected=0, subject_selected='all'):
    subject_list = Subject.objects.all().order_by('name')
    return {'subject_list': subject_list, 'class_selected': class_selected, 'subject_selected': subject_selected}
