from django.contrib import admin
from modeltranslation.admin import TranslationAdmin,TranslationStackedInline
from .models import Category, Gallery, Videopholio, Advantages, Price, Globals, CaseGallery, CaseWork, Contacts


# class GalleryInline(admin.StackedInline):
class GalleryInline(TranslationStackedInline):
    model = Gallery
    extra = 0
    ordering = ['idsort', ]
    list_editable = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    # prepopulated_fields = {'imgTitle_ru': ('slug__categoryName',)}
    fieldsets = (
        ('Портфолио',
         {'fields': (
             ('imgTitle', 'idsort', 'slug', ('image_tag', 'categoryGallery'),),)}),
    )
    readonly_fields = ('image_tag',)
    sortable_field_name = "idsort"

class VideopholioInline(admin.TabularInline):
    # # class AdvantagesInline(TranslationAdmin):
    #
    model = Videopholio
    extra = 0
    ordering = ['idsort', ]
    list_editable = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    sortable_field_name = "idsort"

class AdvantagesInline(TranslationStackedInline):
    model = Advantages
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    sortable_field_name = "idsort"
    readonly_fields = ('image_tag',)
    fieldsets = (
            ('Тип фотосъемки',
             {'fields': ('advantagesTitle', ('idsort', 'position', 'status'), ('image_tag', 'advantagesImage'), 'advantagesText',), }),

        )

class PriceAdminInline(TranslationStackedInline):
    model = Price
    extra = 0
    # classes = ('grp-collapse grp-closed',)
    # inline_classes = ('grp-collapse grp-open',)
    sortable_field_name = "idsort"
    fieldsets = (
            ('Тип фотосъемки',
             {'fields': ('slug', ('priceBlockName', 'priceBlockCount', 'status',), 'idsort', 'priceBlockText',), }),

        )


# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(TranslationAdmin):
    list_display_links = ('id', 'categoryName',)
    list_display = ['id', 'categoryName', 'idsort', 'status', 'razdel', ]
    list_editable = ['idsort', 'status']
    ordering = ['razdel', 'idsort', ]
    list_filter = ('razdel', 'status',)
    prepopulated_fields = {'slug': ('categoryName',)}
    sortable_field_name = "idsort"

    fieldsets = (
        ('Услуга', {'fields': (
            'razdel', 'categoryName', ('slug', 'idsort', 'status'), 'keyWords', ( 'image_tag', 'categoryBanner',),
            'video',
            'introText',
            ),
        }),

    )
    readonly_fields = ('image_tag',)
    inlines = [
        AdvantagesInline,
        GalleryInline,
        VideopholioInline,
        PriceAdminInline
    ]

    class Media:
        js = (

            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',

            '/static/modeltranslation/js/force_jquery.js',
            '/static/modeltranslation/js/clearable_inputs.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
                '/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',
                       ),
        }
admin.site.register(Category, CategoryAdmin)


# class GalleryAdmn(TranslationAdmin):
#     list_display_links = ('slug', 'imgTitle_ru', 'imgTitle_uk', 'imgTitle_en', 'image_tag',)
#     list_display = ['image_tag', 'imgTitle_ru', 'imgTitle_uk', 'imgTitle_en', 'slug', 'idsort', ]
#     list_editable = ['idsort', ]
#     ordering = ['slug', 'idsort', ]
#     list_filter = ('slug',)
#     sortable_field_name = "idsort"
#     # prepopulated_fields = {'slug': ('categoryName',)}
#
#     fieldsets = (
#         ('Портфолио',
#          {'fields': ('slug', 'imgTitle', 'categoryGallery', 'image_tag',), }),
#     )
#     readonly_fields = ('image_tag',)
#
#     class Media:
#         js = (
#             '/static/tiny_mce/tiny_mce.js',
#             '/static/tiny_mce/tiny_mce_init.js',
#             '/static/modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
#             '/static/modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
#         }
# admin.site.register(Gallery, GalleryAdmn)


