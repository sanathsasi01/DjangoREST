from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerializer

@api_view(['GET', ])
def api_detail_blog_view(request, id):

    try: 
        blog_post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


# Update
@api_view(['PUT'])
def api_update_blog_view(request, id):

    try: 
        blog_post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success' : "Updated successfully"
            }
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete
@api_view(['DELETE'])
def api_delete_blog_view(request, id):

    try: 
        blog_post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        if operation:
            data = {
                'success' : 'Successfully deleted'
            }
        else:
            data = {
                'failure' :  'delete failed'
            }
        return Response(data=data)