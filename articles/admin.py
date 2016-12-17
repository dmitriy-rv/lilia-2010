from django.contrib import admin
from articles.models import Article, Excursions, Houses, Image
from image_cropping import ImageCroppingMixin

# Register your models here.

admin.site.register(Article)

class InlineImage(admin.TabularInline):
    model = Image

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass

class CelebrityAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [InlineImage]
    pass


admin.site.register(Excursions, MyModelAdmin)
admin.site.register(Houses, CelebrityAdmin)