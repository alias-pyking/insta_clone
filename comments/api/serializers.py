from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField,
                                        HyperlinkedIdentityField,
                                        )
        
from comments.models import Comment,Reply

class CommentsSerializer(ModelSerializer):
    # comment_replies = HyperlinkedIdentityField(
    #     view_name='comments-api:api_comment_replies',
    #     lookup_field='pk',
    # )
    class Meta:
        model = Comment
        fields = [
            'post',
            'user',
            'text',
            'timestamp',
            # 'comment_replies',
        ]

class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'text',
            'timestamp',
        ]

class CommentsReplySerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Reply
        fields = [
            'user',
            'text',
            'timestamp',
            # 'comment_replies',
        ]
    def get_user(self, obj):
        return str(obj.user)