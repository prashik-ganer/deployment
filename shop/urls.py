from django.urls import path
from shop import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("scan/", views.scan, name="scan"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/prod=<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("samplenew/", views.samplenew, name="samplenew"),
    path("signup/", views.handleSignup, name="handlesignup"),
    path("login/", views.handleLogin, name="handleLogin"),
    path("logout/", views.handleLogout, name="handleLogout"),
    path("category/", views.category, name="category"),
    path("category/<str:slug>", views.categorySlug, name="categorySlug"),
    path("stores/", views.stores, name="stores"),
    path("update_item/", views.updateItem, name="update_item"),
    path("qrcode/id=<int:order_id>", views.qrcode, name="qrcode"),
    
    path("all_products/", views.allProducts, name="allProducts"),
    path("all_products/<int:pk>", views.products_sellers, name="products_with_id"),
    
    
    path("all_orders/", views.allOrders, name="allOrders"),
    path("all_orders_create/", views.allOrders_create, name="allOrders_create"),
    path("all_orders_update/<int:pk>", views.allOrders_update, name="allOrders_update"),
    path("all_orders_delete/<int:pk>", views.allOrders_delete, name="allOrders_delete"),
    
    
    
    
    path("all_orders/<int:pk>", views.orders_sellers, name="SellerOrders"),
    # path("order_create/", views.OrderCreate, name="OrderCreate"),
    # path("order_update/", views.OrderUpdate, name="OrderUpdate"),
    # path("all_orders/<int:pk>", views.OrderDetails, name="OrderDetails"),
    
]
