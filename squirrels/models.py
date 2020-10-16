from django.db import models
from django.utils.translation import gettext as _

class SquirrelDB(models.Model):
    X = models.FloatField(
            max_length = 20,
            help_text = _('Longitude coordinate for squirrel sighting point'),
        )
    Y = models.FloatField(
            max_length = 20,
            help_text = _('Latitude coordinate for squirrel sighting point'),
        )
    sq_id = models.CharField(
            max_length = 100,
            help_text = _('Identification tag for each squirrel sightings'),
        )
    Hect = models.CharField(
            max_length = 20,
            help_text = _('Hectare of Sighting'),
        )
    SHIFT_CHOICES = [
            ('AM', _('AM')),
            ('PM', _('PM')),
        ]
    Shift = models.CharField(
            max_length = 2,
            help_text = _('Shift of Sighting'),
            choices = SHIFT_CHOICES,
            default = 'AM',
        )
    Date = models.DateField(
            help_text = _('Date of Sighting'), 
        )
    Hect_sq_num = models.CharField(
            max_length = 20,
            help_text = _('Number within the chronological sequence of squirrel sightings'),
        )
    Age_choices = [
            ('Adult', _('Adult')),
            ('Juvenile', _('Juvenile'))
        ]
    Age = models.CharField(
            max_length = 10,
            help_text = _('Age of squirrel'),
            choices = Age_choices,
            blank = True,
        )
    Primary_color_choices = [
            ('Gray', _('Gray')),
            ('Black', _('Black')),
            ('Cinnamon', _('Cinnamon')),
        ]
    Primary_color = models.CharField(
            max_length = 10,
            choices = Primary_color_choices,
            blank = True,
            help_text = _('Primary color of squirrel'),
        )
    Highlight_color_choices = [
            ('Gray', _('Gray')),
            ('Black', _('Black')),
            ('Cinnamon', _('Cinnamon')),
        ]
    Highlight_color = models.CharField(
            max_length = 10,
            choices = Highlight_color_choices,
            blank = True,
            help_text = _('Highlight fur color'),
        )
    Combo = models.CharField(
            max_length = 30,
            blank = True,
            help_text = _('Combination of primary and highlight color'),
        )
    Color_notes = models.TextField(
            blank = True,
            help_text = _('Color notes of squirrel'),
        )
    Location_choices = [
            ('Ground Plane', _('Ground Plane')),
            ('Above Ground', _('Above Ground')),
        ]
    Location = models.CharField(
            max_length = 20,
            help_text = _('Location of squirrel'),
            choices = Location_choices,
            blank = True,
        )
    Above_measure = models.CharField(
            max_length = 10,
            blank = True,
            help_text = _('Above ground sighter measurement of squirrel'),
        )
    Specific_loc = models.TextField(
            blank = True,
            help_text = _('Specific location of squirrel'),
        )
    Running = models.BooleanField(
            help_text = _('Squirrel was seen running'),
        )
    Chasing = models.BooleanField(
            help_text = _('Squirrel was seen chasing another squirrel'),
        )
    Climbing = models.BooleanField(
            help_text = _('Squirrel was seen climbing a tree or other environmental landmark'),
        )
    Eating = models.BooleanField(
            help_text = _('Squirrel was seen eating'),
        )
    Foraging = models.BooleanField(
            help_text = _('Squirrel was seen foraging for food'),
        )
    Other_act = models.TextField(
            blank = True,
            help_text = _('Other activities squirrel was doing'),
        )
    Kuks = models.BooleanField(
            help_text = _('Squirrel was heard kukking'),
        )
    Quass = models.BooleanField(
            help_text = _('Squirrel was heard quaaing'),
        )
    Moans = models.BooleanField(
            help_text = _('Squirrel was heard moaning'),
        )
    Tail_flag = models.BooleanField(
            help_text = _('Squirrel was seen flagging its tail'),
        )
    Tail_twitch = models.BooleanField(
            help_text = _('Squirrel was seen twitching its tail'),
        )
    Approaches = models.BooleanField(
            help_text = _('Squirrel was seen approaching human, seeking food'),
        )
    Indifferent = models.BooleanField(
            help_text = _('Squirrel was indifferent to human presence'),
        )
    Runs_from = models.BooleanField(
            help_text = _('Squirrel was seen running from humans, seeing them as a threat'),
        )		
    Other_interactions = models.TextField(
            blank = True,
            help_text = _('Sighter notes on other types of interactions between squirrels and humans'),
        )
    Lat_long = models.CharField(
            max_length = 100,
            help_text = _('Latitude and longitude'),
        )
    def __str__(self):
        return self.sq_id
