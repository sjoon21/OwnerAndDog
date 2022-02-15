
import json
from os import stat

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
    
    def get(self, request):
        owners    = Owner.objects.all()
        results = []
        for owner in owners: 
            results.append(
                {
                    "name"  : owner.name, 
                    "age"   : owner.age,
                    "email" : owner.email
                    # Get owners information from DB
                    # Print out the name, age, and email
                }
            )
        return JsonResponse({'results':results}, status=200)
    
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs  = [
                {"DogName": dog.name} for dog in Dog.objects.filter(owner_id = owner.id)
            ]
            # Add Dog list into owners' info.
            results.append(
                {
                    "owner_name"       : owner.name,
                    "owner_age"        : owner.age,
                    "dog_list"         : dogs
                }
            )
        return JsonResponse({'results' : results}, status=200)
        

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

    def get(self, request):
        dogs    = Dog.objects.all()
        results = []
        for dog in dogs: 
            results.append(
                {
                    "name"  : dog.name, 
                    "age"   : dog.age,
                    
                }
            )
        return JsonResponse({'results':results}, status=200)