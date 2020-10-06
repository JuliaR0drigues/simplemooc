from django.db import models

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)

    slug = models.SlugField('Atalho')

    description = models.TextField('Descrição', blank=True) # Blank = True quer dizer que o campo não é obrigatório

    start_date = models.DateField('Data de Início', null=True, blank=True)

    about = models.TextField('Sobre o Curso', blank=True)

    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        'Criando em', auto_now_add=True # Ser'salva a data de criação
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True #Será salvo toda vez que atualizar a informação a data da utilma atualização será salva
    )

    objects = CourseManager()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('courses:details', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-name']