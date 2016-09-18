from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('atalho')
    description = models.TextField('descrição simples', blank=True)
    about = models.TextField('sobre o curso', blank=True)
    start_date = models.DateField('data de início', null=True, blank=True)
    image = models.ImageField(
        'imagem', upload_to='courses/images', null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now_add=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'courses'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']
