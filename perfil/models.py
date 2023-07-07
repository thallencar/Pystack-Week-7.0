from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento= models.FloatField(default=0)

    def __str__(self) -> str:
        return self.categoria

class Conta(models.Model):
    banco_choices = (
        ('BB', 'Banco do Brasil'),
        ('CE', 'Caixa Econômica Federal'),
        ('IT', 'Itaú Unibanco'),
        ('BR', 'Bradesco'),
        ('SB', 'Santander Brasil'),
        ('SF', 'Banco Safra'),
        ('BV', 'Banco Votorantim'),
        ('CI', 'Banco Citibank'),
        ('BTG', 'Banco BTG Pactual'),
        ('OR', 'Banco Original'),
        ('PA', 'Banco Pan'),
        ('IN', 'Banco Inter'),
        ('C6', 'Banco C6'),
        ('BNB', 'Banco do Nordeste do Brasil'),
        ('BCOOP', 'Bancoob'),
        ('SICREDI', 'Sicredi'),
        ('BI', 'Banco Industrial do Brasil'),
        ('PINE', 'Banco Pine'),
        ('BANRISUL', 'Banrisul'),
        ('REN', 'Banco Rendimento')
        
        )
    
    tipo_choices=(
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    )


    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=8, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")

    def __str__(self):
        return self.apelido
    


