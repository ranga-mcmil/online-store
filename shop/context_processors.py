from .models import Category


def categories_processor(request):
    categories = Category.objects.all()
    category = None
    return {'categories': categories, 'category': category}
