from django.db import models

# Common Abstract Class

class GridList(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=16)
    short = models.CharField(max_length=32,blank=True,null=True)
    source = models.URLField(max_length=64,blank=True,null=True)
    product = models.URLField(max_length=64,blank=True,null=True)
    description = models.CharField(max_length=256,blank=True,null=True)
    def __unicode__(self):
        return self.title

# Sections

class Project(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)
    performances = models.ManyToManyField('Performance')

class Performance(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)
    link = models.URLField()
    projects = models.ManyToManyField(Project,through=Project.performances.through)

class Installation(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)
    project = models.ForeignKey(Project)

class Composition(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)

class Experiment(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)

class Publication(GridList):
    gridlist_id = models.OneToOneField(GridList,parent_link=True)
    conference = models.CharField(max_length=128)
    project = models.ForeignKey(Project)

# Detail Field
class TextDetail(models.Model):
    item = models.ForeignKey(GridList)
    title = models.CharField(max_length=16)
    detail = models.CharField(max_length=1024)

# Resource helper classes

class Helper(models.Model):
    item = models.ForeignKey(GridList)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024,blank=True,null=True)
    link = models.URLField(max_length=1024)
    def __unicode__(self):
        return self.title
    class Meta:
        abstract = True

class Link(Helper):
    pass

class Image(Helper):
    def __unicode__(self):
        return self.screenshot

class Video(Helper):
    def __unicode__(self):
        return self.project.title + ":" + self.title

class Category(Helper):
    pass