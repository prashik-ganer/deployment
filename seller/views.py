from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from accounts.decorators import unauthenticated_user, allowed_users, admin_only

# Extra implemented
from .forms import OrderStatusForm, OrderUpdatesForm
from shop.models import Orders, Product, OrderUpdate, Customer_QR, SellerProductStock
from accounts.models import Seller, Order, Customer
import json
import pyqrcode
import requests
from .filters import OrdersFilter


from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def home(request):
    sellers =  Seller.objects.all()
    print(sellers)

    context = {'sellers': sellers}


    return render(request, 'seller/index.html', context)


@csrf_exempt
def seller_profile(request, seller_profile):   
    #     order_items_list.append(p)
    # print("order_items_list : ", order_items_list)
    # j = json.dumps(order_items_list)
    # print("order", order)
    
    thank = True
    seller = Seller.objects.get(id=seller_profile)
    # print(seller)
    order = seller.orders_set.all()
    seller_email = seller.seller_email
    seller_phone = seller.seller_phone
    # items_json = order.items_json
    order_count = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()

    # order_json = order.items_json
    orders_list=[]
    for orders in order:
        # print(orders)
        orders_list.append(orders)
        # x = {x.items_json for x in orders}                                       # Set comprehension
    print("orders_list")
    print("orders_list", orders_list)


    seller_orders_list=[]
    # CHecks order id to match it with airtable orders's id
    print("Seller orders list")
    for item in orders_list:
        # print(item.order_id)
        seller_orders_list.append(item.order_id)
        # pass
    print(seller_orders_list)
    myFilter = OrdersFilter(request.GET, queryset=order)
    order = myFilter.qs

    # cats = {(item.order_id:item.items_json) for item in orders_list}                                       # Set comprehension
    # print("cats : ", cats)
    # catprods = Product.objects.values('category', 'id')
    # # print(cats)
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])

    dicts = {}
    order_items_list = []
    for i in order:
        order_id = i.order_id
        items_json = i.items_json
        # print("order_id = ", order_id)
        # print("items_json = ", items_json)
        order_items_list.append(order_id)
        dicts[order_id]=items_json
    # print(dicts)
    dumped_dict = json.dumps(dicts)
    # print("dumped_dict", dumped_dict)
    replaced_dict = dumped_dict.replace("\\", " ")
    dicts1 = replaced_dict.replace("\"{","[{")
    dicts2 = dicts1.replace("}\"","}]")
    # print("dicts2",dicts2)

    get_headers = {
        'Authorization': 'Bearer keydq2SURfHCN4Aig'
        }

    url = 'https://api.airtable.com/v0/appJeyihmd9jyLKy1/TableNew?maxRecords=100&view=Orders'
    response = requests.get(url, headers=get_headers)
    # print(donors_response)
    data = response.json()
    # print(donors_data)
    dumps = json.dumps(data)
    # print(dumps)
    airtable_order_id = []
    airtable_order_status = []

    # Generating order id list and order status list from json received
    for j in data['records']:
        # Gets all order ids from airtable
        airtable_order_id.append(j['fields']['OrderId'])
        # Gets all order statuses from airtable
        airtable_order_status.append(j['fields']['OrderStatus'])

    print(airtable_order_id)
    # print(airtable_order_status)

    # Joiniing order ids withorder status
    airtable_dict = dict(zip(airtable_order_id,airtable_order_status))
    print("airtable_dict : ", airtable_dict)

    # Ids of seller orders that matched with airtable
    print("Ids of seller orders that matched with airtable with order status!")

    seller_order_status_dict = {}
    for i in seller_orders_list:
        # print("i   : ", i)
        for j in airtable_dict:
            # print("airtable_idct[j]   :", airtable_dict[j])
            if j == i:
                # print(j, airtable_dict[j])
                seller_order_status_dict[i] = airtable_dict[j]
    print(seller_order_status_dict)
    seller_order_with_status_str_one = json.dumps(str(seller_order_status_dict))
    json_seller_order_with_status_two = seller_order_with_status_str_one.replace("\'", "\"")
    json_seller_order_with_status_three = json_seller_order_with_status_two.replace("\"{", "{")
    json_seller_order_with_status_four = json_seller_order_with_status_three.replace("}\"", "}")
    print("json_seller_order_with_status_four", json_seller_order_with_status_four)
    json_seller_order_with_status = json.dumps(eval(json_seller_order_with_status_four))
    # one = json.dumps(str(json_seller_order_with_status_four))
    # json_seller_order_with_status = one.replace("\\\"", "\"")
    # json_seller_order_with_status = json_seller_order_with_status_four.replace("\"", "/")
    print(json_seller_order_with_status)
    # for i in orders_list:
    #     print(i.order_id)
    


    context={'replaced_New':dicts2,'order':order,'seller_email':seller_email, 'seller_phone':seller_phone, 'order_count':order_count, 'delivered':delivered, 'pending': pending,
            'myFilter':myFilter, 'json_seller_order_with_status':json_seller_order_with_status, 'thank':thank}

    return render(request, 'seller/seller_profile.html', context)


def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    print(orders)
    print(customers)

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers': customers, 
    'total_orders':total_orders, 'total_customers':total_customers,
    'delivered':delivered, 'pending':pending}
    return render(request, 'seller/dashboard.html', context)


def products(request):
    seller = request.user.seller
    print("seller : ", request.user.seller)
    products = Product.objects.filter(seller=seller)
    print(products)

    seller_product_stock = SellerProductStock.objects.filter(seller_ps=seller)
    print("seller_product_stock",seller_product_stock)

    # url = '/shop/seller_products/'
    # response = requests.get(url, headers=get_headers)

    context = {'products':products, 'seller_product_stock':seller_product_stock}
    # return HttpResponse("Products!")
    return render(request, 'seller/seller_products.html', context)

def sellerTracker(request, status):
    updates = OrderUpdate.objects.filter(order_id=status)
    allupdates = OrderUpdate.objects.filter(order_id=status)
    print("allupdates : ", allupdates)
    print("updates : ", updates)
    form  = OrderUpdatesForm()
    if request.method == 'POST':
        form = OrderUpdatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/seller')
    context = {'form':form}
    return render(request, 'seller/seller_tracker.html', context)

@csrf_exempt
def updateStatus(request, status):
    statusorder = Orders.objects.get(order_id=status)
    form = OrderStatusForm(instance=statusorder)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=statusorder)
        if form.is_valid():
            form.save()
            return redirect('/seller')
    context = {'form':form}
    return render(request, 'seller/update_status.html', context)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def updateOrderStatus(request):
    
    return JsonResponse('Order Status updated successfully!', safe=True)



