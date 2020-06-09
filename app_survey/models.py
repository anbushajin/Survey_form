from django.db import models


class Question(models.Model):
    question = models. CharField (max_length=50)


    def __str__(self):
        return self.question

class Survey(models.Model):
    qtn = models.CharField (max_length=100)
    name = models. CharField (max_length=50)
    title = models. CharField (max_length=50)
    multiple =  models. BooleanField ()
    choice = models.TextField (max_length=1000)
    mandatory = models. BooleanField ()

    def __str__(self):
        return self.name
