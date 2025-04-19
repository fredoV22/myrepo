from django import forms

class StudentForm(forms.Form):
    gpa = forms.FloatField(label='GPA')
    attendance = forms.FloatField(label='Attendance Rate')
    income = forms.FloatField(label='Family Income')
    support = forms.BooleanField(label='Has Financial Support', required=False)
    mental_health = forms.IntegerField(label='Mental Health Score')
    activities = forms.BooleanField(label='Participates in Activities', required=False)
    materials = forms.BooleanField(label='Has Learning Materials', required=False)
    mode = forms.ChoiceField(choices=[('online', 'Online'), ('f2f', 'Face-to-Face'), ('hybrid', 'Hybrid')])
