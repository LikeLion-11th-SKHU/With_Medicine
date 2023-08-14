from django.db import models
from django.conf import settings

# Create your models here.
class Review_board(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=1, related_name="r_posts")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='review_posts', blank=True)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def r_update_counter(self):
        self.hits = self.hits + 1
        self.save()
    
class Review_Comment(models.Model):
    review_board_id = models.ForeignKey(Review_board, on_delete=models.CASCADE, related_name='comment')
    b_text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.b_text 