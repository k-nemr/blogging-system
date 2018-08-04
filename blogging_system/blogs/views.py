from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blogs.models import Blog
from blogs.serializers import BlogSerializer


# Create your views here.

@api_view(['GET'])
def list_blogs(request):
    """
    List  blogs.
    """
    next_page = 1
    previous_page = 1
    blogs = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    serializer = BlogSerializer(data, context={'request': request}, many=True)
    if data.has_next():
        next_page = data.next_page_number()
    if data.has_previous():
        previous_page = data.previous_page_number()

    return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages,
                     'nextlink': '/api/blogs/?page=' + str(next_page),
                     'prevlink': '/api/blogs/?page=' + str(previous_page)})


@api_view(['POST'])
def create_blog(request):
    """
    Create a new blog.
    """
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
