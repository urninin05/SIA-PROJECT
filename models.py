from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    task_title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title