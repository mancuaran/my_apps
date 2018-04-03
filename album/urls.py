from django.conf.urls import include, url 
from album import views


urlpatterns = (
	url(r'^$', views.base, name='base'),
	url(r'^category/$', views.category, name='category-list'),
	url(r'^category/(?P<category_id>\d+)/detail/$', views.category_detail,
		name='category_detail'),
	url(r'^photo/$', views.PhotoListView.as_view(),
		name='photo_list'),
	url(r'^photo/(?P<pk>\d+)/detail/$', views.PhotoDetailView.as_view(),
		name='photo_detail'),
	url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(),
		name='photo-update'),

	url(r'^photo/create/$', views.PhotoCreate.as_view(), 
		name='photo-create'),
	url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(),
		name='photo-delete'),

)