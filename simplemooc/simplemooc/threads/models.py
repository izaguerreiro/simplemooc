from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


class Thread(models.Model):
    title = models.CharField('título', max_length=100)
    slug = models.SlugField('slug', max_length=100, unique=True)
    body = models.TextField('mensagem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='autor', related_name='threads'
    )
    views = models.IntegerField('visualizações', blank=True, default=0)
    answers = models.IntegerField('respostas', blank=True, default=0)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('threads:thread', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'tópico'
        verbose_name_plural = 'tópicos'
        ordering = ['-updated_at']


class Reply(models.Model):
    reply = models.TextField('resposta')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='autor', related_name='replies'
    )
    thread = models.ForeignKey(Thread, verbose_name='tópico', related_name='replies')
    correct = models.BooleanField('correta?', blank=True, default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now_add=True)

    def __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'resposta'
        verbose_name_plural = 'respostas'
        ordering = ['-correct', 'created_at']


def post_save_reply(created, instance, **kwargs):
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
    if instance.correct:
        instance.thread.replies.exclude(pk=instance.pk).update(correct=False)


def post_delete_reply(instance, **kwargs):
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()


models.signals.post_save.connect(
    post_save_reply, sender=Reply, dispatch_uid='post_save_reply'
)
models.signals.post_delete.connect(
    post_delete_reply, sender=Reply, dispatch_uid='post_delete_reply'
)