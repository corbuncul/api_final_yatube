from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель групп."""
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; '
                  'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель постов."""
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        'Фото', upload_to='posts/', blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return (
            f'{self.text.split()[0]} автор: {self.author.get_username()}.'
        )


class Comment(models.Model):
    """Модель комментариев к постам."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return (
            f'{self.text.split()[0]} автор: {self.author.get_username()} '
            f'к посту: {self.post}'
        )


class Follow(models.Model):
    """Модель подписок пользователей."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Респондент',
        related_name='following')

    class Meta:
        unique_together = ('user', 'following')
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

    def clean(self):
        if self.user == self.following:
            raise ValidationError('Подписка на самого себя запрещена!')

    def __str__(self):
        return f'{self.user.get_username()} -> {self.following.get_username()}'
