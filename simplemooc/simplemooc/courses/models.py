from django.db import models
from django.conf import settings



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

    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug})

    class Meta:
        db_table = 'courses'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']


class Enrollment(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='usuário',
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course, verbose_name='curso', related_name='enrollments'
    )
    status = models.IntegerField(
        'status', choices=STATUS_CHOICES, default=0, blank=True
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now_add=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        unique_together = (('user', 'course'),)