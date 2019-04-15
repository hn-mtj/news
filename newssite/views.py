from urllib import response


from newssite.tasks import post_count_view
# Create your views here.
from newssite.models import Post
from newssite.models import Category
from taggit.models import Tag
from newssite.serializers import PostSerializer
from newssite.serializers import CategorySerializer
from django.http import Http404, JsonResponse
from newssite.serializers import TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
import requests
from rest_framework.permissions import IsAuthenticated


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        try:
            # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            # if x_forwarded_for:
            #     ip = x_forwarded_for.split(',')[0]
            # else:
            #     ip = request.META.get('REMOTE_ADDR')

            ip='185.212.195.122'
            url = "http://ip-api.com/json/"+ip

            headers = {
                'accept': "application/json",
                'content-type': "application/json"
            }
            queryset = self.queryset.order_by('-priority')

            response = requests.request("GET", url, headers=headers)
            if response.raise_for_status()== None:
                geo=response.json()
                if "city" in geo:
                    if geo["city"] == "Kermanshah":
                      queryset = queryset.filter(category=1)

            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("no result")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        post_count_view.delay(instance.id)
        return Response(serializer.data)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    paginate_by = 1
    permission_classes = (IsAuthenticated,)



class TagView(APIView):

    def list(request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)