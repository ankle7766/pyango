# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=128)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo',on_delete=models.CASCADE)),
            ],
        ),
    ]
