from django import forms
from django.forms.widgets import NumberInput


class ExampleForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    name = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placholder':'write your comment here'}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))  
    # value = forms.DecimalField()  

    # email_address = forms.EmailField( 
    #     required = False,
    # )

    message = forms.CharField(
	    max_length = 10,
    )

    email_address = forms.EmailField( 
        label="Please enter your email address",
    )

    first_name = forms.CharField(initial='Your name')

    # day = forms.DateField(initial=datetime.date.today)


    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)