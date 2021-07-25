from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
# Create your views here.


@api_view(['POST'])
def create_place(request, place):

    place_name = request.data.get('place_name')
    coordinates = request.data.get('coordinates')
    # place = request.data.get('place')
    if place == 'P':
        try:
            province = Province.objects.create(name=place_name)
        except Exception as e:
            return Response({"message": "can not create the province", "error": str(e)}, status=500)
        return Response({"message": "province created", "code": province.code})
    elif place == 'D':
        province_code = request.data.get('province_code')
        try:
            province = Province.objects.get(code=province_code)
        except Exception as e:
            return Response({f"message": f"no province with code {province_code} found."}, status=500)
        try:
            district = District.objects.create(name=place_name, province=province, coordinates=coordinates)
        except Exception as e:
            return Response({"message": "can not create the district", "error": str(e)}, status=500)
        return Response({"message": "district created", "code": district.code})

    elif place == 'S':
        district_code = request.data.get('district_code')
        try:
            district = District.objects.get(code=district_code)
        except Exception as e:
            return Response({f"message": f"no district with code {district_code} found."}, status=500)
        try:
            sector = Sector.objects.create(name=place_name, district=district, coordinates=coordinates)
        except Exception as e:
            return Response({"message": "can not create the sector", "error": str(e)}, status=500)
        return Response({"message": "sector created", "code": sector.code})

    elif place == 'C':

        sector_code = request.data.get('sector_code')
        try:
            sector = Sector.objects.get(code=sector_code)
        except Exception as e:
            return Response({f"message": f"no sector with code {sector_code} found."}, status=500)
        try:
            cell = Cell.objects.create(name=place_name, sector=sector, coordinates=coordinates)
        except Exception as e:
            return Response({"message": "can not create the cell", "error": str(e)}, status=500)
        return Response({"message": "cell created", "code": cell.code})

    elif place == 'V':

        cell_code = request.data.get('cell_code')
        try:
            cell = Sector.objects.get(code=cell_code)
        except Exception as e:
            return Response({f"message": f"no cell with code {cell_code} found."}, status=500)
        try:
            village = Village.objects.create(name=place_name, cell=cell, coordinates=coordinates)
        except Exception as e:
            return Response({"message": "can not create the village", "error": str(e)}, status=500)
        return Response({"message": "village created", "code": village.code})

