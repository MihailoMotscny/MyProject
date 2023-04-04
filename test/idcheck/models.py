from django.db import models




class Myid(models.Model):
    name_company=models.CharField('Назва компанії', max_length=25)
    culture=models.CharField('Культура',max_length=20)
    price=models.CharField('Ціна',max_length=230)
    date=models.DateTimeField('Дата публікації')
    idcheck = models.CharField('ID:', max_length=230, blank=True)

    def __str__(self,request):
        idcheck=request.user.id
        return self.name_company,idcheck
