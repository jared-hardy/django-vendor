from django.urls import path

from vendor.views import vendor as vendor_views

app_name = "vendor"

urlpatterns = [
    path('cart/', vendor_views.CartView.as_view(), name="cart"),
    path('cart/add/<slug:slug>/', vendor_views.AddToCartView.as_view(), name="add-to-cart"),
    path('cart/remove/<slug:slug>/', vendor_views.RemoveFromCartView.as_view(), name="remove-from-cart"),
    path('cart/summary/<int:pk>/', vendor_views.PaymentSummaryView.as_view(), name="purchase-summary"),

    # path('cart/remove/<slug:slug>/', vendor_views.TransactionSummary.as_view(), name="transaction-summary"),
    # path('cart-item/edit/<int:id>/', vendor_views.CartItemQuantityEditView.as_view(), name='vendor-cart-item-quantity-edit'),
    # path('retrieve/cart/', vendor_views.RetrieveCartView.as_view(), name='vendor-user-cart-retrieve'),
    # path('delete/cart/<int:id>/', vendor_views.DeleteCartView.as_view(), name='vendor-user-cart-delete'),
    # path('retrieve/order/<int:id>/', vendor_views.RetrieveOrderView.as_view(), name='vendor-user-order-retrieve'),
    # path('retrieve/purchase-item/<int:id>/', vendor_views.RetrievePurchaseView.as_view(), name='vendor-user-purchase-retrieve'),
    # path('retrieve/purchase/list/', vendor_views.RetrievePurchaseListView.as_view(), name='vendor-user-purchase-list'),
    # path('retrieve/order-summary/', vendor_views.RetrieveOrderSummaryView.as_view(), name='vendor-order-summary-retrieve'),
    # path('payment/processing/', vendor_views.PaymentProcessingView.as_view(), name='vendor-payment-processing'),
    # path('request/refund/<int:id>/', vendor_views.RequestRefundView.as_view(), name='vendor-request-refund'),
    # path('retrieve/refund/requests/', vendor_views.RetrieveRefundRequestsView.as_view(), name='vendor-retrieve-refund-requests'),
    # path('issue/refund/<int:id>/', vendor_views.IssueRefundView.as_view(), name='vendor-issue-refund'),
    
    path('checkout/account/', vendor_views.AccountInformationView.as_view(), name="checkout-account"),
    path('checkout/payment/', vendor_views.PaymentView.as_view(), name="checkout-payment"),
    path('checkout/review/', vendor_views.ReviewCheckoutView.as_view(), name="checkout-review"),

    path('customer/products/', vendor_views.ProductsListView.as_view(), name="customer-products"),
    path('customer/product/<int:pk>/receipt/', vendor_views.ReceiptDetailView.as_view(), name="customer-receipt"),
    path('customer/subscriptions/', vendor_views.SubscriptionsListView.as_view(), name="customer-subscriptions"),
    path('customer/subscription/<int:pk>/cancel/', vendor_views.SubscriptionCancelView.as_view(), name="customer-subscription-cancel"),
    path('customer/shipping/<int:pk>/update', vendor_views.ShippingAddressUpdateView.as_view(), name="customer-shipping-update"),               # TODO: [GK-3030] Do not use PKs in URLs

    # TODO: Add user's account mangement urls
    # TODO: add user's order details page
]
