from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from . import maths
from django.http import JsonResponse
import re

@api_view(["GET"])
@permission_classes([AllowAny])
def class_number(request):
    number = request.query_params.get("number")


    if number is None:
        return JsonResponse({"number": None, "error": True},
                        status=status.HTTP_400_BAD_REQUEST,)
    
    #if no number is inputed
    if not re.match(r"^-?\d+$", number):
        return JsonResponse(
            {"message": number, "error": True},
            status=status.HTTP_400_BAD_REQUEST,
        )
    

     #convert 'number' to an integer
    number = int(number)

    data = {
        "number": number,
        "is_prime": maths.num_prime(abs(number)),
        "is_perfect": maths.num_perfect(abs(number)),
        "properties":maths.num_properties(abs(number)),
        "digit_sum": maths.sum_of_digits(abs(number)),
        "fun_fact":maths.get_funfact_for_number(number)
    }

    return JsonResponse(data=data, status=status.HTTP_200_OK)


