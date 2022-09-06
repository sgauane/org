from PIL import Image
from django import forms

from apps.reg.models import Imagem, TipoDocumento, Organizacao, TipoOrganizacao, Cidade, Bairro


class ImagemForm(forms.ModelForm):
    # x = forms.FloatField(widget=forms.HiddenInput())
    # y = forms.FloatField(widget=forms.HiddenInput())
    # width = forms.FloatField(widget=forms.HiddenInput())
    # height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Imagem
        fields = ('ficheiro',)
        # fields = ('ficheiro', 'x', 'y', 'width', 'height',)

    # def save(self):
    #     photo = super(ImagemForm, self).save()
    #
    #     x = self.cleaned_data.get('x')
    #     y = self.cleaned_data.get('y')
    #     w = self.cleaned_data.get('width')
    #     h = self.cleaned_data.get('height')
    #
    #     image = Image.open(photo.file)
    #     cropped_image = image.crop((x, y, w + x, h + y))
    #     resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
    #     resized_image.save(photo.file.path)
    #
    #     return photo


class OrganizacaoForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Nome",
                "class": "form-control"
            }
        )
    )
    nuit = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeolder": "Nuit",
                    "class": "form-control"
                }
            )
        )
    abreviatura = forms.CharField(
                widget=forms.TextInput(
                    attrs={
                        "placeolder": "Abreviatura",
                        "class": "form-control"
                    }
                )
            )
    descricao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Descricao",
                "class": "form-control"
            }
        )
    )
    tipo_organizacao = forms.ModelChoiceField(
        queryset=TipoOrganizacao.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Tipo de Organizacao",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Organizacao
        fields = ['nome','nuit','abreviatura','descricao','tipo_organizacao']


class EnderecoForm(forms.Form):
    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Cidade",
                "class": "form-control"
            }
        )
    )
    bairro = forms.ModelChoiceField(
        queryset=Bairro.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Bairro",
                "class": "form-control"
            }
        )
    )
    rua_avenida = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Rua/Avenida",
                "class": "form-control"
            }
        )
    )
    nome_edificio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Edificio",
                "class": "form-control"
            }
        )
    )
    numero_edificio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero",
                "class": "form-control"
            }
        )
    )
    andar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Andar",
                "class": "form-control"
            }
        )
    )
    flat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Flat",
                "class": "form-control"
            }
        )
    )
    numero_casa = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero de Casa",
                "class": "form-control"
            }
        )
    )