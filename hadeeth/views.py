from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Hadeeth
from .serializers import HadeethSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class HadeethList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Hadeeth.objects.all()
    serializer_class = HadeethSerializer

class HadeethDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Hadeeth.objects.all()
    serializer_class = HadeethSerializer
