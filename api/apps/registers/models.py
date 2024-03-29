from django.contrib.auth.models import User
from django.db import models


class CollectedCoin(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify collected coin',
    )
    value = models.FloatField(
        null=False,
        blank=False,
        help_text='coin value',
        default=10
    )
    user = models.ForeignKey(
        User,
        related_name='coins',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'collected_coin'


class Monster(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify monster',
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text='name monster'
    )

    class Meta:
        db_table = 'monsters'

    def __str__(self):
        return self.name


class KilledMonster(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify killed monster',
    )
    user = models.ForeignKey(
        User,
        related_name='dead_monsters',
        on_delete=models.CASCADE
    )
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Killed_monster'


class Death(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        blank=False,
        help_text='identify death',
    )
    user = models.ForeignKey(
        User,
        related_name='deaths',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        null=True,
        auto_now_add=True,
        help_text='register datetime death',
    )

    class Meta:
        db_table = 'deaths'
