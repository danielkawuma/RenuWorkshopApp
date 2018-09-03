from django.db import models

# Create your models here.

MAX_CHAR_LENGTH = 100


class Track(models.Model):

    name = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Name",
                            null=False)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Name",
                            null=False)

    # url = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="URL",
    #                        null=True)
    # workshop_sponsored = models.ForeignKey(Workshop,
    #                                        on_delete=models.CASCADE,
    #                                        db_column="Workshop_Sponsored")

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    first_name = models.CharField(max_length=MAX_CHAR_LENGTH,
                                  db_column="First_Name", null=False)
    last_name = models.CharField(max_length=MAX_CHAR_LENGTH,
                                 db_column="Last_Name", null=False)
    email = models.EmailField(db_column="Email_Address", null=False)
    institution = models.CharField(max_length=MAX_CHAR_LENGTH,
                                   db_column="Institution", null=True)
    gender = models.CharField(max_length=1, db_column="Gender",
                              choices=GENDER_CHOICES, null=True,
                              default='X')
    country = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Country",
                           null=True, default='UNSPECIFIED')

    def __str__(self):
        fname = str(self.first_name)
        lname = str(self.last_name)
        email = str(self.email)
        return fname + " " + lname + " <" + email + ">"


class Participant(Person):
    # workshop_attended = models.ForeignKey(Workshop,
    #                                       on_delete=models.CASCADE,
    #                                       db_column="Workshop_Attended")
    pass


class Facilitator(Person):

    # workshop_taught = models.ForeignKey(Workshop,
    #                                     on_delete=models.CASCADE,
    #                                     db_column="Workshop_Taught")
    pass


class Workshop(models.Model):

    name = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Name",
                            null=False)
    start_date = models.DateField(db_column="Start_Date", null=False)
    end_date = models.DateField(db_column="End_Date", null=False)
    venue = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Venue",
                             null=False)
    host = models.CharField(max_length=MAX_CHAR_LENGTH, db_column="Host",
                            null=True)

    track = models.ForeignKey(Track, on_delete=models.CASCADE,
                              db_column="Track")

    # To implement mapping tables
    facilitators = models.ManyToManyField(Facilitator,
                                          related_name="facilitated",
                                          db_table="workshop_facilitator_map")
    participants = models.ManyToManyField(Participant,
                                          related_name="attended",
                                          db_table="workshop_participant_map")
    sponsors = models.ManyToManyField(Sponsor, related_name="sponsored",
                                      db_table="workshop_sponsor_map")

    def __str__(self):
        return self.name
