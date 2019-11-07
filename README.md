# django_test_task

2. Write django querysets for retrieving:
	2.1) Count of "B" instances without related "a".
	2.2) "A" queryset with "b_count" field (amount of related "B" instances).
	2.3) "A" queryset where any related "b" has flag=True or without related "b". 

3. Django Rest Framework - realize list view which return list of serialized "B" instances with fields: 'id', 'text', 'a_name', 'a_id'.
**Collect data in single query.


Models for 2 and 3 tasks:

class A(models.Model):
    name = models.CharField(
        unique=True, max_length=100, null=False, blank=False,
    )


class B (models.Model):
    a = models.ForeignKey(
        A, on_delete=models.CASCADE, null=True, blank=True,
    )
    text = models.TextField()
    flag = models.BooleanField()
