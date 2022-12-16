from django import forms

from apps.projectos.models import Projecto, ProjectoGaleria


class ProjectoForms(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "id":"foto",
                "placeholder":"Foto",
                "class":"form-control",
            }
        ),
        required=False
    )
    designacao = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeolder": "Designacao",
                "class": "form-control",

            }
        )
    )
    descricao = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeolder": "Descricao",
                "class": "form-control",

            }
        )
    )
    class Meta:
        model = Projecto
        fields = ['imagem','designacao','descricao']


class ProjectoGaleriaForms(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder":"Foto",
                "class":"form-control",
            }
        ),
        required=False
    )
    descricao = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeolder": "Descricao",
                "class": "form-control",

            }
        )
    )
    class Meta:
        model = ProjectoGaleria
        fields = ['imagem','descricao']
