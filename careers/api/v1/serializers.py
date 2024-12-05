from rest_framework import serializers

from careers.models import Careers


class CreateCareersSerializer(serializers.Serializer):
    username  = serializers.CharField()
    title  = serializers.CharField()
    content  = serializers.CharField()    

    class Meta:
        model = Careers
        fields = [
            "username","title",
            "content",
        ]

    def create(self, validated_data):
        user = Careers.objects.create(**validated_data)
        return user

class ListCareersSerializer(serializers.Serializer):
    id  = serializers.CharField()
    username  = serializers.CharField()
    title  = serializers.CharField()
    content  = serializers.CharField()  
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = Careers
        fields = [
            "id", "username","title",
            "content", "created_datetime"
        ]


class PatchCareersSerializer(serializers.Serializer):
    title  = serializers.CharField()
    content  = serializers.CharField()  

    class Meta:
        model = Careers
        fields = ["title", "content"]

    def update(self, instance, validated_data):
        import ipdb
        ipdb.set_trace()
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)        
        instance.save()
        return instance

class DeleteProductsSerializer(serializers.Serializer):
        
    id = serializers.CharField()        

    class Meta:
        model = Careers
        fields = [
            "id"
        ]
