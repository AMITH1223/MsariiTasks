from rest_framework import viewsets
from .models import Task, UserData, StudyGroup, CommunityForum
from .serializers import TaskSerializer, UserDataSerializer, StudyGroupSerializer, CommunityForumSerializer
from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.impute import SimpleImputer 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserDataSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

class CommunityForumViewSet(viewsets.ModelViewSet):
    queryset = CommunityForum.objects.all()
    serializer_class = CommunityForumSerializer


def getdata(request):
    # Annotate each user with a count of occurrences and then filter to get unique names
    unique_user_data = UserData.objects.values('name').annotate(name_count=Count('name')).order_by()
    return render(request, 'prediction.html', {'unique_user_data': unique_user_data})


def postdata(request):
    if request.method == 'POST':
        selected_user = request.POST.get('selected_user')
        try:
            # Retrieve all data entries for the selected user
            user_data_entries = UserData.objects.filter(name=selected_user)
            
            if not user_data_entries.exists():
                return JsonResponse({'error': f'No user found with the name: {selected_user}'})
            
            # Initialize counts for interests
            backend_interest_count = 0
            frontend_interest_count = 0
            
            # Iterate through each data entry for the user and count interests
            for entry in user_data_entries:
                interests = entry.interests.split(',') if entry.interests else []
                backend_interest_count += interests.count("Backend")
                frontend_interest_count += interests.count("Frontend")
            
            print('data1', backend_interest_count)
            print('data2', frontend_interest_count)
            
            
            # Prepare data (this is just a placeholder, you should replace this with actual data preparation)
            X = np.array([[10], [20], [30], [40], [50]])  # Example data
            y = np.array([0, 1, 0, 1, 1])  # Example labels
            
            # Train model
            model = LogisticRegression()
            model.fit(X, y)
            
            # Make predictions
            backend_prediction = model.predict([[backend_interest_count]])
            frontend_prediction = model.predict([[frontend_interest_count]])
            
            # Print prediction percentage
            backend_prediction_percentage = model.predict_proba([[backend_interest_count]])[0][1] * 100
            frontend_prediction_percentage = model.predict_proba([[frontend_interest_count]])[0][1] * 100
            print(f"Prediction Percentage for {selected_user} (Backend): {backend_prediction_percentage}%")
            print(f"Prediction Percentage for {selected_user} (Frontend): {frontend_prediction_percentage}%")
            
            # Return prediction percentages
            return JsonResponse({'selected_user': selected_user, 'backend_prediction_percentage': backend_prediction_percentage, 'frontend_prediction_percentage': frontend_prediction_percentage})
        except UserData.DoesNotExist:
            return JsonResponse({'error': f'No user found with the name: {selected_user}'})
    else:
        return JsonResponse({'error': 'Invalid request method'})







