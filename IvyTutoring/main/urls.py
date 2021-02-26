from django.urls import path
from main.views import *

urlpatterns = [
	path('', HomePage, name='Home Page'),
	path('signup/parent', ParentReg, name='Parent Registration'),
	path('signup/student', StudentReg, name='Student Registration'),
	path('signup/tutor', TutorReg, name='Tutor Registration'),
	path('login/', UserLogin, name='Login'),

]