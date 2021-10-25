from django.db import models
from taggit.managers import TaggableManager


class AnimeData(models.Model):
    title = models.TextField("タイトル", null=True)
    star = models.FloatField("評価", null=True)
    story = models.TextField("あらすじ", null=True)
    img_path = models.TextField("画像パス", null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name_plural = "AnimeData"
        db_table = "anime_db"

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "title": self.title,
            "star": self.star,
            "story": self.story,
            "img_path": self.img_path,
            "tags": self.tags.names(),
        }

    # get_absolute_urlは、アニメタイトルの詳細を表示するとき使うかも？
    # 21/10/18時点、活用する目処なし
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
