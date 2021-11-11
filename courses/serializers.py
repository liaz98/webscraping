from .models import Course, Category, CourseUrl
from rest_framework import serializers

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'slug',)

    # def get_fields(self):
    #     fields = super().get_fields()
    #     fields['children'] = CategorySerializer(many=True, read_only=True)
    #     return fields


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id',  'url', 'title', 'description', 'rating', 'enrolled', 'offered', 'course_type']

class CourseUrlSerializer(serializers.ModelSerializer):
    course = CourseSerializer(required=False, read_only=True)
    class Meta:
        model = CourseUrl
        fields = ['course',]

class SubCategorySerializer(serializers.ModelSerializer):
  children = CourseUrlSerializer(source='courseurl', many=True, read_only=True, required=False)

  class Meta:
        model = Category
        fields = ["id", "name", "children",]

class CategorySerializer(serializers.ModelSerializer):
    parentCategory = serializers.PrimaryKeyRelatedField()
    subCategory = serializers.SubCategorySerializer()
    # subcategories = SubCategorySerializer(source="children", many=True, required=False)

    class Meta:
        model = Category
        fields = ("parentCategory", "name",  "subcategories",)

    def get_related_field(self, model_field):
        # Handles initializing the `subcategories` field
        return CategorySerializer()
