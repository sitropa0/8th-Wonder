
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'player'), (2, 'sponsor'), (3, 'drinkMeister'), (4, 'manager')], default=1)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=80)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('balance', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('instructions', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('approved', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drinkmeister',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('employeeID', models.CharField(max_length=300)),
                ('isAllowedToServeDrinks', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('yearsWorked', models.IntegerField()),
                ('mostMoneyHeld', models.IntegerField()),
                ('drinksSold', models.IntegerField()),
                ('totalTournamentsMade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('currentHole', models.IntegerField()),
                ('hole', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('companyName', models.CharField(max_length=300)),
                ('canSponsorTournament', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.TextField()),
                ('amount', models.IntegerField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOrdered', models.TimeField(auto_now=True)),
                ('specificInstructions', models.CharField(max_length=300)),
                ('served', models.BooleanField(default=False)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.drink')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(blank=True, to='main.Player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sponsor'),
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.score'),
        ),
    ]
