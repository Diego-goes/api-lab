from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from ..permissions import Professor 
from rest_framework.permissions import AllowAny
from ..models import Lab
from ..serializers import LabSerializer
import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

def decode_token(token):
    # try:
        # A chave secreta usada para assinar o token JWT
        secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
        
        # Decodifica o token
        algorithm = settings.SIMPLE_JWT["ALGORITHM"]
        # Teste
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNSwidXNlcm5hbWUiOiJQcm9mZXNzb3IiLCJ1c2VyX3R5cGVfaWQiOjEsImV4cCI6MTY5NTY4NjQwMH0.mdxFtNeF7jvDfIyeYi4LVl-BIivG4w0P339y7k8RwDs"
        # secret_key = "cfh58$*%jf*%584mf*4jJf8J*&fh789J*H)$#-3JFej()(#_)mf#*(593)"
        # algorithm = "HS256"

        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        print(f'PAYLOD: {payload}')
        
        # O 'payload' agora contém as informações do token decodificado
        return payload
    # except jwt.ExpiredSignatureError:
    #     raise AuthenticationFailed('Token expirado. Faça login novamente.')
    # except jwt.DecodeError:
    #     raise AuthenticationFailed('Token inválido. Faça login novamente.')


@api_view(["GET"])
# @permission_classes([Professor])
def getData(request):
    token = request.META.get("HTTP_AUTHORIZATION").split("Bearer ")[1]
    token = token.replace('"', '')
    print(f'TOKEN: {token}')
    payload = decode_token(token)
    print(request.user)
    labs = Lab.objects.all()
    serializer = LabSerializer(labs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([Professor])
def getLab(request, pk):
    labs = Lab.objects.get(id=pk)
    serializer = LabSerializer(labs, many=False)
    return Response(serializer.data)


@api_view(["POST"])
# @permission_classes([Professor])
def addLab(request):
    dados = request.data
    if "andar" in dados and "lab" in dados:
        andar = dados["andar"]
        lab = dados["lab"]

        try:
            if Lab.objects.filter(andar=andar).exists():
                return Response({f"O Lab tem já está registrado no andar {andar}."})
            
        except Lab.DoesNotExist:
            return Response({"Laboratório não encontrado."})

        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response({"mensagem": "Existem campos faltando."})

@api_view(["POST"])
def inativarLab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        if lab.is_active == 1:
            lab.is_active = 0
            lab.save()
            return Response({f"Lab inativado com sucesso!"})
        else:
            return Response({f"Lab ja estava inativado!"})
    except Lab.DoesNotExist:
        return Response({"Laboratório não encontrado"})


@api_view(["POST"])
def ativarLab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        if lab.is_active == 0:
            lab.is_active = 1
            lab.save()
            return Response({"Lab ativado com sucesso!"})
        else:
            return Response({"Lab ja estava ativado!"})
    except Lab.DoesNotExist:
        return Response({"Laboratório não encontrado"})


@api_view(["PUT"])
def updateLab(request, pk):
    lab = Lab.objects.get(id=pk)
    serializer = LabSerializer(instance=lab, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteLab(request, pk):
    lab = Lab.objects.get(id=pk)
    lab.delete()
    return Response("Lab successfully deleted!")