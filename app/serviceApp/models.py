from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    location = models.CharField(max_length=30, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class LogEntry(models.Model):
    # The model for Log Entry
    isVerified = False
    #logAuthor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    benefitingService = models.CharField(max_length=200)
    logDescription = models.CharField(max_length=200)
    serviceDate = models.DateTimeField()
    serviceTime = models
    logEntryDate = models.DateTimeField(
        default=timezone.now()
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def acceptLogAccepted(self):
        self.isVerified = True

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.logAuthor + self.published_date

class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class GithubProfile(models.Model):
    user = models.ForeignKey(User)
    github_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    scopes = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class TumblrProfile(models.Model):
    user = models.ForeignKey(User)
    tumblr_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class InstagramProfile(models.Model):
    user = models.ForeignKey(User)
    instagram_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class TwitterProfile(models.Model):
    user = models.ForeignKey(User)
    twitter_user = models.CharField(max_length=200)
    oauth_token = models.CharField(max_length=200)
    oauth_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class LinkedinProfile(models.Model):
    user = models.ForeignKey(User)
    linkedin_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class MeetupToken(models.Model):
    # user = models.ForeignKey(User)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.access_token)

class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    fb_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)

class GoogleProfile(models.Model):
    user = models.ForeignKey(User)
    google_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)

class DropboxProfile(models.Model):
    user = models.ForeignKey(User)
    dropbox_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)


class FoursquareProfile(models.Model):
    user = models.ForeignKey(User)
    foursquare_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
