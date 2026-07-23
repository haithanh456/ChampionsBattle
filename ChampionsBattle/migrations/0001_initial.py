from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bd_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Champion Team',
                'verbose_name_plural': 'Champion Teams',
            },
        ),
        migrations.CreateModel(
            name='ChampionTeamBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_models.ball')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls', to='ChampionsBattle.championteam')),
            ],
            options={
                'verbose_name': 'Team Ball',
                'verbose_name_plural': 'Team Balls',
            },
        ),
    ]
