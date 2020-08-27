"""
Payment processor for Authorize.net.
"""
from .base import PaymentProcessorBase

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *
from django.conf import settings

class AuthorizeNetProcessor(PaymentProcessorBase):
    AUTHORIZE_CAPUTRE_TRANSACTION = "authCaptureTransaction"
    
    API_ENDPOINTS = [
        AUTHORIZE_CAPUTRE_TRANSACTION
    ]

    def __init__(self):
        self.merchantAuth = apicontractsv1.merchantAuthenticationType()

    def get_checkout_context(self, invoice, **kwargs):
        '''
        The Invoice plus any additional values to include in the payment record.
        '''
        self.merchantAuth.transactionKey = settings.AUTHORIZE_NET_TRANSACTION_KEY#'4tbEK65FB8Tht59Y'
        self.merchantAuth.name = settings.AUTHORIZE_NET_API_ID #'79MvGs6X3P'

    def auth_capture(self, invoice, card, kwargs):
        if not self.merchantAuth.name or not self.merchantAuth.transactionKey:
            return "error", False

        creditCard = apicontractsv1.creditCardType()

        creditCard.cardNumber = str(card.data['card_number'])
        creditCard.expirationDate = str("-".join([card.data['expire_year'],card.data['expire_month']]))
        creditCard.cardCode = str(card.data['cvv_number'])

        payment = apicontractsv1.paymentType()
        payment.creditCard = creditCard

        transactionrequest = apicontractsv1.transactionRequestType()
        transactionrequest.transactionType = AuthorizeNetProcessor.AUTHORIZE_CAPUTRE_TRANSACTION
        transactionrequest.amount = Decimal(invoice.total).quantize(Decimal('.00'), rounding=ROUND_DOWN)
        transactionrequest.payment = payment


        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = self.merchantAuth
        createtransactionrequest.refId = str("-".join([str(invoice.profile.pk), str(settings.SITE_ID), str(invoice.pk)]))

        createtransactionrequest.transactionRequest = transactionrequest
        createtransactioncontroller = createTransactionController(createtransactionrequest)
        createtransactioncontroller.execute()

        response = createtransactioncontroller.getresponse()
        
        if (response.messages.resultCode == "Ok"):
            return f"Transaction ID : {response.transactionResponse.transId}", True
        else:
            return f"response code: {response.messages.resultCode}", False

        
