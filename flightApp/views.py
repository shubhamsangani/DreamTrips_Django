
from django.shortcuts import render, redirect
from DreamTrips import *
from flightApp.models import *
from hotelApp.models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  #for File storage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.utils import timezone
import random
import string
import os
import io
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def flightFun(request):
    context = {
            "header" : "header header-dark",
            "mainheaderClass" : "nav-brand static-show",
            "headerClass" : "mob-show",
            "listheader" : "list-buttons light",
            "alistheader" : "",

        }
    try:
        userDetails = request.session.get("userinfo")
        flightdata = flightModel.objects.filter(flight_is_active=True).values()
        flightdetailsdata = flightDetailsModel.objects.filter(flightDetails_is_active=True)
        flightFacilitiesdata = flightFacilitiesModel.objects.filter(flightFacilities_is_active=True).values()
        
        if userDetails:
            return render(request, 'flight_list.html', {"flightdata":flightdata,"flightFacilitiesdata":flightFacilitiesdata,"flightdetailsdata" : flightdetailsdata,"userDetails": userDetails, "context": context, "flag": 1})
        else:
            return render(request, 'flight_list.html', {"flightdata":flightdata,"flightFacilitiesdata":flightFacilitiesdata,"flightdetailsdata" : flightdetailsdata,"context": context, "flag": 0})
    except Exception as e:
        print(e)
        return render(request, 'error404.html')

def flightdetailFun(request, flightClass_id):
    context = {
        "header": "header header-dark",
        "mainheaderClass": "nav-brand static-show",
        "headerClass": "mob-show",
        "listheader": "list-buttons light",
        "alistheader": "",
    }
    try:
        # Get user info from session
        userDetails = request.session.get("userinfo")

        flightclassdata = flightClassModel.objects.get(pk=flightClass_id)
        request.session["selected_flight_id"] = flightclassdata.flightClass_id

        if userDetails:
            return render(request, 'flight_detail.html', {"flightclassdata": flightclassdata, "userDetails": userDetails, "context": context, "flag": 1})
        else:
            return render(request, 'flight_detail.html', {"flightclassdata": flightclassdata, "context": context, "flag": 0})
    except Exception as e:
        print(e)
        return render(request, 'error404.html')

def flightclassFun(request, flightDetails_id):
    context = {
        "header": "header header-dark",
        "mainheaderClass": "nav-brand static-show",
        "headerClass": "mob-show",
        "listheader": "list-buttons light",
        "alistheader": "",
    }
    try:
        # Get user info from session
        userDetails = request.session.get("userinfo")

        flightdetailsdata = flightDetailsModel.objects.get(pk=flightDetails_id)
        flightclassdata = flightClassModel.objects.filter(flightDetails=flightdetailsdata, flightClass_is_active=True)

        if userDetails:
            return render(request, 'flight_class.html', {"flightclassdata": flightclassdata, "flightdetailsdata": flightdetailsdata, "userDetails": userDetails, "context": context, "flag": 1})
        else:
            return render(request, 'flight_class.html', {"flightclassdata": flightclassdata, "flightdetailsdata": flightdetailsdata, "context": context, "flag": 0})

    except Exception as e:
        print(e)
        return render(request, 'error404.html')

