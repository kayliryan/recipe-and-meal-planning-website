from django import forms
from recipes.models import Rating, FoodItem


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]

class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        exclude = ()