from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=100)
    member_count = models.IntegerField()
    ticket_count = models.IntegerField()
    tasks_to_do_count = models.IntegerField()
    tasks_high_prio_count = models.IntegerField()
    owner_id = models.IntegerField()

    def __str__(self):
        return self.title
    
class Task(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    assignee = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(User, related_name='reviewed_tasks', on_delete=models.SET_NULL, null=True)
    due_date = models.DateTimeField()
    comments_count = models.IntegerField()

    def __str__(self):
        return self.title
