from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="영화 제목")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=100, verbose_name="주연")
    genre = models.CharField(max_length=50, verbose_name="장르")
    grade = models.FloatField(verbose_name="별점")
    #모델 수정 시, default 붙이기
    release = models.IntegerField(verbose_name="개봉 연도")
    running_time = models.IntegerField(verbose_name="러닝 타임")
    content = models.TextField(verbose_name="리뷰 내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)