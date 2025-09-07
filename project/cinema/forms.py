from django import forms

from .models import Comment, Movie


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label="Izoh", widget=forms.TextInput(
        attrs= {
            'style': 'width: 100%; border-radius: 20px; padding: 10px; margin: 10px;',
            'placeholder': "Izoh kiriting"

        }
    ))


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'photo', 'video', 'release_date', 'genre']

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "style": "width: 100%; padding: 10px; border-radius: 12px;",
                    "placeholder": "Movie Name"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "style": "width: 100%; padding: 10px; border-radius: 12px;",
                    "placeholder": "Movie Description",
                    "rows": 5
                }
            ),
            "release_date": forms.NumberInput(
                attrs={
                    "style": "width: 100%; padding: 10px; border-radius: 12px;",
                    "placeholder": "Release Year"
                }
            ),
            "genre": forms.Select(
                attrs={
                    "style": "width: 100%; padding: 10px; border-radius: 12px;"
                }
            ),
            "photo": forms.ClearableFileInput(
                attrs={
                    "style": "width: 100%; margin-top: 10px;"
                }
            ),
            "video": forms.ClearableFileInput(
                attrs={
                    "style": "width: 100%; margin-top: 10px;"
                }
            ),
        }
