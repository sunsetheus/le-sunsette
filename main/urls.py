from django.urls import path
from main.views import create_product_flutter, show_main, add_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increment_item, decrement_item, delete_item, get_item_json, add_item_ajax, delete_item_ajax, increment_item_ajax, decrement_item_ajax

app_name = 'main'
urlpatterns = [
  path('', show_main, name='show_main'),

  path('add_item', add_item, name='add_item'),
  path('xml/', show_xml, name='show_xml'), 
  path('json/', show_json, name='show_json'),
  path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
  path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 

  path('register/', register, name='register'),
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),
  path('increment_item/<int:id>/', increment_item, name='increment_item'),
  path('decrement_item/<int:id>/', decrement_item, name='decrement_item'),
  path('delete_item/<int:id>/', delete_item, name='delete_item'),
  path('get-item/', get_item_json, name='get_item_json'),
  path('create-ajax/', add_item_ajax, name='add_item_ajax'),
  path('delete_item_ajax/', delete_item_ajax, name='delete_item_ajax'),
  path('increment_item_ajax/', increment_item_ajax, name='increment_item_ajax'),
  path('decrement_item_ajax/', decrement_item_ajax, name='decrement_item_ajax'),
  path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]