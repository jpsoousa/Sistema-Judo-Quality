# Generated by Django 2.2.4 on 2019-10-22 22:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tournament_name', max_length=255)),
                ('initial_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TournamentProfiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.TournamentProfiles')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='register_participants_tournament',
                                                 related_query_name='register_participantss_tournament',
                                                 to='register.Tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                           related_name='register_participantss_participant',
                                           related_query_name='register_participantss_participant',
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('register.participants',),
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('register.participants',),
        ),
        migrations.CreateModel(
            name='Knockout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_initial_match', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('first_match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='knockout_first_match',
                                                  related_query_name='first_matchs', to='register.Knockout')),
                ('second_match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='knockout_second_match',
                                                   related_query_name='second_matchs', to='register.Knockout')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='register_knockout_tournament',
                                                 related_query_name='register_knockouts_tournament',
                                                 to='register.Tournament')),
                ('competitor_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                     related_name='register_knockout_competitor_one',
                                                     related_query_name='register_knockouts_competitor_one',
                                                     to='register.Competitor')),
                ('competitor_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                     related_name='register_knockout_competitor_two',
                                                     related_query_name='register_knockouts_competitor_two',
                                                     to='register.Competitor')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='register_knockouts_referee',
                                              related_query_name='register_knockouts_referee', to='register.Referee')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='register_knockouts_winner',
                                             related_query_name='register_knockouts_winner', to='register.Competitor')),
            ],
        ),
    ]