# class AdvantagesAdmin(TranslationAdmin):
#     list_display_links = ('advantagesTitle', 'slug',)
#     list_display = ['id', 'advantagesTitle', 'slug', 'position', 'idsort', 'status', ]
#     list_editable = ['idsort', 'position', 'status', ]
#     ordering = ['slug', 'idsort', ]
#     list_filter = ('slug', 'status', 'position',)
#     sortable_field_name = "idsort"
#     # prepopulated_fields = {'slug': ('categoryName',)}
#     fieldsets = (
#         ('Тип фотосъемки',
#          {'fields': ('slug', 'advantagesTitle', 'position', 'idsort', 'advantagesImage', 'advantagesText',), }),
#
#     )
#
#     class Media:
#         js = (
#             '/static/tiny_mce/tiny_mce.js',
#             '/static/tiny_mce/tiny_mce_init.js',
#             '/static/modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
#             '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',),
#         }
#
#
# admin.site.register(Advantages, AdvantagesAdmin)


# class PriceAdmin(TranslationAdmin):
#     list_display_links = ('priceBlockName', 'slug',)
#     list_display = ['id', 'priceBlockName', 'slug', 'idsort', 'status', ]
#     list_editable = ['idsort', 'status', ]
#     ordering = ['slug', 'idsort', ]
#     list_filter = ('slug', 'status',)
#     sortable_field_name = "idsort"
#     # prepopulated_fields = {'slug': ('categoryName',)}
#     fieldsets = (
#         ('Тип фотосъемки',
#          {'fields': ('slug', ('priceBlockName', 'priceBlockCount',), 'idsort', 'priceBlockText',), }),
#
#     )
#
#     class Media:
#         js = (
#             '/static/tiny_mce/tiny_mce.js',
#             '/static/tiny_mce/tiny_mce_init.js',
#             '/static/modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
#             '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',),
#         }
# admin.site.register(Price, PriceAdmin)


#


class CaseGalleryInline(admin.TabularInline):
    model = CaseGallery
    extra = 0
    ordering = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    fieldsets = (
        ('Портфолио',
         {'fields': ('link', 'idsort', 'imgAlt', 'Gallery', 'image_tag',), }),

    )
    sortable_field_name = "idsort"
    readonly_fields = ('image_tag',)


class CaseWorkAdmin(TranslationAdmin):
    list_display_links = ('id', 'title',)
    list_display = ['id', 'title', 'slug', 'idsort', 'status', ]
    list_editable = ['idsort', 'status']
    ordering = ['slug', 'idsort',]
    sortable_field_name = "idsort"
    list_filter = ('status', 'slug',)
    prepopulated_fields = {'link': ('title',)}

    fieldsets = (
        ('Кейс работ', {'fields': (('slug', 'idsort', 'status'), 'title', 'link', 'text',), }),

    )
    # readonly_fields = ('image_tag',)
    inlines = [
        CaseGalleryInline,
    ]

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(CaseWork, CaseWorkAdmin)


# class CaseGalleryAdmin(admin.ModelAdmin):
#     list_display_links = ('link', 'imgAlt',)
#     list_display = ['link', 'idsort', 'imgAlt', 'Gallery', 'image_tag', ]
#     list_editable = ['idsort']
#     list_filter = ('link',)
#     # prepopulated_fields = {'link': ('title',)}
#     ordering = ['idsort', ]
#     sortable_field_name = "idsort"
#
#     fieldsets = (
#         ('Портфолио',
#          {'fields': ('link', 'idsort', 'imgAlt', 'Gallery', 'image_tag',), }),
#
#     )
#     readonly_fields = ('image_tag',)
#
#
# admin.site.register(CaseGallery, CaseGalleryAdmin)


class ContactsAdmin(TranslationAdmin):
    list_display_links = ('id', 'name',)
    list_display = ['id', 'name', 'idsort', 'status', ]
    list_editable = ['idsort', 'status']
    # 'name', 'idsort', 'status', 'photo', 'tel', 'fb', 'insta',
    fieldsets = (
        ('Контакты', {'fields': ('name', 'tel', ('idsort', 'status',), 'photo', ('fb', 'insta',), 'about',), }),
    )

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
            '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Contacts, ContactsAdmin)
