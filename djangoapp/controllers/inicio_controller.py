from rest_framework.response import Response

routes = [
    {
        "url": "login/",
        "methods": ["POST"],
        "body": {
            "cpf_cnpj": "string",
            "password": "string"
        }
    },
    {
        "url": "users/",
        "methods": ["GET"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "users/create",
        "methods": ["POST"],
        "body": {
            "username": "string_unique",
            "name": "string",
            "email": "string",
            "user_type_id": "int",
            "password": "string",
            "is_active": "int",
            "cpf_cnpj": "string",
            "phone": "string"
        }
    },
    {
        "url": "users/read/<str:pk>",
        "methods": ["GET"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "users/update/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
        "body": {
            "username": "string_unique",
            "name": "string",
            "email": "string",
            "user_type_id": "int",
            "password": "string",
            "is_active": "int",
            "cpf_cnpj": "string",
            "phone": "string"
        }
    },
    {
        "url": "users/delete/<str:pk>",
        "methods": ["DELETE"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "users/inativar/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "users/ativar/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "labs/",
        "methods": ["GET"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "labs/create",
        "methods": ["POST"],
        "authorization": "Bearer (token)",
        "body": {
            "andar": "int",
            "lab": "string",
            "description": "string",
            "is_active": "int"
            }
    },
    {
        "url": "labs/read/<str:pk>",
        "methods": ["GET"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "labs/update/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
        "body": {
            "andar": "int",
            "lab": "string",
            "description": "string",
            "is_active": "int"
            }
    },
    {
        "url": "labs/delete/<str:pk>",
        "methods": ["DELETE"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "labs/inativar/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "labs/ativar/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
    },
    {
        "url": "reslabs/",
        "methods": ["GET"],
        "authorization": "Bearer (token)"
    },
    {
        "url": "reslabs/create",
        "methods": ["POST"],
        "authorization": "Bearer (token)",
        "body": {
            "lab_id": "int",
            "user_id": "int",
            "res_date": "timestamptz"
            }
    },
    {
        "url": "reslabs/read/<str:pk>",
        "methods": ["GET"],
        "authorization": "Bearer (token)"
    },
    {
        "url": "reslabs/update/<str:pk>",
        "methods": ["PUT"],
        "authorization": "Bearer (token)",
        "body": {
            "lab_id": "int",
            "user_id": "int",
            "res_date": "timestamptz"
            }
    },
    {
        "url": "reslabs/delete/<str:pk>",
        "methods": ["DELETE"],
        "authorization": "Bearer (token)"
    }
]
def exibir_urls(request):
    return Response(routes)
