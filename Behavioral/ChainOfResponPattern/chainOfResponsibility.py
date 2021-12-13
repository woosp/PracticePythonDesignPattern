class Handler:
    def __init__(self):
        self.next_handler = None

    def setNext(self, handler):
        self.next_handler = handler

    def handle(self, req):
        if self.next_handler:
            return self.next_handler.handle(req)
        return None


class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f"processing cash {req['amount']} won")
        else:
            print(f"CashHandler cannot process")
            super().handle(req)

class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'credit_card':
            print(f"processing credit card {req['amount']} won")
        else:
            print(f"CreditCard cannot process")
            super().handle(req)

class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debit_card':
            print(f"processing debit card {req['amount']} won")
        else:
            print(f"DebitCard cannot process")
            super().handle(req)


# test code
cash_handler = CashHandler()
credit_card_handler = CreditCardHandler()
debit_card_handler = DebitCardHandler()

cash_handler.setNext(credit_card_handler)
credit_card_handler.setNext(debit_card_handler)

payment = {
    'method': 'debit_card', 
    # 'method': 'paypal', 
    'amount': 10000
}

cash_handler.handle(payment)