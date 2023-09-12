from Account.models import Booking,Broker
def badges(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context=[]
        # Retrieve the count of items from your model
        item_count = Booking.objects.count()
        item_count_bro = Broker.objects.filter(status=0).count()

        
        
        return {'bro':item_count_bro,"pro":item_count}