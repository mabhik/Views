from django import forms

class student(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    email=forms.EmailField(max_length=40)