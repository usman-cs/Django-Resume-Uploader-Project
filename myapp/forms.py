from django import forms
from .models import Resume

GENDER_CHOICE = [
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE = [
    ('Wah','Wah'),
    ('Islamabad','Islamabads')
]
class ResumeForm(forms.ModelForm):    
    gender = forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect(attrs={}))
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple( ))
    class Meta:
        model = Resume
        fields = ['id','name','dob','gender','locality','city','pin','state','mobile','job_city',
    'profile_image','my_file']
        labels = {'name':"Full Name ",'dob':'Date of Birth ','pin':'Pin Code ','mobile':'Mobile Number ',
                'state':'State ','job_city':'Job City ','profile_image':'Profile Image ','my_file':'Document ','email':'Email '
                ,'city':'City ','gender':'Gender '}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}   ),
            'city':forms.TextInput(attrs={'class':'form-control'}   ),
            'pin':forms.NumberInput(attrs={'class':'form-control'}  ),
            'state':forms.Select(attrs={'class':'form-control'} ),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}   ),
            'email':forms.EmailInput(attrs={'class':'form-control'} ),
            'my_file':forms.FileInput(attrs={})
        }

