from rest_framework import serializers
from test_app.models import B, A


# realize list view which return list of serialized "B" instances with fields: 'id', 'text', 'a_name', 'a_id'.
class BSerializer(serializers.ModelSerializer):
    a_name = serializers.StringRelatedField()

    class Meta:
        model = B
        depth = 1
        fields = ['id', 'text', 'a_name', 'a_id']
