from .models import *


class DataMixin:
    model = Book
    paginate_by = 6