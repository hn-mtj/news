import datetime

from celery.decorators import task
from django.db import transaction
from django.db.models import F

from newssite.models import Post


@task()
def post_count_view(id):
    #post = Post.objects.filter(pk=id)

    with transaction.atomic():
        post=Post.objects.select_for_update().get(pk=id)
        #post.update(count_view=F('count_view') + 1)
        post.count_view+=1
        post.publish_time=datetime.datetime.now()
        post.save()