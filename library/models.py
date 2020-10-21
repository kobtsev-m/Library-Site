from django.db import models


class PublishingHouse(models.Model):

    name = models.TextField()
    foundation_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    image = models.ImageField(
        upload_to="library/ph_covers/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Author(models.Model):

    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):

    ISBN = models.CharField(
        max_length=13
    )

    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    publishing_house = models.ForeignKey(
        PublishingHouse,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    copy_count = models.SmallIntegerField(
        default=1
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    image = models.ImageField(
        upload_to="library/books_covers/",
        null=True,
        blank=True
    )

    good_votes = models.SmallIntegerField(default=0)
    bad_votes = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):

    name = models.TextField()
    comment = models.TextField()
    date = models.DateTimeField()

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return '({}) {}: {}'.format(
            self.book.title,
            self.name,
            self.comment[:20] + '...'
            if len(self.comment) > 25
            else self.comment
        )


class ContentImage(models.Model):

    name = models.TextField()
    image = models.ImageField(
        upload_to="library/content/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name