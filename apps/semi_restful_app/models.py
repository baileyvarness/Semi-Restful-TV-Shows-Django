from django.db import models

class ShowsManager(models.Manager):
    def validator(self, post_data):
        print('post_data: ', post_data)
        errors = {}
        if len(post_data['title']) < 2:
            print('title is too short')
            errors['title'] = "title is too short"
        if len(post_data['network']) < 3:
            print('network is too short')
            errors['network'] = "network is too short"
        if len(post_data['description']) < 10:
            print('description is too short')
            errors['description'] = "description is too short"
        
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()