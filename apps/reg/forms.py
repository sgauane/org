from PIL import Image
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from apps.reg.models import Imagem, TipoDocumento, Organizacao, TipoOrganizacao, Cidade, Bairro, Pessoa, Membro, \
    TipoContrato


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


class PessoaForm(forms.ModelForm):
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
    apelido = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Apelido",
                "class": "form-control"
            }
        ),
        required=False
    )
    genero = forms.ChoiceField(
        choices=Pessoa.generos,
        widget=forms.Select(
            attrs={
                "placeolder": "Generos",
                "class": "form-control"
            }
        )
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data de Nascimento",
                "class": "form-control",
                "type": "date"
            }
        ),

    )
    numero_documento = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeolder": "Numero do Documento",
                "class": "form-control"
            }
        ),
    )
    tipo_documento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Tipo de Documento",
                "class": "form-control"
            }
        )
    )
    nacionalidade = CountryField()

    class Meta:
        model = Pessoa
        fields = ['nuit','nome', 'apelido','nacionalidade','genero','data_nascimento', 'tipo_documento', 'numero_documento']
        widgets = {'nacionalidade': CountrySelectWidget(
            attrs={
                "placeolder": "Tipo de Organizacao",
                "class": "form-control"
            },

        )}


class MembroForm(forms.ModelForm):

    contratado = forms.ModelChoiceField(
        queryset=Pessoa.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Nome",
                "class": "form-control"
            }
        )
    )

    data_inicio_contrato = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data de Inicio",
                "class": "form-control",
                "type": "date"
            }
        ),

    )
    data_termino = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data de Termino",
                "class": "form-control",
                "type": "date"
            }
        ),

    )
    data_assinatura = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeolder": "Data da Assinatura",
                "class": "form-control",
                "type": "date"
            }
        ),

    )

    tipo_contrato = forms.ModelChoiceField(
        queryset=TipoContrato.objects.all(),
        widget=forms.Select(
            attrs={
                "placeolder": "Tipo de Contrato",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Membro
        fields = ['contratado', 'tipo_contrato','data_inicio_contrato','data_termino', 'data_assinatura']


