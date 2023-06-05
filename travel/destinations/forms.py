from django import forms

#MultipleChoiceField

class LocationForm(forms.Form):
    temperature_selection = [
        ('1', '0 - 10°C'),
        ('2', '10 - 15°C'),
        ('3', '15 - 20°C'),
        ('4', '20 - 25°C'),
        ('5', '⩾ 25°C')
    ]

    hotel_price_selection = [
        ('1', '0 - 50 EUR'),
        ('2', '50 - 75 EUR'),
        ('3', '75 - 100 EUR'),
        ('4', '⩾ 100 EUR'),
    ]

    choices = [
        (True, 'Yes'),
        (False, 'No'),
        ('None', 'Whatever')
    ]

    continent_choice = [
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('North America', 'North America'),
        ('South America', 'South America'), 
        ('Australia', 'Australia'),
        ('Africa', 'Africa')
    ]

    is_beach = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, label="Beach")
    are_mountains = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, label="Mountains")
    temperature = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=temperature_selection, label="Average year temperature:", required=False, initial=0)
    hotel_price = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=hotel_price_selection, label="3* hotel price:", required=False, initial=0)
    continent = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=continent_choice, label="Continent:", required=False, initial=0)
    reset_filters = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': 'reset'}),
        required=False
    )