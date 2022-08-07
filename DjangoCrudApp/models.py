from djongo import models
# Create your models here.

class Posts(models.Model):
    _id=models.ObjectIdField()
    post_title=models.CharField(max_length=255)
    post_description=models.TextField()
    comment=models.CharField(max_length=255)
    tags=models.CharField(max_length=255)
    user_details=models.CharField(max_length=255)
    objects=models.DjongoManager()
    
    def __str__(self):
        return self.post_title 