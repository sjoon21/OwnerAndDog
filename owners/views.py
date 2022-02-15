
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name = data['name'],
            age = data['age'],
            email = data['email']
            # Post owners information (name, age, and email)
        ) 

        return JsonResponse({'message':'created'}, status=201)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        # Dogs require Owners info. in order to exist in DB
        
        # if not Owner.objects.filter(id = data['owner_id']).exists:
        #      return JsonResponse({'message':'Owner not found'}, status=404)
            # If dog does not have any owner_id then it should not exist,
            # Make excetption for non owner_id and show 404 status to inform.

        owner = Owner.objects.get(name = data['owner'])
        
        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = owner
            # Post dogs informations into DB
        )

        return JsonResponse({'message':'created'}, status=201)