from django.db import models
from accounts.models import Account

# Create your models here.
class Flashcard(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_cards = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_cards(self):
        return self.card_set.all()
      

class Card(models.Model):
  desc = models.CharField(max_length=200)
  front = models.CharField(max_length=500)
  back = models.CharField(max_length=500)    
  flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    
  def __str__(self):
        return self.desc

  def get_cards(self):
        return self.card_set.all()
  
  

  