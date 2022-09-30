from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
#from pkg_resources import _


# Create your models here.
class ModeloBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    activo = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)
    data_actualizacao = models.DateField(auto_created=True, null=True, blank=True)


    class Meta:
        abstract = True


class Cidade(ModeloBase):
    pais = CountryField()
    designacao= models.CharField(max_length=255, null=False, default="")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.designacao


class Bairro(ModeloBase):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    designacao= models.CharField(max_length=255, null=False, default="")

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __str__(self):
        return self.designacao


class Localizacao(ModeloBase):
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    rua_avenida = models.CharField(max_length=255)
    quarteirao = models.CharField(max_length=10, null=True, blank=True)
    nome_edificio = models.CharField(max_length=255, null=True, blank=True)
    numero_edificio = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Localizacao"
        verbose_name_plural = "Localizacoes"

    def __str__(self):
        return self.rua_avenida


class TipoEntidade(ModeloBase):
    designacao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Tipo de Entidade"
        verbose_name_plural = "Tipos de Entidades"

    def __str__(self):
        return self.designacao


class TipoOrganizacao(ModeloBase):
    designacao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Tipo de Organizacao"
        verbose_name_plural = "Tipos de Organizacoes"

    def __str__(self):
        return self.designacao


class TipoDocumento(ModeloBase):
    designacao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"

    def __str__(self):
        return self.designacao


def user_directory_path(instance, ficheiro):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'imagens/user_{0}/{1}'.format(instance.user.id, ficheiro)


class Imagem(ModeloBase):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    ficheiro = models.ImageField(upload_to='imagens')

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return self.ficheiro.url


class Entidade(ModeloBase):
    nuit =models.CharField(max_length=9, null= True, blank=True)
    nome = models.CharField(max_length=500)
    foto = models.OneToOneField(Imagem, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome


class Pessoa(Entidade):
    apelido = models.CharField(max_length=255, null=True, blank=True)
    nacionalidade = CountryField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    data_nascimento = models.DateField()
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return "%s %s" % (self.nome, self.apelido)


class Organizacao(Entidade):
    abreviatura = models.CharField(max_length=255, blank=True)
    descricao = models.CharField(max_length=255, blank=True)
    data_constituicao = models.DateTimeField(auto_created=True, blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_created=True, blank=True, null=True)
    numero_br = models.CharField(max_length=255, blank=True)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_organizacao = models.ForeignKey(TipoOrganizacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'organizacao'
        verbose_name_plural = 'organizacacoes'


class Endereco(ModeloBase):
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    numero_casa = models.CharField(max_length=10, blank=True)
    andar = models.CharField(max_length=10, blank=True)
    flat = models.CharField(max_length=10, blank=True)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    def __str__(self):
        return self.numero_casa


