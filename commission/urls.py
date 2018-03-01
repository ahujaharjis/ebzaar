from django.conf.urls import url

from . import views

app_name = 'commission'
urlpatterns = [
    url(r'^gstno_change/(?P<name>[\w ]+)/$',views.gstno_change,name='gstno_change'),
    url(r'^commission/$',views.home_commission,name="home_commission"),
    url(r'^default_rate/(?P<name>[\w ]+)/$',views.default_rate,name="default_rate"),
    url(r'^concessional_rate/(?P<name>[\w ]+)/$',views.concessional_rate,name="concessional_rate"),
    url(r'^promo_rate/(?P<name>[\w ]+)/$',views.promo_rate,name="promo_rate"),

    url(r'^reimbursement/(?P<name>[\w ]+)/$',views.reimbursement,name="reimbursement"),
    url(r'^ajax_calls/myFunction/$', views.myFunction),
    url(r'^deliver_zone/(?P<name>[\w ]+)/$',views.delivery_zone,name="delivery_zone"),
    url(r'^penalty_reason_list/(?P<name>[\w ]+)/$',views.penalty_reason_list,name="penalty_reason_list"),
    url(r'^penalty_list/(?P<name>[\w ]+)/$',views.penalty_list,name="penalty_list"),
    url(r'^addcommrate/(?P<name>[\w ]+)/$',views.addcommrate,name="addcommrate"),
    url(r'^store_detail/(?P<name>[\w ]+)/$',views.store_detail,name="store_detail"),
    url(r'^comm_calc/$',views.comm_calc,name="comm_calc"),
 ]