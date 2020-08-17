from technique.models import TechniqueItemFavorite,TechniqueItem
from chat.models import *
from techniqueOrder.models import *
from .models import Notification
import random
def check_profile(request):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    all_Technique = TechniqueType.objects.filter(is_active=True)
    if request.user.is_authenticated:
        user = request.user
        user.save()
        profile_ok = False
        #can_add_technique = True
        techniqueItemsFavorite = TechniqueItemFavorite.objects.filter(user=user)
        wishlist_ids = []
        for i in techniqueItemsFavorite:
            wishlist_ids.append(i.techniqueitem.id)
        my_technique = TechniqueItem.objects.filter(owner=user)
        my_technique_orders = TechniqueOrder.objects.filter(customer=user)
        my_tarif = user.tarif
        print('TARIF DELAY=',user.tarif.new_orders_delay)
        my_balance = user.balance
        # try:
        #     if my_tarif.technique_count <= user.technique_added:
        #         can_add_technique = False
        # except:
        #     pass
        try:
            can_call = my_tarif.can_call
            can_chat = my_tarif.can_chat
        except:
            can_call = False
            can_chat = False



        if user.phone and user.city and user.email:
            profile_ok = True
        allChats = Chat.objects.filter(users__in=[user.id])
        all_orders_apply = TechniqueOrderApply.objects.filter(user=user,is_choosen=False)
        allNotificatons = Notification.objects.filter(user=user,is_read=False,is_chat_notification=False)

        allUnreadChats = allChats.filter(isNewMessages=True).exclude(lastMsgBy=user)
        allReadChats = allChats.filter(isNewMessages=False)


    return locals()

