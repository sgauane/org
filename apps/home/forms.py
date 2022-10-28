from django import forms

from apps.home.models import Perguntas, SobreNos, Valores


class PerguntaForms(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Teu Nome",
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Teu Email",
                "class": "form-control"
            }
        )
    )
    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titulo",
                "class": "form-control"
            }
        )
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Teu Email",
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    class Meta:
        model = Perguntas
        fields = ['nome', 'email', 'titulo', 'mensagem']


class SobreNosForm(forms.ModelForm):
    missao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Missao",
                "class": "form-control"
            }
        )
    )
    visao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Visao",
                "class": "form-control"
            }
        )
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Descricao",
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    class Meta:
        model = SobreNos
        fields = ['missao','visao','descricao']


class ValoresForm(forms.ModelForm):
    designacao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Designacao",
                "class": "form-control"
            }
        )
    )

    activo = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"Activo",
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = Valores
        fields = ['designacao','activo']
