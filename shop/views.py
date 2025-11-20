from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
=======
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
from .models import Product, Order, OrderItem

# ---------------------------
# Product Views
# ---------------------------

def product_list(request):
<<<<<<< HEAD
    # Search
    query = request.GET.get('q', '').strip()
    products_qs = Product.objects.all()
    if query:
        products_qs = products_qs.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products_qs.order_by('-created_at'), 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "shop/product_list.html", {"products": products, "query": query})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})

def product_edit(request, product_id):
    """Placeholder edit view: for now redirect back to product detail."""
    product = get_object_or_404(Product, id=product_id)
    # In a full app this would render an edit form. For now redirect to detail.
    return redirect('shop:product_detail', product_id=product.id)


def product_delete(request, product_id):
    """Placeholder delete view: for now redirect to product list.
    Deletion should be confirmed and restricted to staff in a real app.
    """
    # Do not delete automatically; just redirect to product list.
    return redirect('shop:product_list')
=======
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd

# ---------------------------
# Cart & Checkout
# ---------------------------

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("shop:cart")

<<<<<<< HEAD

def update_cart(request):
    """Update quantities in the session-based cart. Expects POST with product_id and quantity."""
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return redirect('shop:cart')

        cart = request.session.get('cart', {})
        if quantity <= 0:
            cart.pop(str(product_id), None)
        else:
            cart[str(product_id)] = quantity
        request.session['cart'] = cart
    return redirect('shop:cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('shop:cart')

=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
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
<<<<<<< HEAD
=======
@login_required
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
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

<<<<<<< HEAD
        # Create the order (Cash on Delivery only)
        order = Order.objects.create(user=user, address=request.POST.get('address'), total=grand_total, payment_method='cod')
=======
        # Create the order
        order = Order.objects.create(user=user, address=request.POST.get('address'), total=grand_total)
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd

        # Create OrderItems
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=int(product_id))
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

<<<<<<< HEAD
        # Clear cart and redirect to success
        request.session['cart'] = {}
=======
        # Clear cart
        request.session['cart'] = {}

        # Redirect to success page
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
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

<<<<<<< HEAD

# Online payment flow removed — only Cash on Delivery is supported now.


def about(request):
    """Render a static About page describing the business and values."""
    return render(request, "shop/about.html")


def contact(request):
    """Show a contact form and handle simple POSTs. We don't send email here; we display a thank-you page instead."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        context = {'name': name, 'email': email, 'message': message}
        return render(request, 'shop/contact_success.html', context)
    return render(request, 'shop/contact.html')

=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
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
