from rest_framework import serializers
from test_app.models import B


# realize list view which return list of serialized "B" instances with fields: 'id', 'text', 'a_name', 'a_id'.
class BSerializer(serializers.ModelSerializer):
    class Meta:
        model = B
        depth = 1
        fields = ['id', 'text', 'a']

    def to_representation(self, obj):
        """ This is to flatten the structure and rename the fields according to the task """
        representation = super().to_representation(obj)
        a_representation = representation.pop('a')
        representation['a_name'] = a_representation['name'] if a_representation else ''
        representation['a_id'] = a_representation['id'] if a_representation else ''
        return representation
