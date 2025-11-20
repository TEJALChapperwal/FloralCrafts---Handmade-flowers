from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    # Edit/Delete placeholders (safe redirects for now)
    path("product/<int:product_id>/edit/", views.product_edit, name="product_edit"),
    path("product/<int:product_id>/delete/", views.product_delete, name="product_delete"),

    

    # Cart
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-success/", views.order_success, name="order_success"), 
    path("update-cart/", views.update_cart, name="update_cart"),
    path("remove-from-cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),

    # Auth
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
