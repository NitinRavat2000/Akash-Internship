from django.conf.urls import url
from BRMapp import views



urlpatterns = [
    url('view-books',views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('search-book',views.searchBook),
    url('new-book',views.newBook),
    url('submit',views.add),
    url('search',views.search),
    url('edit',views.edit),
    url('login' ,views.userlogin),
    url('logout' ,views.userlogout),
    ]
