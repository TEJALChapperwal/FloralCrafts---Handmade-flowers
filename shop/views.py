from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem

# ---------------------------
# Product Views
# ---------------------------

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

# ---------------------------
# Cart & Checkout
# ---------------------------

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("shop:cart")

def cart(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items, total = [], 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({"product": product, "quantity": quantity, "subtotal": subtotal})
    return render(request, "shop/cart.html", {"cart_items": cart_items, "total": total})

@login_required
@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return render(request, "shop/checkout.html", {"error": "Your cart is empty."})

    if request.method == "POST":
        user = request.user
        # Calculate grand total for the order
        grand_total = 0
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=int(product_id))
            grand_total += product.price * quantity

        # Create the order
        order = Order.objects.create(user=user, address=request.POST.get('address'), total=grand_total)

        # Create OrderItems
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=int(product_id))
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        # Clear cart
        request.session['cart'] = {}

        # Redirect to success page
        return redirect("shop:order_success")

    # GET request: show checkout summary
    cart_items = []
    grand_total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))
        subtotal = product.price * quantity
        grand_total += subtotal
        cart_items.append({"product": product, "quantity": quantity, "subtotal": subtotal})

    context = {"cart_items": cart_items, "grand_total": grand_total}
    return render(request, "shop/checkout.html", context)


from django.shortcuts import render

def order_success(request):
    return render(request, "shop/order_success.html")

# ---------------------------
# Authentication
# ---------------------------

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop:product_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('shop:product_list')
        else:
            return render(request, 'registration/login.html', {'error': "Invalid credentials."})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect("shop:product_list")
