from django.urls import path

from vendor import views

urlpatterns = [
    path('add-to-cart/', views.AddToCartView.as_view(), name="vendor-add-to-cart"),
    path('add-to-cart/<str:sku>/', views.NewAddToCartView.as_view(), name="vendor-new-add-to-cart"),
    path('cart-item/edit/<int:id>/', views.CartItemQuantityEditView.as_view(), name='vendor-cart-item-quantity-edit'),
    path('removefromcart/<str:sku>/', views.RemoveFromCartView.as_view(), name="vendor-remove-from-cart"),
    path('retrieve/cart/', views.RetrieveCartView.as_view(), name='vendor-user-cart-retrieve'),
    path('delete/cart/<int:id>/', views.DeleteCartView.as_view(), name='vendor-user-cart-delete'),
    path('retrieve/order/<int:id>/', views.RetrieveOrderView.as_view(), name='vendor-user-order-retrieve'),
    path('retrieve/purchase-item/<int:id>/', views.RetrievePurchaseView.as_view(), name='vendor-user-purchase-retrieve'),
    path('retrieve/purchase/list/', views.RetrievePurchaseListView.as_view(), name='vendor-user-purchase-list'),
    path('retrieve/order-summary/', views.RetrieveOrderSummaryView.as_view(), name='vendor-order-summary-retrieve'),
    path('payment/processing/', views.PaymentProcessingView.as_view(), name='vendor-payment-processing'),
    path('request/refund/<int:id>/', views.RequestRefundView.as_view(), name='vendor-request-refund'),
    path('retrieve/refund/requests/', views.RetrieveRefundRequestsView.as_view(), name='vendor-retrieve-refund-requests'),
    path('issue/refund/<int:id>/', views.IssueRefundView.as_view(), name='vendor-issue-refund'),

]
