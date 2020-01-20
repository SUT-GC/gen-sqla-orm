# -*- coding:utf8 -*-

from sqlalchemy import (
    Column,
    SmallInteger,
    BigInteger,
    String,
    Text,
    Float,
    DateTime,
    Integer,
)

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()


class ApplePayReceipt(Base):
    __tablename__ = "apple_pay_receipt"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    order_no = Column(String, name="order_no", default='', nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    receipt = Column(String, name="receipt", nullable=True)
    already_used = Column(Integer, name="already_used", default=0, nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class ApplePaySubscriptionReceipt(Base):
    __tablename__ = "apple_pay_subscription_receipt"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    order_no = Column(String, name="order_no", default='', nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    receipt = Column(String, name="receipt", nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)


class ApplePaySubscriptionRenewal(Base):
    __tablename__ = "apple_pay_subscription_renewal"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    purchase_date = Column(DateTime, name="purchase_date", nullable=True)
    expires_date = Column(DateTime, name="expires_date", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)
    original_transaction_id = Column(String, name="original_transaction_id", nullable=True)
    status = Column(Integer, name="status", nullable=True)
    tob = Column(Integer, name="tob", default=1, nullable=True)


class CashCommodity(Base):
    __tablename__ = "cash_commodity"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    store_type = Column(String, name="store_type", nullable=True)
    identity = Column(String, name="identity", nullable=True)
    item_name = Column(String, name="item_name", nullable=True)
    subtitle = Column(String, name="subtitle", default='', nullable=True)
    commodity_intro = Column(String, name="commodity_intro", default='', nullable=True)
    commodity_url = Column(String, name="commodity_url", default='', nullable=True)
    online = Column(Integer, name="online", default=0, nullable=True)
    delete_flag = Column(Integer, name="delete_flag", nullable=True)
    sales_unit = Column(String, name="sales_unit", default='', nullable=True)
    sales_unit_value = Column(Integer, name="sales_unit_value", default=0, nullable=True)
    first_category = Column(String, name="first_category", nullable=True)
    second_category = Column(String, name="second_category", nullable=True)
    item_identity = Column(String, name="item_identity", default='', nullable=True)
    stock_type = Column(Integer, name="stock_type", default=-1, nullable=True)
    default_group = Column(Integer, name="default_group", default=1, nullable=False)
    ext_attributes = Column(String, name="ext_attributes", default='', nullable=True)
    p_order = Column(Integer, name="p_order", nullable=True)
    enable_ab = Column(Integer, name="enable_ab", default=0, nullable=False)
    type = Column(Integer, name="type", default=1, nullable=False)
    mutex_type = Column(Integer, name="mutex_type", default=1, nullable=False)
    gender_type = Column(Integer, name="gender_type", default=0, nullable=True)
    gift_flag = Column(Integer, name="gift_flag", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    scene_type = Column(Integer, name="scene_type", default=0, nullable=False)
    first_child_category = Column(String, name="first_child_category", nullable=True)
    corner_mark_url = Column(String, name="corner_mark_url", nullable=True)


class CoinCommodity(Base):
    __tablename__ = "coin_commodity"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    first_category = Column(String, name="first_category", nullable=False)
    second_category = Column(String, name="second_category", nullable=False)
    item_identity = Column(String, name="item_identity", nullable=False)
    item_name = Column(String, name="item_name", nullable=True)
    subtitle = Column(String, name="subtitle", default='', nullable=True)
    commodity_intro = Column(String, name="commodity_intro", default='', nullable=True)
    commodity_url = Column(String, name="commodity_url", default='', nullable=True)
    commodity_level = Column(Integer, name="commodity_level", default=0, nullable=True)
    stock_type = Column(Integer, name="stock_type", default=-1, nullable=True)
    online = Column(Integer, name="online", default=0, nullable=True)
    delete_flag = Column(Integer, name="delete_flag", default=0, nullable=True)
    sales_unit = Column(String, name="sales_unit", nullable=True)
    sales_unit_value = Column(Integer, name="sales_unit_value", nullable=True)
    free_times = Column(Integer, name="free_times", default=0, nullable=False)
    free_start_time = Column(DateTime, name="free_start_time", default=datetime.now(), nullable=False)
    free_end_time = Column(DateTime, name="free_end_time", default=datetime.now(), nullable=False)
    p_order = Column(Integer, name="p_order", nullable=True)
    enable_ab = Column(Integer, name="enable_ab", default=0, nullable=False)
    type = Column(Integer, name="type", default=1, nullable=False)
    mutex_type = Column(Integer, name="mutex_type", default=1, nullable=False)
    default_group = Column(Integer, name="default_group", default=1, nullable=False)
    ext_attributes = Column(String, name="ext_attributes", default='', nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    gender_type = Column(Integer, name="gender_type", default=0, nullable=True)
    corner_mark_url = Column(String, name="corner_mark_url", default='', nullable=True)
    first_child_category = Column(String, name="first_child_category", nullable=True)
    period_config = Column(String, name="period_config", default='', nullable=False)


class CoinCommodityFreeConfigure(Base):
    __tablename__ = "coin_commodity_free_configure"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    configure_id = Column(String, name="configure_id", default='', nullable=False)
    item_identity = Column(String, name="item_identity", default='', nullable=False)
    free_times = Column(Integer, name="free_times", default=0, nullable=False)
    free_start_time = Column(DateTime, name="free_start_time", default=datetime.now(), nullable=False)
    free_end_time = Column(DateTime, name="free_end_time", default=datetime.now(), nullable=False)
    is_valid = Column(Integer, name="is_valid", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class CoinCommodityPackageRelation(Base):
    __tablename__ = "coin_commodity_package_relation"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    package_item_identity = Column(String, name="package_item_identity", default='', nullable=False)
    relation_item_identity = Column(String, name="relation_item_identity", default='', nullable=False)
    amount = Column(Integer, name="amount", default=0, nullable=False)
    valid = Column(Integer, name="valid", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class CommodityCategory(Base):
    __tablename__ = "commodity_category"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    category_name = Column(String, name="category_name", nullable=False)
    category_code = Column(String, name="category_code", nullable=False)
    parent_code = Column(String, name="parent_code", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    online_flag = Column(Integer, name="online_flag", default=0, nullable=True)
    delete_flag = Column(Integer, name="delete_flag", default=0, nullable=True)
    category_type = Column(Integer, name="category_type", nullable=True)


class CommodityPrivilegePkgRelation(Base):
    __tablename__ = "commodity_privilege_pkg_relation"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    commodity_identity = Column(String, name="commodity_identity", nullable=False)
    commodity_category = Column(Integer, name="commodity_category", nullable=True)
    privilege_package_identity = Column(String, name="privilege_package_identity", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), primary_key=True, nullable=False)


class GiftProduct(Base):
    __tablename__ = "gift_product"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    cash_commodity_id = Column(BigInteger, name="cash_commodity_id", default=0, nullable=False)
    item_identity = Column(String, name="item_identity", default='', nullable=False)
    item_rule = Column(Integer, name="item_rule", default=100, nullable=False)
    gift_product_name = Column(String, name="gift_product_name", default='', nullable=False)
    item_type = Column(Integer, name="item_type", default=1, nullable=False)
    gift_unit = Column(String, name="gift_unit", default='', nullable=False)
    gift_unit_value = Column(Integer, name="gift_unit_value", default=0, nullable=False)
    gift_intro = Column(String, name="gift_intro", default='', nullable=False)
    promotion_intro = Column(String, name="promotion_intro", default='', nullable=False)
    start_time = Column(DateTime, name="start_time", default=datetime.now(), nullable=False)
    end_time = Column(DateTime, name="end_time", default=datetime.now(), nullable=False)
    status = Column(Integer, name="status", default=1, nullable=False)
    is_valid = Column(Integer, name="is_valid", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class Privilege(Base):
    __tablename__ = "privilege"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    identity = Column(String, name="identity", nullable=False)
    name = Column(String, name="name", nullable=True)
    description = Column(String, name="description", nullable=True)
    state = Column(Integer, name="state", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class PrivilegePackage(Base):
    __tablename__ = "privilege_package"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    identity = Column(String, name="identity", nullable=False)
    name = Column(String, name="name", nullable=True)
    description = Column(String, name="description", nullable=True)
    state = Column(Integer, name="state", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class PrivilegePackageRelation(Base):
    __tablename__ = "privilege_package_relation"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    privilege_package_identity = Column(String, name="privilege_package_identity", nullable=True)
    privilege_identity = Column(String, name="privilege_identity", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class SceneCommodity(Base):
    __tablename__ = "scene_commodity"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    scene_id = Column(BigInteger, name="scene_id", nullable=False)
    first_category = Column(String, name="first_category", nullable=False)
    item_identity = Column(String, name="item_identity", nullable=False)
    validation = Column(Integer, name="validation", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class UserCoinCommodityTimes(Base):
    __tablename__ = "user_coin_commodity_times"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", default=0, nullable=False)
    info = Column(Text, name="info", nullable=False)
    is_valid = Column(Integer, name="is_valid", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class WechatSubscriptionContract(Base):
    __tablename__ = "wechat_subscription_contract"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    contract_code = Column(String, name="contract_code", nullable=False)
    plan_id = Column(String, name="plan_id", nullable=False)
    change_type = Column(String, name="change_type", nullable=True)
    operate_time = Column(String, name="operate_time", nullable=False)
    contract_id = Column(String, name="contract_id", nullable=True)
    json_str = Column(Text, name="json_str", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class WechatSubscriptionTimer(Base):
    __tablename__ = "wechat_subscription_timer"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    contract_id = Column(String, name="contract_id", nullable=False)
    order_no = Column(String, name="order_no", nullable=False)
    commodity_identity = Column(String, name="commodity_identity", nullable=False)
    plan_id = Column(String, name="plan_id", nullable=False)
    total_fee = Column(Float, name="total_fee", nullable=False)
    begin_time = Column(DateTime, name="begin_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    retry_times = Column(Integer, name="retry_times", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
