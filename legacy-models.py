# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BuisnessBuisnessninfluencer(models.Model):
    id = models.BigAutoField(primary_key=True)
    business = models.ForeignKey('BuisnessBusinesses', models.DO_NOTHING)
    influencer = models.ForeignKey('InfluensysInfluencers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buisness_buisnessninfluencer'


class BuisnessBusinesses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    crn = models.CharField(max_length=255, blank=True, null=True)
    industry = models.TextField()  # This field type is a guess.
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buisness_businesses'


class BuisnessBusinessgoals(models.Model):
    id = models.BigAutoField(primary_key=True)
    objectives = models.TextField(blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    kpi = models.CharField(max_length=255, blank=True, null=True)
    country = models.JSONField(blank=True, null=True)
    gender = models.TextField()  # This field type is a guess.
    address = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    selected_interests = models.TextField()  # This field type is a guess.
    business = models.ForeignKey(BuisnessBusinesses, models.DO_NOTHING)
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    income_level = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'buisness_businessgoals'


class BuisnessCampaigninfluencers(models.Model):
    id = models.BigAutoField(primary_key=True)
    campaign = models.ForeignKey('BuisnessCampaigns', models.DO_NOTHING)
    influencer = models.ForeignKey('InfluensysInfluencers', models.DO_NOTHING)
    business = models.ForeignKey(BuisnessBusinesses, models.DO_NOTHING)
    confirmed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'buisness_campaigninfluencers'


class BuisnessCampaigns(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    channel_section = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    creative_asset = models.CharField(max_length=255, blank=True, null=True)
    breakdown = models.CharField(max_length=255, blank=True, null=True)
    target_age = models.CharField(max_length=255, blank=True, null=True)
    target_gender = models.TextField()  # This field type is a guess.
    target_income_level = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField()  # This field type is a guess.
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    content_formats = models.CharField(max_length=255, blank=True, null=True)
    distribution_channels = models.CharField(max_length=255, blank=True, null=True)
    offer_description = models.CharField(max_length=255, blank=True, null=True)
    offer_terms = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(BuisnessBusinesses, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buisness_campaigns'


class BuisnessEventinfluencer(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey('BuisnessEvents', models.DO_NOTHING)
    influencer = models.ForeignKey('InfluensysInfluencers', models.DO_NOTHING)
    confirmed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'buisness_eventinfluencer'


class BuisnessEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_type = models.TextField()  # This field type is a guess.
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(BuisnessBusinesses, models.DO_NOTHING)
    country = models.CharField(max_length=255, blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    target_age = models.CharField(max_length=255, blank=True, null=True)
    target_gender = models.CharField(max_length=255, blank=True, null=True)
    target_income = models.CharField(max_length=255, blank=True, null=True)
    target_interests = models.TextField()  # This field type is a guess.
    target_occupation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buisness_events'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InfluensysInfluencerinstagramtokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=1000)
    influencer = models.ForeignKey('InfluensysInfluencers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'influensys_influencerinstagramtokens'


class InfluensysInfluencers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    industry = models.TextField()  # This field type is a guess.
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'influensys_influencers'


class InfluensysTargetinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    objectives = models.TextField(blank=True, null=True)
    target_age = models.TextField()  # This field type is a guess.
    country = models.JSONField(blank=True, null=True)
    target_gender = models.TextField()  # This field type is a guess.
    target_income_level = models.TextField()  # This field type is a guess.
    occupation = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    selected_interests = models.TextField()  # This field type is a guess.
    influencer = models.ForeignKey(InfluensysInfluencers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'influensys_targetinfo'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
