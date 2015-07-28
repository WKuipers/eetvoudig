from django.db import models


class Wbw_list(models.Model):
    list_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, blank=True)


class Participant(models.Model):
    wbw_list = models.ForeignKey(Wbw_list, null=True)
    wbw_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)


class Bystander(models.Model):
    name = models.CharField(max_length=200)


class Meal(models.Model):
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True)

    wbw_list = models.ForeignKey(Wbw_list, null=True)
    participants = models.ManyToManyField(Participant, blank=True)
    bystanders = models.ManyToManyField(Bystander, blank=True)
    payer = models.ForeignKey(Participant, null=True, related_name='paymeal')
