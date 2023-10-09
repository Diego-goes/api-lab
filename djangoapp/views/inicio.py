from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from ..controllers import inicio_controller

@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_urls_view(request):
    return inicio_controller.exibir_urls(request)
