from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Gallery, Advantages, Price, CaseWork, Contacts, BlogPhoto

class CategoryTranslationOptions(TranslationOptions):
	fields = ('categoryName', 'keyWords', 'descriptions', 'introText')
	# empty_values = {'name': '', 'content': ''}
translator.register(Category, CategoryTranslationOptions)

class GalleryTranslationOptions(TranslationOptions):
	fields = ('imgTitle',)
translator.register(Gallery, GalleryTranslationOptions)

class AdvantagesTranslationOptions(TranslationOptions):
	fields = ('advantagesTitle', 'advantagesText')
translator.register(Advantages, AdvantagesTranslationOptions)

class PriceTranslationOptions(TranslationOptions):
	fields = ('priceBlockName', 'priceBlockText')
translator.register(Price, PriceTranslationOptions)


class CaseWorkTranslationOptions(TranslationOptions):
	fields = ('title', 'text', 'keyWords', 'descriptions',)
translator.register(CaseWork, CaseWorkTranslationOptions)

class ContactsTranslationOptions(TranslationOptions):
	fields = ('name', 'about',)
translator.register(Contacts, ContactsTranslationOptions)

class BlogPhotoTranslationOptions(TranslationOptions):
	fields = ('title', 'text', 'keyWords', 'descriptions',)
translator.register(BlogPhoto, BlogPhotoTranslationOptions)