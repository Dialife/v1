from django.db import models


class Recipe(models.Model):
    def __str__(self):
        return self.food.id+ ' - ' + self.food_title
    food_id = models.CharField(max_length=250)

    food_title = models.CharField(max_length=250)

    name_title = models.CharField(max_length=250)

    calories_title = models.CharField(max_length=250)

    fat_title = models.CharField(max_length=250)

    protein_title = models.CharField(max_length=250)

    carbs_title = models.CharField(max_length=250)

    fiber_title = models.CharField(max_length=250)

    type_title = models.CharField(max_length=250)

    calcium_title = models.CharField(max_length=250)

    cholestrol_title = models.CharField(max_length=250)

    iron_title = models.CharField(max_length=250)

    magnesium_title = models.CharField(max_length=250)

    sodium_title = models.CharField(max_length=250)

    phosphorous_title = models.CharField(max_length=250)

    potassium_title = models.CharField(max_length=250)

    zinc_title = models.CharField(max_length=250)

    niacin_title = models.CharField(max_length=250)

    vitamina_title = models.CharField(max_length=250)

    vitaminb6_title = models.CharField(max_length=250)

    vitaminc_title = models.CharField(max_length=250)

class Exercise(models.Model):
    exercise_calorie_title = models.CharField(max_length=250)
    exercise_calorie_burn = models.CharField(max_length=250)
    def __str__(self):
        return self.exercise_calorie_title

