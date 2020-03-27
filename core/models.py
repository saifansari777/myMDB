from django.db import models

# Create your models here.
class Movie(models.Model):
	NOT_RATED = 0
	RATED_G = 1
	RATED_PG = 2
	RATED_R = 3
	RATINGS = (
				(NOT_RATED, "NR - Not Rated"),
				(RATED_G, "G - General Audiences"),
				(RATED_PG, "PG - Parent Guidance Suggested"),
				(RATED_R, "R - Restricted"),
						)
	title = models.CharField(max_length = 140)
	plot  = models.TextField()
	year  = models.PositiveIntegerField()
	rating =  models.PositiveIntegerField(
								choices=RATINGS,
								default=NOT_RATED	
									)
	runtime = models.PositiveIntegerField()
	website = models.URLField(blank = True)
	poster  = models.ImageField(upload_to='media/uploads/%Y/%m/%d/', blank= True)
	director = models.ForiegnKey(
								to="Person",
								on_delete =models.SET_NULL,
								related_name="directed",
								null=True,
								blank=True	)
	writer = models.ManyToManyField(
									to="Person",
									related_name="writing_credits",
									blank=True)

	class Meta:
		ordering = ("-year", "title")

	def __str__(self):
		return "{} ({})" .format(self.title, self.year)


class Person(models.Model):
	first_name = models.CharField(max_length = 140)
	last_name = models.CharField(max_length = 140)
	date_of_birth = models.DateField()
	death =  models.DateField(null=True, blank=True)

	class Meta;
		ordering = (
			"last_name", "first_name")
	def __str__(self):
		if self.death:
			return f"{self.last_name} {self.first_name} ({self.date_of_birth}-{self.death})"
		else:
			return f"{self.last_name} {self.first_name} {self.date_of_birth}"		