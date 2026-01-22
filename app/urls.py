from django.urls import path

from .views import (dashboard, create_record, record_detail, update_record, delete_record, search, signup, signin, signout, page_404)

# Create your urls here.


urlpatterns = [
    # Record
    path("dashboard/", dashboard, name='dashboard'), # All records
    path("dashboard/<int:record_id>/", record_detail, name='record-detail'), # Individual record
    path("dashboard/create/", create_record, name="create-record"),# Create record
    path("dashboard/update/<int:record_id>/", update_record, name='update-record'), # Update record
    path("dashboard/delete/<int:record_id>/", delete_record, name='delete-record'), # Delete record
    path("search/", search, name='search'), # search record
    
    # Authentication
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
    
    path("404/", page_404, name="page-404"), # 404 Not Found 
]