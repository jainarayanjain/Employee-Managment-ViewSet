from django.urls import path
from user.views_with_customserializer import GetRequest

# urlpatterns = [
#     path('crudoperations/', views.GetRequest.as_view({'get':'listk','post':'create'}), name="list"),
#     path('crudoperations/<int:pk>/',views.GetRequest.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
# ]

urlpatterns = [
    path('crudoperations/', GetRequest.as_view({'get':'listk'}), name="list"),
    # path('crudoperations/<int:pk>/',GetRequest.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]
