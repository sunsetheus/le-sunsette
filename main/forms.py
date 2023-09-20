from django.forms import ModelForm, TextInput, NumberInput, Textarea
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price"]
        # reference: https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
        widgets = {
            "name": TextInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
            }),
            "amount": NumberInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'min': 1 # reference: https://stackoverflow.com/questions/37024650/specify-max-and-min-in-numberinput-widget
            }),
            "description": Textarea(attrs={
                'class': 'min-w-[370px] max-h-[150px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
            }),
            "price": NumberInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'min': 0.01
            })
        }