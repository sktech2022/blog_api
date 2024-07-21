from rest_framework.views import APIView,Response
from .serializers import *
from rest_framework import status
from .models import *

class BlogData(APIView):
    def get(self,request):
        blogs=Blog.objects.all()
        serializer = BlogSerializers(blogs,many=True)
        return Response(
            {
                    "success" : True,
                    'data':serializer.data,
                    "message": "Blogs List",
                    "error":None
                },
            status=status.HTTP_200_OK
        )
    def post(self,request):
        print(request.data)
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success" : True,
                    'data':serializer.data,
                    "message": "Blog Created",
                    "error":None
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                    {
                        'success': False,
                        'data': None, 
                        'message': 'Blog NOT Created',
                        'errors': serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )  
            
class BlogView(APIView):
    def put(self,request,id):
        blog=Blog.objects.filter(id=id).first()
        serializer=BlogSerializers(data=request.data,instance=blog,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'data': serializer.data, 
                    'message': 'Blog updated',
                    'errors': None
                },
                status=status.HTTP_200_OK
            )
        else:
             return Response(
                    {
                        'success': False,
                        'data': None, 
                        'message': 'Blog not updated',
                        'errors': serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )  
        
    def delete(self,request,id):
        blog=Blog.objects.filter(id=id).first()
        blog.delete()
        return Response(
                {
                    'success': True,
                    'data': None, 
                    'message': 'Blog Deleted',
                    'errors': None
                },
                status=status.HTTP_200_OK
            )