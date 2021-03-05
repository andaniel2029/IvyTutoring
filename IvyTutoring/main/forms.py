from django.utils import timezone
from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ParentForm(UserCreationForm):
	email = forms.EmailField(label='Email', help_text='Email Required')
	date_birth = forms.DateField(label='Date Of Birth', widget = forms.SelectDateWidget(years=range(1900, (int(timezone.localtime().year)))))

	class Meta:
		model = User
		fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'date_birth']

	def save(self, commit=True):
		parent = super(ParentForm, self).save(commit=False)
		parent.user_type = 1
		parent.is_active = False
		if commit:
			parent.save()
		return parent

class contactForm(forms.Form):
	user_choices = [
	('',''),
	('parent', 'Parent'),
	('student', 'Student'),
	('tutor', 'Tutor')
	]
	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	email = forms.EmailField(label='Email')
	user_type = forms.CharField(label='Are You: ', widget=forms.Select(choices=user_choices))
	subject = forms.CharField(label='Subject')
	message = forms.CharField(label='Message')

# class StudentForm(UserCreationForm):
# 	date_birth = forms.DateField(label='Date Of Birth', widget = forms.SelectDateWidget(years=range(1900, (int(timezone.localtime().year)))))

# 	class Meta:
# 		model = User
# 		fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'date_birth']

# 	def save(self, commit=True):
# 		student = super(StudentForm, self).save(commit=False)
# 		student.user_type = 1
# 		if commit:
# 			student.save()
# 		return student

# class TutorForm(UserCreationForm):
# 	date_birth = forms.DateField(label='Date Of Birth', widget = forms.SelectDateWidget(years=range(1900, (int(timezone.localtime().year)))))

# 	class Meta:
# 		model = User
# 		fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'date_birth']

# 	def save(self, commit=True):
# 		tutor = super(TutorForm, self).save(commit=False)
# 		tutor.user_type = 1
# 		if commit:
# 			tutor.save()
# 		return tutor