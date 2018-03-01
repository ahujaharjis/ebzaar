from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class NoServiceArea(models.Model):
    name = models.CharField(max_length=60)
    email_id = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=32)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'no_service_area'
        unique_together = (('email_id', 'latitude', 'longitude'), ('phone_no', 'latitude', 'longitude'),)


class OcAbandonedCart(models.Model):
    abandoned_cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    merchant_id = models.IntegerField()
    product_ids = models.TextField()
    total_amount = models.IntegerField()
    added_on = models.DateTimeField()
    modifieded_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_abandoned_cart'


class OcAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    company_id = models.CharField(max_length=32)
    tax_id = models.CharField(max_length=32)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_address'


class OcAffiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=32)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate'


class OcAffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_transaction'


class OcArea(models.Model):
    area_id = models.AutoField(primary_key=True)
    suburb_id = models.IntegerField()
    area_name = models.CharField(max_length=200)
    pincode = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_area'


class OcAttribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute'


class OcAttributeDescription(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class OcAttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute_group'


class OcAttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class OcBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner'


class OcBannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_banner_image'


class OcBannerImageDescription(models.Model):
    banner_image_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    banner_id = models.IntegerField()
    title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_banner_image_description'
        unique_together = (('banner_image_id', 'language_id'),)


class OcBehaviorRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    store_view = models.CharField(max_length=255)
    customer_group_ids = models.CharField(max_length=255)
    actions = models.IntegerField()
    reward_point = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_behavior_rules'


class OcBestSeller(models.Model):
    best_seller_id = models.AutoField(primary_key=True)
    merchant_id = models.IntegerField()
    product_id = models.IntegerField()
    status = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_best_seller'


class OcBrandStore(models.Model):
    store = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'oc_brand_store'


class OcBrandStoreDeliveryPincode(models.Model):
    store = models.ForeignKey(OcBrandStore, models.DO_NOTHING)
    pincode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'oc_brand_store_delivery_pincode'
        unique_together = (('store', 'pincode'),)


class OcBrandStoreLogistics(models.Model):
    store = models.ForeignKey(OcBrandStore, models.DO_NOTHING)
    logistics = models.ForeignKey('OcLogistics', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_brand_store_logistics'
        unique_together = (('store', 'logistics'),)


class OcBrandStorePickupAddress(models.Model):
    store = models.ForeignKey(OcBrandStore, models.DO_NOTHING)
    address = models.ForeignKey(OcAddress, models.DO_NOTHING)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_brand_store_pickup_address'
        unique_together = (('store', 'address'), ('store', 'sort_order'),)


class OcBusinessAddress(models.Model):
    store = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING)
    address = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_business_address'


class OcCalendarAcceptedDaysOfEachMonth(models.Model):
    blocked = models.ForeignKey('OcCalendarBlockedDaysOfEachMonth', models.DO_NOTHING)
    merchant = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_calendar_accepted_days_of_each_month'
        unique_together = (('blocked', 'merchant'),)


class OcCalendarAcceptedHalfDaysOfWeek(models.Model):
    blocked = models.ForeignKey('OcCalendarHalfDaysOfWeek', models.DO_NOTHING)
    merchant = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_calendar_accepted_half_days_of_week'
        unique_together = (('blocked', 'merchant'),)


class OcCalendarBlockedDaysOfEachMonth(models.Model):
    day = models.PositiveIntegerField()
    city = models.ForeignKey('OcCity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_calendar_blocked_days_of_each_month'
        unique_together = (('day', 'city'),)


class OcCalendarBlockedDaysOfMonth(models.Model):
    city = models.ForeignKey('OcCity', models.DO_NOTHING)
    merchant = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_calendar_blocked_days_of_month'
        unique_together = (('city', 'merchant', 'start', 'end'),)


class OcCalendarBlockedDaysOfWeek(models.Model):
    week = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    city = models.ForeignKey('OcCity', models.DO_NOTHING)
    merchant = models.ForeignKey('OcCustomerpartnerToCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_calendar_blocked_days_of_week'
        unique_together = (('week', 'day', 'city', 'merchant'),)


class OcCalendarBlockedDaysOfYear(models.Model):
    start = models.DateField()
    end = models.DateField()
    city = models.ForeignKey('OcCity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_calendar_blocked_days_of_year'
        unique_together = (('start', 'end', 'city'),)


class OcCalendarHalfDaysOfWeek(models.Model):
    week = models.PositiveIntegerField()
    city = models.ForeignKey('OcCity', models.DO_NOTHING)
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'oc_calendar_half_days_of_week'
        unique_together = (('week', 'city', 'start', 'end'),)


class OcCatalogRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    conditions_serialized = models.TextField()
    store_view = models.CharField(max_length=255)
    customer_group_ids = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    actions = models.IntegerField()
    reward_per_spent = models.IntegerField()
    reward_point = models.IntegerField()
    rule_position = models.IntegerField()
    stop_rules_processing = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_catalog_rules'


class OcCategoriesMasterCategory(models.Model):
    category = models.ForeignKey('OcCategory', models.DO_NOTHING)
    master_category = models.ForeignKey('OcMasterCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_categories_master_category'
        unique_together = (('master_category', 'category'),)


class OcCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_category'
    def __str__(self):
        return str(self.category_id)

class OcCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_category_description'
        unique_together = (('category_id', 'language_id'),)

    def __str__(self):
        return self.name

class OcCategoryFilter(models.Model):
    category_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter'
        unique_together = (('category_id', 'filter_id'),)


class OcCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcCategoryToLayout(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class OcCategoryToStore(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store'
        unique_together = (('category_id', 'store_id'),)


class OcCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    zone_id = models.IntegerField()
    name = models.CharField(max_length=128)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_city'


class OcCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_country'


class OcCoupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    first_time = models.IntegerField()
    map = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_coupon'


class OcCouponCategory(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class OcCouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_history'


class OcCouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_product'


class OcCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_currency'


class OcCustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    required = models.IntegerField()
    location = models.CharField(max_length=32)
    position = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field'


class OcCustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class OcCustomFieldToCustomerGroup(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_to_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class OcCustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value'


class OcCustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


class OcCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    token = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    facebook_id = models.CharField(max_length=255)
    twitter_id = models.CharField(max_length=255)
    google_id = models.CharField(max_length=255)
    linkedin_id = models.CharField(max_length=255)
    vkontakte_id = models.CharField(max_length=255)
    odnoklassniki_id = models.CharField(max_length=255)
    live_id = models.CharField(max_length=255)
    yandex_id = models.CharField(max_length=255)
    mailru_id = models.CharField(max_length=255)
    instagram_id = models.CharField(max_length=255)
    paypal_id = models.CharField(max_length=255)
    vimeo_id = models.CharField(max_length=255)
    tumblr_id = models.CharField(max_length=255)
    yahoo_id = models.CharField(max_length=255)
    foursquare_id = models.CharField(max_length=255)
    selected_store = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer'


class OcCustomerAltNoOtp(models.Model):
    customer_id = models.IntegerField(unique=True)
    org_otp = models.CharField(max_length=4, blank=True, null=True)
    org_otp_expiry = models.DateTimeField()
    alt_mobile = models.CharField(unique=True, max_length=10, blank=True, null=True)
    alt_otp = models.CharField(max_length=4, blank=True, null=True)
    alt_otp_expiry = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_alt_no_otp'


class OcCustomerAuthentication(models.Model):
    customer_authentication_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    provider = models.CharField(max_length=55)
    identifier = models.CharField(max_length=200)
    web_site_url = models.CharField(max_length=255)
    profile_url = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    birth_day = models.CharField(max_length=255)
    birth_month = models.CharField(max_length=255)
    birth_year = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_authentication'
        unique_together = (('identifier', 'provider'),)


class OcCustomerBanIp(models.Model):
    customer_ban_ip_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'oc_customer_ban_ip'


class OcCustomerField(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.IntegerField()
    value = models.TextField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_field'
        unique_together = (('customer_id', 'custom_field_id', 'custom_field_value_id'),)


class OcCustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    company_id_display = models.IntegerField()
    company_id_required = models.IntegerField()
    tax_id_display = models.IntegerField()
    tax_id_required = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group'


class OcCustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class OcCustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_history'


class OcCustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_ip'


class OcCustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_online'


class OcCustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    transaction_type = models.IntegerField()
    product_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward'


class OcCustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_transaction'


class OcCustomerpartnerCommissionCategory(models.Model):
    category_id = models.IntegerField()
    fixed = models.FloatField()
    percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_commission_category'


class OcCustomerpartnerCommissionManual(models.Model):
    name = models.CharField(max_length=100)
    fixed = models.FloatField()
    percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_commission_manual'


class OcCustomerpartnerDownload(models.Model):
    download_id = models.AutoField(primary_key=True)
    seller_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_download'


class OcCustomerpartnerFlatshipping(models.Model):
    partner_id = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    tax_class_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_flatshipping'


class OcCustomerpartnerProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=13)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    viewed = models.IntegerField()
    oc_product_id = models.IntegerField()
    keyword = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product'


class OcCustomerpartnerProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


class OcCustomerpartnerProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    tag = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_description'
        unique_together = (('product_id', 'language_id'),)


class OcCustomerpartnerProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_discount'


class OcCustomerpartnerProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_filter'
        unique_together = (('product_id', 'filter_id'),)


class OcCustomerpartnerProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_image'


class OcCustomerpartnerProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_option'


class OcCustomerpartnerProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_option_value'


class OcCustomerpartnerProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_related'
        unique_together = (('product_id', 'related_id'),)


class OcCustomerpartnerProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_reward'


class OcCustomerpartnerProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_special'


class OcCustomerpartnerProductToCategory(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_to_category'
        unique_together = (('product_id', 'category_id'),)


class OcCustomerpartnerProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_product_to_download'
        unique_together = (('product_id', 'download_id'),)


class OcCustomerpartnerShipping(models.Model):
    seller_id = models.IntegerField()
    country_code = models.CharField(max_length=100)
    zip_to = models.CharField(max_length=100)
    zip_from = models.CharField(max_length=100)
    price = models.FloatField()
    weight_from = models.FloatField()
    weight_to = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_shipping'


class OcCustomerpartnerSoldTracking(models.Model):
    product_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    date_added = models.DateField()
    tracking = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_sold_tracking'


class OcCustomerpartnerToCommission(models.Model):
    customer_id = models.IntegerField()
    commission_id = models.IntegerField()
    fixed = models.FloatField()
    percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_commission'


class OcCustomerpartnerToCustomer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    is_partner = models.IntegerField()
    screenname = models.CharField(max_length=255)
    shipping_boundry = models.IntegerField()
    gender = models.CharField(max_length=255)
    shortprofile = models.TextField()
    avatar = models.CharField(max_length=255)
    twitterid = models.CharField(max_length=255)
    paypalid = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city_id = models.IntegerField()
    zone_id = models.IntegerField()
    country_id = models.IntegerField()
    facebookid = models.CharField(max_length=255)
    backgroundcolor = models.CharField(max_length=255)
    companybanner = models.CharField(max_length=255)
    companylogo = models.CharField(max_length=255)
    companylocality = models.CharField(max_length=255)
    companyname = models.CharField(max_length=255)
    companydescription = models.TextField()
    countrylogo = models.CharField(max_length=1000)
    otherpayment = models.TextField()
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    seo_city = models.TextField(blank=True, null=True)
    seo_keyword = models.TextField()
    meal_voucher = models.IntegerField()
    meal_voucher_sudexo = models.IntegerField()
    meal_voucher_ticket = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_customer'


class OcCustomerpartnerToFeedback(models.Model):
    customer_id = models.SmallIntegerField()
    seller_id = models.SmallIntegerField()
    feedprice = models.SmallIntegerField()
    feedvalue = models.SmallIntegerField()
    feedquality = models.SmallIntegerField()
    nickname = models.CharField(max_length=255)
    summary = models.TextField()
    review = models.TextField()
    createdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_feedback'


class OcCustomerpartnerToOrder(models.Model):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.FloatField()
    quantity = models.FloatField()
    shipping = models.CharField(max_length=255)
    shipping_rate = models.FloatField()
    payment = models.CharField(max_length=255)
    payment_rate = models.FloatField()
    admin = models.FloatField()
    customer = models.FloatField()
    details = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_order'


class OcCustomerpartnerToPayment(models.Model):
    customer_id = models.IntegerField()
    amount = models.FloatField()
    text = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    request_type = models.CharField(max_length=255)
    paid = models.IntegerField()
    balance_reduced = models.IntegerField()
    payment = models.CharField(max_length=255)
    date_added = models.DateField()
    date_modified = models.DateField()
    added_by = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_payment'


class OcCustomerpartnerToProduct(models.Model):
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_product'


class OcCustomerpartnerToStorelocator(models.Model):
    customerpartner_to_storelocator_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    storelocator_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_storelocator'


class OcCustomerpartnerToTransaction(models.Model):
    customer_id = models.IntegerField()
    amount = models.FloatField()
    text = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    date_added = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_to_transaction'


class OcCustomerpartnerUploadInfo(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customerpartner_upload_info'


class OcDelivery(models.Model):
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    subarea = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_delivery'


class OcDeliveryZone(models.Model):
    delivery_zone_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    city_id = models.IntegerField()
    postcode = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_delivery_zone'


class OcDeliveryZoneDescription(models.Model):
    delivery_zone_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_delivery_zone_description'


class OcDeliveryZoneTimes(models.Model):
    delivery_zone_id = models.IntegerField()
    timeslot_duration_id = models.IntegerField()
    bandwidth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_delivery_zone_times'


class OcDeliverydateswizard(models.Model):
    ddw_id = models.AutoField(primary_key=True)
    shipping_method_code = models.CharField(max_length=12)
    required = models.PositiveIntegerField()
    enabled = models.PositiveIntegerField()
    weekdays = models.CharField(max_length=20)
    min_days = models.PositiveIntegerField()
    max_days = models.PositiveSmallIntegerField()
    cut_off_time_enabled = models.IntegerField()
    cut_off_time_hours = models.PositiveIntegerField()
    cut_off_time_minutes = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_deliverydateswizard'


class OcDeliverydateswizardDates(models.Model):
    ddwd_id = models.AutoField(primary_key=True)
    ddw_id = models.PositiveIntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    type = models.CharField(max_length=12)
    recurring = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_deliverydateswizard_dates'


class OcDeliverydateswizardTimes(models.Model):
    ddw_id = models.PositiveIntegerField()
    language_id = models.PositiveIntegerField()
    text = models.CharField(max_length=64)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_deliverydateswizard_times'


class OcDownload(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=128)
    mask = models.CharField(max_length=128)
    remaining = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_download'


class OcDownloadDescription(models.Model):
    download_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_download_description'
        unique_together = (('download_id', 'language_id'),)


class OcEmailTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_email_template'


class OcErrorlogManager(models.Model):
    filename = models.CharField(max_length=255)
    row_hash = models.CharField(max_length=32)
    message_hash = models.CharField(max_length=32)
    message = models.TextField()
    timestamp = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_errorlog_manager'


class OcExCouponCategory(models.Model):
    coupon_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_ex_coupon_category'


class OcExCouponProduct(models.Model):
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_ex_coupon_product'


class OcExtension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_extension'


class OcFavorateStore(models.Model):
    customer = models.ForeignKey(OcCustomer, models.DO_NOTHING)
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING)
    frequency = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_favorate_store'
        unique_together = (('customer', 'sort_order'), ('customer', 'store'),)


class OcFilter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter'


class OcFilterDescription(models.Model):
    filter_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_description'
        unique_together = (('filter_id', 'language_id'),)


class OcFilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter_group'


class OcFilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class OcGeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_geo_zone'


class OcHomeSlider(models.Model):
    image_id = models.AutoField(primary_key=True)
    url = models.TextField()
    added_on = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_home_slider'


class OcInformation(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information'


class OcInformationDescription(models.Model):
    information_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_description = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_information_description'
        unique_together = (('information_id', 'language_id'),)


class OcInformationToLayout(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class OcInformationToStore(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_store'
        unique_together = (('information_id', 'store_id'),)


class OcLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    filename = models.CharField(max_length=64)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_language'


class OcLayout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout'


class OcLayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_layout_route'


class OcLengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_length_class'


class OcLengthClassDescription(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class OcLogistics(models.Model):
    name = models.CharField(unique=True, max_length=50)
    api_key = models.CharField(unique=True, max_length=50)
    web_service_link = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_logistics'


class OcLogisticsPickupPincode(models.Model):
    logistics = models.ForeignKey(OcLogistics, models.DO_NOTHING)
    pincode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'oc_logistics_pickup_pincode'
        unique_together = (('logistics', 'pincode'),)


class OcLogisticsShipment(models.Model):
    order = models.ForeignKey('OcOrder', models.DO_NOTHING, unique=True)
    logistics = models.ForeignKey(OcLogistics, models.DO_NOTHING)
    awb_no = models.CharField(unique=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'oc_logistics_shipment'


class OcManufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer'


class OcManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class OcMapStoresToCategories(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING)
    master = models.ForeignKey(OcCategory, models.DO_NOTHING,related_name="father")
    primary = models.ForeignKey(OcCategory, models.DO_NOTHING,related_name="head")

    class Meta:
        managed = False
        db_table = 'oc_map_stores_to_categories'
        unique_together = (('store', 'master', 'primary'),)


class OcMasterCategory(models.Model):
    image = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=30)
    sort_order = models.SmallIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'oc_master_category'


class OcMerchantBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.TextField()
    status = models.IntegerField()
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_merchant_banner'


class OcMfilterTags(models.Model):
    mfilter_tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_mfilter_tags'


class OcMfilterValues(models.Model):
    mfilter_value_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=9)
    value = models.CharField(max_length=32, blank=True, null=True)
    value_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_mfilter_values'


class OcMpBlogAddpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    category_id = models.PositiveIntegerField()
    post_title = models.CharField(max_length=500)
    post_metakey = models.CharField(max_length=500)
    post_metadis = models.CharField(max_length=500)
    post_content = models.TextField()
    post_tags = models.CharField(max_length=300)
    post_date = models.CharField(max_length=64)
    customer_id = models.CharField(max_length=10)
    post_comments = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oc_mp_blog_addpost'


class OcMpBlogCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=500)
    customer_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oc_mp_blog_category'


class OcMpBlogComments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=18000)
    post_id = models.CharField(max_length=10)
    comments_show = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oc_mp_blog_comments'


class OcNitroCdnFiles(models.Model):
    file = models.TextField()
    realpath = models.TextField()
    cdn = models.IntegerField(blank=True, null=True)
    size = models.PositiveIntegerField()
    uploaded = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_nitro_cdn_files'


class OcNitroProductCache(models.Model):
    product_id = models.IntegerField()
    cachefile = models.TextField()
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_nitro_product_cache'


class OcOfferHomePage(models.Model):
    home_page_id = models.IntegerField(primary_key=True)
    meta_title = models.TextField()
    meta_tag = models.TextField()
    meta_description = models.TextField()
    meta_keyword = models.TextField()
    content = models.TextField()
    sentence_1 = models.TextField()
    sentence_2 = models.TextField()
    sentence_3 = models.TextField()
    modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_offer_home_page'


class OcOfferPage(models.Model):
    offer_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=50, blank=True, null=True)
    title = models.TextField()
    offer_type = models.IntegerField()
    blog_description = models.TextField(blank=True, null=True)
    blog_url = models.CharField(max_length=100, blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    overlay_text_1 = models.TextField(blank=True, null=True)
    overlay_text_2 = models.TextField(blank=True, null=True)
    meta_tag = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    added_on = models.DateTimeField(blank=True, null=True)
    modifieded_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_offer_page'


class OcOpenbayFaq(models.Model):
    route = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_openbay_faq'


class OcOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option'


class OcOptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_description'
        unique_together = (('option_id', 'language_id'),)


class OcOptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option_value'


class OcOptionValueDescription(models.Model):
    option_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


class OcOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=32)
    payment_company_id = models.CharField(max_length=32)
    payment_tax_id = models.CharField(max_length=32)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_landmark = models.CharField(max_length=50)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=32)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_landmark = models.CharField(max_length=50)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    ddw_delivery_date = models.DateTimeField(blank=True, null=True)
    ddw_time_slot = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_order'


class OcOrderDownload(models.Model):
    order_download_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    name = models.CharField(max_length=64)
    filename = models.CharField(max_length=128)
    mask = models.CharField(max_length=128)
    remaining = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_download'


class OcOrderField(models.Model):
    order_id = models.IntegerField(primary_key=True)
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.IntegerField()
    value = models.TextField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_field'
        unique_together = (('order_id', 'custom_field_id', 'custom_field_value_id'),)


class OcOrderFraud(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    country_match = models.CharField(max_length=3)
    country_code = models.CharField(max_length=2)
    high_risk_country = models.CharField(max_length=3)
    distance = models.IntegerField()
    ip_region = models.CharField(max_length=255)
    ip_city = models.CharField(max_length=255)
    ip_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    ip_longitude = models.DecimalField(max_digits=10, decimal_places=6)
    ip_isp = models.CharField(max_length=255)
    ip_org = models.CharField(max_length=255)
    ip_asnum = models.IntegerField()
    ip_user_type = models.CharField(max_length=255)
    ip_country_confidence = models.CharField(max_length=3)
    ip_region_confidence = models.CharField(max_length=3)
    ip_city_confidence = models.CharField(max_length=3)
    ip_postal_confidence = models.CharField(max_length=3)
    ip_postal_code = models.CharField(max_length=10)
    ip_accuracy_radius = models.IntegerField()
    ip_net_speed_cell = models.CharField(max_length=255)
    ip_metro_code = models.IntegerField()
    ip_area_code = models.IntegerField()
    ip_time_zone = models.CharField(max_length=255)
    ip_region_name = models.CharField(max_length=255)
    ip_domain = models.CharField(max_length=255)
    ip_country_name = models.CharField(max_length=255)
    ip_continent_code = models.CharField(max_length=2)
    ip_corporate_proxy = models.CharField(max_length=3)
    anonymous_proxy = models.CharField(max_length=3)
    proxy_score = models.IntegerField()
    is_trans_proxy = models.CharField(max_length=3)
    free_mail = models.CharField(max_length=3)
    carder_email = models.CharField(max_length=3)
    high_risk_username = models.CharField(max_length=3)
    high_risk_password = models.CharField(max_length=3)
    bin_match = models.CharField(max_length=10)
    bin_country = models.CharField(max_length=2)
    bin_name_match = models.CharField(max_length=3)
    bin_name = models.CharField(max_length=255)
    bin_phone_match = models.CharField(max_length=3)
    bin_phone = models.CharField(max_length=32)
    customer_phone_in_billing_location = models.CharField(max_length=8)
    ship_forward = models.CharField(max_length=3)
    city_postal_match = models.CharField(max_length=3)
    ship_city_postal_match = models.CharField(max_length=3)
    score = models.DecimalField(max_digits=10, decimal_places=5)
    explanation = models.TextField()
    risk_score = models.DecimalField(max_digits=10, decimal_places=5)
    queries_remaining = models.IntegerField()
    maxmind_id = models.CharField(max_length=8)
    error = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_fraud'


class OcOrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_history'


class OcOrderLimit(models.Model):
    status = models.IntegerField(blank=True, null=True)
    max_order_qty = models.CharField(max_length=64, blank=True, null=True)
    min_order_qty = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_order_limit'


class OcOrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_option'


class OcOrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'


class OcOrderRating(models.Model):
    order = models.ForeignKey(OcOrder, models.DO_NOTHING, unique=True)
    rating = models.CharField(max_length=1)
    comments = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'oc_order_rating'


class OcOrderRatingAttribute(models.Model):
    attribute = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'oc_order_rating_attribute'


class OcOrderRatingChoosenAttribute(models.Model):
    rating = models.ForeignKey(OcOrderRating, models.DO_NOTHING)
    attribute = models.ForeignKey(OcOrderRatingAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_order_rating_choosen_attribute'
        unique_together = (('rating', 'attribute'),)


class OcOrderRatingQueries(models.Model):
    query = models.CharField(unique=True, max_length=100)
    rating = models.CharField(unique=True, max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_order_rating_queries'


class OcOrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    created = models.DateTimeField()
    status = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    profile_id = models.IntegerField()
    profile_name = models.CharField(max_length=255)
    profile_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    profile_reference = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_order_recurring'


class OcOrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    created = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_order_recurring_transaction'


class OcOrderShippingTimeDuration(models.Model):
    order_shipping_time_duration_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    delivery_zone_id = models.IntegerField()
    timeslot_duration_id = models.IntegerField()
    date = models.DateField()
    time_duration = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_order_shipping_time_duration'


class OcOrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_status'
        unique_together = (('order_status_id', 'language_id'),)


class OcOrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_total'


class OcOrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_order_voucher'


class OcOtpVerify(models.Model):
    otp_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    phone_no = models.CharField(max_length=11)
    otp_code = models.IntegerField()
    verified = models.IntegerField()
    expiry = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_otp_verify'


class OcProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=13)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    viewed = models.IntegerField()
    mfilter_tags = models.TextField()
    mfilter_values = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product'
    def __str__(self):
        return self.sku

class OcProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


class OcProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    tag = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_description'
        unique_together = (('product_id', 'language_id'),)


class OcProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_discount'


class OcProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_filter'
        unique_together = (('product_id', 'filter_id'),)


class OcProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_image'


class OcProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_option'


class OcProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_product_option_value'


class OcProductProfile(models.Model):
    product_id = models.IntegerField(primary_key=True)
    profile_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_profile'
        unique_together = (('product_id', 'profile_id', 'customer_group_id'),)


class OcProductRecurring(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_recurring'
        unique_together = (('product_id', 'store_id'),)


class OcProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_related'
        unique_together = (('product_id', 'related_id'),)


class OcProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_reward'


class OcProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_special'


class OcProductToCategory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_category'
        unique_together = (('product_id', 'category_id'),)


class OcProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_download'
        unique_together = (('product_id', 'download_id'),)


class OcProductToLayout(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class OcProductToReward(models.Model):
    product_id = models.IntegerField()
    rule_id = models.IntegerField()
    reward_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_reward'


class OcProductToStore(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_store'
        unique_together = (('product_id', 'store_id'),)


class OcProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.PositiveIntegerField()
    cycle = models.PositiveIntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.PositiveIntegerField()
    trial_cycle = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_profile'


class OcProfileDescription(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_profile_description'
        unique_together = (('profile_id', 'language_id'),)


class OcRatingWeightage(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    percent = models.SmallIntegerField()
    user = models.CharField(unique=True, max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_rating_weightage'


class OcReturn(models.Model):
    return_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    opened = models.IntegerField()
    return_reason_id = models.IntegerField()
    return_action_id = models.IntegerField()
    return_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return'


class OcReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_return_action'
        unique_together = (('return_action_id', 'language_id'),)


class OcReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return_history'


class OcReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class OcReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_return_status'
        unique_together = (('return_status_id', 'language_id'),)


class OcReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_review'


class OcSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    group = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_setting'


class OcShoppingCartRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    conditions_serialized = models.TextField()
    store_view = models.CharField(max_length=255)
    customer_group_ids = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    actions = models.IntegerField()
    reward_per_spent = models.IntegerField()
    reward_point = models.IntegerField()
    rule_position = models.IntegerField()
    stop_rules_processing = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_shopping_cart_rules'


class OcSimpleBlogArticle(models.Model):
    simple_blog_article_id = models.AutoField(primary_key=True)
    simple_blog_author_id = models.IntegerField()
    allow_comment = models.IntegerField()
    image = models.TextField()
    featured_image = models.TextField()
    article_related_method = models.CharField(max_length=64)
    article_related_option = models.TextField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article'


class OcSimpleBlogArticleDescription(models.Model):
    simple_blog_article_description_id = models.AutoField(primary_key=True)
    simple_blog_article_id = models.IntegerField()
    language_id = models.IntegerField()
    article_title = models.CharField(max_length=256)
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_description'


class OcSimpleBlogArticleDescriptionAdditional(models.Model):
    simple_blog_article_id = models.IntegerField()
    language_id = models.IntegerField()
    additional_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_description_additional'


class OcSimpleBlogArticleProductRelated(models.Model):
    simple_blog_article_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_product_related'


class OcSimpleBlogArticleToCategory(models.Model):
    simple_blog_article_id = models.IntegerField()
    simple_blog_category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_category'


class OcSimpleBlogArticleToLayout(models.Model):
    simple_blog_article_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_layout'


class OcSimpleBlogArticleToStore(models.Model):
    simple_blog_article_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_store'


class OcSimpleBlogAuthor(models.Model):
    simple_blog_author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    image = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_author'


class OcSimpleBlogAuthorDescription(models.Model):
    simple_blog_author_description_id = models.AutoField(primary_key=True)
    simple_blog_author_id = models.IntegerField()
    language_id = models.IntegerField()
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_author_description'


class OcSimpleBlogCategory(models.Model):
    simple_blog_category_id = models.AutoField(primary_key=True)
    image = models.TextField()
    parent_id = models.IntegerField()
    top = models.IntegerField()
    blog_category_column = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category'


class OcSimpleBlogCategoryDescription(models.Model):
    simple_blog_category_description_id = models.AutoField(primary_key=True)
    simple_blog_category_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_description'


class OcSimpleBlogCategoryToLayout(models.Model):
    simple_blog_category_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_to_layout'


class OcSimpleBlogCategoryToStore(models.Model):
    simple_blog_category_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_to_store'


class OcSimpleBlogComment(models.Model):
    simple_blog_comment_id = models.AutoField(primary_key=True)
    simple_blog_article_id = models.IntegerField()
    simple_blog_article_reply_id = models.IntegerField()
    author = models.CharField(max_length=64)
    comment = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_comment'


class OcSimpleBlogRelatedArticle(models.Model):
    simple_blog_related_article_id = models.AutoField(primary_key=True)
    simple_blog_article_id = models.IntegerField()
    simple_blog_article_related_id = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_related_article'


class OcSimpleBlogView(models.Model):
    simple_blog_view_id = models.AutoField(primary_key=True)
    simple_blog_article_id = models.IntegerField()
    view = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_view'


class OcSmartsearch(models.Model):
    smartsearch_id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField()
    search = models.CharField(max_length=255)
    phase = models.IntegerField()
    results = models.IntegerField()
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'oc_smartsearch'


class OcSpecialCoupon(models.Model):
    abandon_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=10)
    coupon_type = models.CharField(max_length=1)
    discount = models.IntegerField()
    total_amount = models.IntegerField()
    uses = models.IntegerField()
    logged = models.IntegerField()
    free_shipping = models.IntegerField()
    customer_id = models.IntegerField()
    template_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    send_on = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_special_coupon'


class OcSpendingRules(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    conditions_serialized = models.TextField()
    store_view = models.CharField(max_length=255)
    customer_group_ids = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    actions = models.IntegerField()
    reward_per_spent = models.IntegerField()
    reward_point = models.IntegerField()
    rule_position = models.IntegerField()
    stop_rules_processing = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_spending_rules'


class OcStockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class OcStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_store'

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class OcStoreCheckout(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING, unique=True)
    min_amt = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_store_checkout'


class OcStoreExpressDelivery(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING, unique=True)
    tat_in = models.CharField(max_length=5)
    tat = models.SmallIntegerField()
    charge_per_order = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_store_express_delivery'


class OcStoreRating(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING)
    rating = models.CharField(max_length=1)
    comments = models.CharField(max_length=300)
    rating_by = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'oc_store_rating'


class OcStoreSeoUrlQr(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING, unique=True)
    qr_img_path = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_store_seo_url_qr'


class OcStoreTimings(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING)
    open_time = models.TimeField()
    close_time = models.TimeField()
    week_day = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'oc_store_timings'
        unique_together = (('store', 'week_day'),)


class OcStorelocatorGroup(models.Model):
    group_id = models.AutoField(unique=True,primary_key=True)
    group_name_backend = models.CharField(max_length=64)
    group_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_group'


class OcStorelocatorMap(models.Model):
    configuration_id = models.AutoField(unique=True,primary_key=True)
    map_id = models.IntegerField()
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_map'


class OcStorelocatorProductToStore(models.Model):
    storelocator_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_product_to_store'
        unique_together = (('storelocator_id', 'product_id'),)


class OcStorelocatorSearch(models.Model):
    storesearch_id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=12)
    ip_address = models.CharField(max_length=32)
    search_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_search'


class OcStorelocatorStore(models.Model):
    storelocator_id = models.AutoField(primary_key=True)
    store_name_backend = models.CharField(max_length=64)
    store_name = models.TextField()
    store_street = models.CharField(max_length=64)
    store_city = models.CharField(max_length=32)
    store_zip = models.CharField(max_length=8)
    store_country = models.CharField(max_length=32)
    order = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    icon = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_storelocator_store'

    def __str__(self):
        return self.store_name_backend

class OcStorelocatorStoreToGroup(models.Model):
    storelocator_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_store_to_group'
        unique_together = (('storelocator_id', 'group_id'),)


class OcStorelocatorStoreToMap(models.Model):
    storelocator_id = models.IntegerField(primary_key=True)
    map_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_storelocator_store_to_map'
        unique_together = (('storelocator_id', 'map_id'),)


class OcStoresMasterCategory(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING)
    master_category = models.ForeignKey(OcMasterCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oc_stores_master_category'
        unique_together = (('store', 'master_category'),)


class OcStoresWeekend(models.Model):
    store = models.ForeignKey(OcCustomerpartnerToCustomer, models.DO_NOTHING, primary_key=True)
    week_end = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_stores_weekend'
        unique_together = (('store', 'week_end'),)


class OcSubscribeUser(models.Model):
    subscribe_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_subscribe_user'


class OcSuburbArea(models.Model):
    suburb_id = models.AutoField(primary_key=True)
    suburb_name = models.CharField(max_length=200)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_suburb_area'


class OcTaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_class'


class OcTaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate'


class OcTaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class OcTaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rule'


class OcTbSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.PositiveSmallIntegerField()
    group = models.CharField(max_length=32)
    key = models.CharField(max_length=128)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tb_setting'


class OcTestimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_testimonial'


class OcTimeslot(models.Model):
    timeslot_id = models.AutoField(primary_key=True)
    city_id = models.IntegerField()
    timeslot_duration_id = models.CharField(max_length=255)
    weekend_blocks = models.CharField(max_length=255)
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    cutoff = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_timeslot'


class OcTimeslotDate(models.Model):
    timeslot_id = models.IntegerField()
    type = models.CharField(max_length=6)
    recurring = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_timeslot_date'


class OcTimeslotDescription(models.Model):
    timeslot_description_id = models.AutoField(primary_key=True)
    timeslot_id = models.IntegerField()
    language_id = models.IntegerField()
    lable = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_timeslot_description'


class OcTimeslotDuration(models.Model):
    timeslot_duration_id = models.AutoField(primary_key=True)
    time_duration = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_timeslot_duration'


class OcUrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_url_alias'


class OcUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_user'


class OcUserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_user_group'


class OcVoucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher'


class OcVoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher_history'


class OcVoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme'


class OcVoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class OcWeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_weight_class'


class OcWeightClassDescription(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class OcWkCustomField(models.Model):
    forseller = models.CharField(db_column='forSeller', max_length=10)  # Field name made lowercase.
    fieldtype = models.CharField(db_column='fieldType', max_length=100)  # Field name made lowercase.
    isrequired = models.CharField(db_column='isRequired', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field'


class OcWkCustomFieldDescription(models.Model):
    fieldid = models.IntegerField(db_column='fieldId')  # Field name made lowercase.
    fielddescription = models.CharField(db_column='fieldDescription', max_length=5000)  # Field name made lowercase.
    fieldname = models.CharField(db_column='fieldName', max_length=100)  # Field name made lowercase.
    language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field_description'


class OcWkCustomFieldOptionDescription(models.Model):
    optionid = models.IntegerField(db_column='optionId')  # Field name made lowercase.
    optionvalue = models.CharField(db_column='optionValue', max_length=100)  # Field name made lowercase.
    language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field_option_description'


class OcWkCustomFieldOptions(models.Model):
    optionid = models.AutoField(db_column='optionId', primary_key=True)  # Field name made lowercase.
    fieldid = models.IntegerField(db_column='fieldId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field_options'


class OcWkCustomFieldProduct(models.Model):
    fieldid = models.IntegerField(db_column='fieldId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='productId')  # Field name made lowercase.
    fieldtype = models.CharField(db_column='fieldType', max_length=100)  # Field name made lowercase.
    fielddescription = models.CharField(db_column='fieldDescription', max_length=5000)  # Field name made lowercase.
    fieldname = models.CharField(db_column='fieldName', max_length=100)  # Field name made lowercase.
    isrequired = models.CharField(db_column='isRequired', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field_product'


class OcWkCustomFieldProductOptions(models.Model):
    pro_id = models.IntegerField()
    product_id = models.IntegerField()
    fieldid = models.IntegerField(db_column='fieldId')  # Field name made lowercase.
    option_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_wk_custom_field_product_options'


class OcZone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_zone'


class OcZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_zone_to_geo_zone'


class DefaultRate(models.Model):
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)
    payment_gateway_pass = models.BooleanField(blank=True,default=False)
    tax_inclusive = models.BooleanField(blank=True,default=False)

class AdditionalCommRate(models.Model):
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)
    payment_gateway_pass = models.BooleanField(blank=True,default=False)
    tax_inclusive = models.BooleanField(blank=True,default=False)

class Promo(models.Model):
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    sku = models.ForeignKey(OcProduct,null=True,on_delete=models.DO_NOTHING)
    rate = models.DecimalField(decimal_places=2,max_digits=10)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)

DELIVERED_BY = (('STORE','STORE'),('EBAZR','EBAZR'),)

class DeliveryZone(models.Model):
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    pincodes = models.CharField(max_length=1023,null=True)
    delivered_by = models.CharField(max_length=100,choices=DELIVERED_BY)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)

TYPE = (
    ('FLAT PER ORDER','FLAT PER ORDER'),
    ('FLAT PER SKU','FLAT PER SKU'),
    ('PERCENTAGE','PERCENTAGE'),
    ('RATE PER CATEGORY','RATE PER CATEGORY'),
)

class ConcessionalRate(models.Model):
    type = models.CharField(max_length=100,choices=TYPE)
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    sku = models.ForeignKey(OcProduct,null=True,blank=True,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(OcCategory,null=True,blank=True,on_delete=models.DO_NOTHING)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)

class Penalty(models.Model):
    price = models.DecimalField(max_digits=10,decimal_places=2)
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    orders = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)
Reason = (
    ('Cancelled By Store','Cancelled By Store'),
    ('Customer Not Available','Customer Not Available'),
)
class Penalty_orders(models.Model):
    order_id = models.IntegerField()
    price = models.CharField(max_length=1023,null=True)
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING,null=True)
    reason = models.CharField(max_length=100,choices=Reason,null=True)

    def __str__(self):
        return str(self.order_id)

class Reimbursement(models.Model):
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING)
    thres_amt = models.DecimalField(decimal_places=2,max_digits=10)
    amt = models.DecimalField(decimal_places=2,max_digits=10)
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)

class PgFile(models.Model):
    order_id = models.IntegerField()
    order_amount = models.DecimalField(decimal_places=2,max_digits=10)
    pg_charges = models.DecimalField(decimal_places=2,max_digits=10)
    pg_gst = models.DecimalField(decimal_places=2,max_digits=10)
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING,null=True)

class GstStore(models.Model):
    gstno = models.CharField(max_length=100,null=True)
    store_name = models.ForeignKey(OcStorelocatorStore,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.gstno