from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.board, name = 'board'),
    path('library', views.library, name = 'library'),
    path('add_folder', views.add_folder_form, name = 'add_folder'),
    path('add_image', views.add_image_form, name = 'add_image'),
    path('category/<str:name>/<int:id>', views.category_image,name = 'category_image'),
    path('search', views.search, name = 'search'),
    path('tab_content/<int:id>', views.tab_content, name = 'tab_content'),
    path("ajax/", views.call_play_sound, name='call_play_sound'),
    path('settings', views.settings, name = 'settings')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)