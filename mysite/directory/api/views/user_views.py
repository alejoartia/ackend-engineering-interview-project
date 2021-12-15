from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from directory.api.filtersets import UsersFilterSet
from directory.api.serializers import UserSerializer
from directory.models import Company, User
import json
from rest_framework.filters import SearchFilter, OrderingFilter


class UsersViewSet(viewsets.ModelViewSet):
    """
    Endpoint for returning User data.
    """
    filterset_class = UsersFilterSet
    serializer_class = UserSerializer
    filter_backend = (SearchFilter,OrderingFilter)
    search_filter = ('pk','reports_to')

    @action(detail=True, methods=['get'])
    def reports(self, request, pk):
        user = self.get_object()
        users = user.reports.all()
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return User.objects.all()


    #We get the user related With the company id
    @api_view(['GET'])
    def get_Users(request, company_id):
        users = User.objects.filter(company=company_id) 
        serializer =  UserSerializer(users, many=True)
        return Response(serializer.data) 

    #get the reports _up_ to the user get_Hierarchy
    @api_view(['GET'])
    def get_Hierarchy(request, reports_to_id):
        users = User.objects.filter(reports_to=reports_to_id) 
        serializer =  UserSerializer(users, many=True)
        return Response(serializer.data) 


    #Managers is equal to get_Hierarchy_inv is what is shonw in the test
    # get the reports _down_ to the user get_Hierarchy
    @api_view(['GET'])
    def get_Hierarchy_inv(request, user_id):
        users = User.objects.filter(pk=user_id) 
        serializer =  UserSerializer(users, many=True)

        data = json.dumps(serializer.data)
        user=(json.loads(data.strip("[]")))
        print(user['reports_to'])
        user_id_inv=user['reports_to']

        users_inv = User.objects.filter(pk=user_id_inv) 
        serializer_inv =  UserSerializer(users_inv, many=True)
        return Response(serializer_inv.data)     
 
    