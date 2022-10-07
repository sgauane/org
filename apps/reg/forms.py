from PIL import Image
from django import forms

from apps.reg.models import Imagem, TipoDocumento, Organizacao, TipoOrganizacao, Cidade, Bairro, Pessoa


class ImagemForm(forms.ModelForm):
    # ficheiro = forms.ImageField(
    #     widget=forms.FileInput(
    #     attrs={
    #         "class": "form-control"
    #     }
    # ))
    # x = forms.FloatField(widget=forms.HiddenInput())
    # y = forms.FloatField(widget=forms.HiddenInput())
    # width = forms.FloatField(widget=forms.HiddenInput())
    # height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Imagem
        fields = ('ficheiro', 'usuario_criacao')
        # fields = ('ficheiro', 'x', 'y', 'width', 'height',)


class OrganizacaoForm(forms.ModelForm):
    nome = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeolder": "Nome",
                "class": "form-control",

            }
        )
    )
    nuit = forms.CharField(
        max_length=9,
            widget=forms.TextInput(
                attrs={
                    "placeolder": "Nuit",
                    "class": "form-control",
                    "type": "number",
                    "max_lenth": "9"
                }
            )
        )
    abreviatura = forms.CharField(
                widget=forms.TextInput(
                    attrs={
                        "placeolder": "Abreviatura",
                        "class": "form-control"
                    }
                ),
                required=False
            )
    descricao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Descricao",
                "class": "form-control"
            }
        ),
                required=False
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
    data_constituicao = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data de Constituicao",
                "class": "form-control",
                "type": "date"
            }
        ),
                required=False
    )
    data_publicacao = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data da Publicacao",
                "class": "form-control",
                "type": "date"
            }
        ),
                required=False
    )
    numero_br = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero do Boletim da Republica",
                "class": "form-control"
            }
        ),
                required=False
    )

    class Meta:
        model = Organizacao
        fields = ['nuit','nome','abreviatura','descricao','tipo_organizacao', 'data_constituicao', 'data_publicacao','numero_br']


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
        ),
                required=False
    )
    numero_edificio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero",
                "class": "form-control"
            }
        ),
                required=False
    )
    quarteirao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Quarteirao",
                "class": "form-control"
            }
        ),
                required=False
    )
    andar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Andar",
                "class": "form-control"
            }
        ),
                required=False
    )
    flat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Flat",
                "class": "form-control"
            }
        ),
                required=False
    )
    numero_casa = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero de Casa",
                "class": "form-control"
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['bairro'].queryset = Bairro.objects.none()
    #     print('xxxxxxxxxxxxxxxxxxxxxxxxx',self.data)
    #
    #     if 'cidade' in self.data:
    #         print('---------------------------')
    #         try:
    #             print('xxxxxxxxxxxxxxxxxxxxxxxxx')
    #             cidade_id = int(self.data.get('cidade'))
    #             print(">>>>>>>>>>>>>>>>>>>", cidade_id)
    #             self.fields['bairro'].queryset = Bairro.objects.filter(
    #                 cidade_id=cidade_id
    #             )
    #         except (ValueError, TypeError):
    #             pass
    #     else:
    #         print(*args)


class PessoaForm(forms.ModelForm):
    model = Pessoa
    fields = ['nacionalidade']

class MembroForm(forms.Form):
    numero = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero",
                "class": "form-control",

            }
        )
    )
