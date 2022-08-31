from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import logout
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_200_OK, template_name='menu.html')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    permission_classes = (AllowAny,)


    def get(self, request, *args, **kwargs):
        return Response(template_name='home.html')

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if is_ajax(request):
            return Response(template_name='home.html')

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    permission_classes = (AllowAny,)

    def post(self, request):
        if is_ajax(request):
            email = request.data.get('email')
            password = request.data.get('password')

            if email and password:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    request.user.id
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        if is_ajax(request):
            return Response(template_name='home.html')

class MenuView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu.html'

    def get(self, request):

        query = Item.objects.all()
        queries = Order.objects.all()
        queryset = Cart.objects.all()
        serializer_item = ItemSerializer(query, many=True)
        serializer = CartItemSerializer(queryset, many=True)
        serializer_order= OrderViewSerializer(queries, many=True)
        print(request.user.id)
        return Response({'data': serializer_item.data, 'cart': serializer.data, 'orders': serializer_order.data})

        
class CartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu.html'
    permission_classes = (AllowAny,)

    def post(self, request):
        if is_ajax(request):
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(request.user.id)
                return Response({'cart': serializer.data}, template_name='menu.html')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if is_ajax(request):
            item= Cart.objects.filter(item=id).first()
            if item:
                item.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrderView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu.html'
    permission_classes = (AllowAny,)

    def post(self, request):
        if is_ajax(request):
            serializer = OrderCreationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(request.user.id)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if is_ajax(request):
            query = Order.objects.all()
            serializer = OrderViewSerializer(query, many=True)
            return Response({'order': serializer.data}, template_name='menu.html')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OrderCreationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu.html'
    permission_classes = (AllowAny,)

    def post(self, request):
        if is_ajax(request):
            serializer = OrderCreationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(request.user.id)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





    