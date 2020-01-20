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


class AccessUrlLog(Base):
    __tablename__ = "access_url_log"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    url = Column(String, name="url", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=False)


class AccountCancel(Base):
    __tablename__ = "account_cancel"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    area = Column(String, name="area", nullable=True)
    phone = Column(String, name="phone", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    state = Column(SmallInteger, name="state", nullable=True)
    post_number = Column(BigInteger, name="post_number", nullable=True)
    popularity = Column(BigInteger, name="popularity", nullable=True)
    follow_number = Column(BigInteger, name="follow_number", nullable=True)
    follower_number = Column(BigInteger, name="follower_number", nullable=True)
    del_flag = Column(Integer, name="del_flag", nullable=True)
    reg_time = Column(DateTime, name="reg_time", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class ActivityMatchIdMapping0(Base):
    __tablename__ = "activity_match_id_mapping0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    activity_id = Column(BigInteger, name="activity_id", nullable=False)
    identity_number = Column(Integer, name="identity_number", nullable=False)
    identity_desc = Column(String, name="identity_desc", nullable=False)
    state = Column(Integer, name="state", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class ActivityMatchInfo0(Base):
    __tablename__ = "activity_match_info0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    planet_entrance = Column(Integer, name="planet_entrance", default=1, nullable=False)
    h5_title = Column(String, name="h5_title", nullable=False)
    activity_name = Column(String, name="activity_name", nullable=True)
    show_time = Column(DateTime, name="show_time", nullable=False)
    open_time = Column(DateTime, name="open_time", nullable=False)
    close_time = Column(DateTime, name="close_time", nullable=False)
    icon = Column(String, name="icon", nullable=True)
    description = Column(String, name="description", nullable=True)
    activity_image_url = Column(String, name="activity_image_url", nullable=False)
    im_card_url = Column(String, name="im_card_url", nullable=False)
    push_content = Column(String, name="push_content", nullable=False)
    state = Column(Integer, name="state", default=1, nullable=False)
    checked = Column(Integer, name="checked", default=0, nullable=False)
    check_admin_id = Column(Integer, name="check_admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class ActivityMatchRule0(Base):
    __tablename__ = "activity_match_rule0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    activity_id = Column(BigInteger, name="activity_id", nullable=False)
    identity_number = Column(Integer, name="identity_number", nullable=False)
    state = Column(Integer, name="state", default=1, nullable=False)
    target_identity_number = Column(Integer, name="target_identity_number", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class AdSource(Base):
    __tablename__ = "ad_source"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    channel = Column(String, name="channel", nullable=True)
    device = Column(String, name="device", nullable=True)
    agent = Column(String, name="agent", nullable=True)
    activity = Column(String, name="activity", nullable=True)
    sub_channel = Column(String, name="sub_channel", nullable=True)
    url = Column(String, name="url", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class AdSourceFunction(Base):
    __tablename__ = "ad_source_function"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    source_id = Column(BigInteger, name="source_id", nullable=True)
    function = Column(String, name="function", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class AdSourceLabel(Base):
    __tablename__ = "ad_source_label"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    source_id = Column(BigInteger, name="source_id", nullable=True)
    label = Column(String, name="label", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class AdminActionStats(Base):
    __tablename__ = "admin_action_stats"

    admin_id = Column(BigInteger, name="admin_id", primary_key=True, nullable=False)
    reviewed_complaint_number = Column(Integer, name="reviewed_complaint_number", nullable=True)
    user_function_auth_number = Column(Integer, name="user_function_auth_number", nullable=True)
    delete_user_number = Column(Integer, name="delete_user_number", nullable=True)
    locked_post_number = Column(Integer, name="locked_post_number", nullable=True)
    date = Column(String, name="date", primary_key=True, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), primary_key=True, nullable=False)


class AdminLoginRecord(Base):
    __tablename__ = "admin_login_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    action = Column(String, name="action", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class AdminPool(Base):
    __tablename__ = "admin_pool"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class AdminPost(Base):
    __tablename__ = "admin_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=True)


class AdminPush(Base):
    __tablename__ = "admin_push"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    notice_title = Column(String, name="notice_title", nullable=False)
    notice_content = Column(String, name="notice_content", nullable=False)
    state = Column(String, name="state", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=False)
    send_time = Column(DateTime, name="send_time", nullable=True)


class AdminRecommendPool(Base):
    __tablename__ = "admin_recommend_pool"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    recommend_admin_id = Column(BigInteger, name="recommend_admin_id", nullable=False)
    source_type = Column(Integer, name="source_type", nullable=True)
    state = Column(String, name="state", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class AdminTelephone(Base):
    __tablename__ = "admin_telephone"

    telephone = Column(String, name="telephone", primary_key=True, nullable=False)


class AdminUser(Base):
    __tablename__ = "admin_user"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    nickname = Column(String, name="nickname", nullable=True)
    username = Column(String, name="username", nullable=True)
    pswd = Column(String, name="pswd", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    last_login_time = Column(DateTime, name="last_login_time", nullable=True)
    status = Column(BigInteger, name="status", default=1, nullable=True)


class AdminValidateCode(Base):
    __tablename__ = "admin_validate_code"

    url = Column(String, name="url", primary_key=True, nullable=False)
    code = Column(String, name="code", nullable=False)


class AntiSpamStrategyReview(Base):
    __tablename__ = "anti_spam_strategy_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    strategy_id = Column(Integer, name="strategy_id", nullable=False)
    reason_desc = Column(String, name="reason_desc", nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    strategy_admin_id = Column(BigInteger, name="strategy_admin_id", nullable=True)
    handle_admin_id = Column(BigInteger, name="handle_admin_id", nullable=True)
    handle_action = Column(SmallInteger, name="handle_action", default=0, nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)


class AssistantQa(Base):
    __tablename__ = "assistant_qa"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    keywords = Column(String, name="keywords", nullable=True)
    content = Column(String, name="content", nullable=True)
    parent = Column(String, name="parent", nullable=True)
    type = Column(Integer, name="type", nullable=True)
    answer = Column(Text, name="answer", nullable=True)
    sort = Column(Integer, name="sort", nullable=True)
    use_num = Column(Integer, name="use_num", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    feedback_id = Column(BigInteger, name="feedback_id", nullable=True)
    type = Column(Integer, name="type", nullable=True)
    url = Column(String, name="url", nullable=True)


class AutoBreak(Base):
    __tablename__ = "auto_break"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    uid = Column(BigInteger, name="uid", nullable=True)
    target_id = Column(BigInteger, name="target_id", nullable=True)
    room = Column(String, name="room", nullable=True)
    type = Column(Integer, name="type", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class AutoReply(Base):
    __tablename__ = "auto_reply"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    key = Column(String, name="key", nullable=True)
    question = Column(String, name="question", nullable=True)
    answer = Column(String, name="answer", nullable=True)
    use_num = Column(BigInteger, name="use_num", default=0, nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)


class BlackWord(Base):
    __tablename__ = "black_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=True)
    content = Column(String, name="content", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    remark = Column(String, name="remark", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class BlockDevice(Base):
    __tablename__ = "block_device"

    device_id = Column(String, name="device_id", primary_key=True, nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    user_ids = Column(String, name="user_ids", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)


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


class CheatUser(Base):
    __tablename__ = "cheat_user"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    target_user_id = Column(BigInteger, name="target_user_id", nullable=True)
    message_time = Column(DateTime, name="message_time", nullable=True)
    content = Column(String, name="content", nullable=True)
    spam_words = Column(String, name="spam_words", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    layer = Column(String, name="layer", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    review_time = Column(DateTime, name="review_time", nullable=True)


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


class ComlaintSync(Base):
    __tablename__ = "comlaint_sync"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    complaint_id = Column(BigInteger, name="complaint_id", nullable=False)
    state = Column(Integer, name="state", default=1, nullable=False)
    reviewed = Column(Integer, name="reviewed", default=0, nullable=False)
    admin_id = Column(Integer, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class CommentReviewRecord(Base):
    __tablename__ = "comment_review_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author_id = Column(BigInteger, name="post_author_id", nullable=True)
    comment_id = Column(BigInteger, name="comment_id", nullable=True)
    comment_author_id = Column(BigInteger, name="comment_author_id", nullable=True)
    comment_create_time = Column(DateTime, name="comment_create_time", nullable=True)
    comment_pre_handle_reason = Column(SmallInteger, name="comment_pre_handle_reason", nullable=True)
    comment_pre_handle_remark = Column(String, name="comment_pre_handle_remark", nullable=True)
    pool_code = Column(SmallInteger, name="pool_code", nullable=True)
    comment_handle_action = Column(SmallInteger, name="comment_handle_action", default=0, nullable=True)
    author_handle_action = Column(SmallInteger, name="author_handle_action", default=0, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


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


class ComplaintExt(Base):
    __tablename__ = "complaint_ext"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_type = Column(String, name="target_type", nullable=True)
    target_id = Column(BigInteger, name="target_id", nullable=True)
    target_user_id = Column(BigInteger, name="target_user_id", nullable=False)
    target_post_id = Column(BigInteger, name="target_post_id", nullable=True)
    target_comment_id = Column(BigInteger, name="target_comment_id", nullable=True)
    target_expression_id = Column(BigInteger, name="target_expression_id", nullable=True)
    target_chat_id = Column(BigInteger, name="target_chat_id", nullable=True)
    author_id = Column(BigInteger, name="author_id", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    content = Column(String, name="content", nullable=True)
    image_url = Column(String, name="image_url", nullable=True)
    review_state = Column(String, name="review_state", nullable=True)
    reviewer_id = Column(BigInteger, name="reviewer_id", nullable=True)
    review_action = Column(String, name="review_action", nullable=True)
    review_time = Column(DateTime, name="review_time", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    explain_txt = Column(String, name="explain_txt", default='', nullable=True)


class ComplaintStats(Base):
    __tablename__ = "complaint_stats"

    date = Column(String, name="date", primary_key=True, nullable=False)
    complaint_number = Column(Integer, name="complaint_number", nullable=True)
    target_user_number = Column(Integer, name="target_user_number", nullable=True)
    reviewed_complaint_number = Column(Integer, name="reviewed_complaint_number", nullable=True)
    user_function_auth_number = Column(Integer, name="user_function_auth_number", nullable=True)
    delete_user_number = Column(Integer, name="delete_user_number", nullable=True)
    locked_post_number = Column(Integer, name="locked_post_number", nullable=True)
    chat_handled_number = Column(Integer, name="chat_handled_number", nullable=True)
    user_handled_number = Column(Integer, name="user_handled_number", nullable=True)
    post_complaint_number = Column(Integer, name="post_complaint_number", nullable=True)
    chat_complaint_number = Column(Integer, name="chat_complaint_number", nullable=True)
    comment_complaint_number = Column(Integer, name="comment_complaint_number", nullable=True)
    specialword_complaint_number = Column(Integer, name="specialword_complaint_number", nullable=True)


class DiscoverLabelPostMapping(Base):
    __tablename__ = "discover_label_post_mapping"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    label_id = Column(String, name="label_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class DiscoverPost(Base):
    __tablename__ = "discover_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_type = Column(SmallInteger, name="post_type", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    url_index = Column(SmallInteger, name="url_index", nullable=True)
    url = Column(String, name="url", nullable=True)
    response = Column(String, name="response", nullable=True)
    rec_state = Column(SmallInteger, name="rec_state", default=0, nullable=True)
    interest_labels = Column(String, name="interest_labels", nullable=True)
    interest_labels_path = Column(String, name="interest_labels_path", nullable=True)
    beauty_score = Column(Float, name="beauty_score", nullable=True)
    cluster_id = Column(Integer, name="cluster_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_by = Column(BigInteger, name="modify_by", nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class DiscoverPostReview(Base):
    __tablename__ = "discover_post_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    queue_code = Column(Integer, name="queue_code", nullable=True)
    beauty_score = Column(Float, name="beauty_score", nullable=True)
    cluster_id = Column(Integer, name="cluster_id", nullable=True)
    handle_action = Column(Integer, name="handle_action", default=-1, nullable=True)
    original_interest_labels = Column(String, name="original_interest_labels", nullable=True)
    present_interest_labels = Column(String, name="present_interest_labels", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    watch_time = Column(DateTime, name="watch_time", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class DvAction(Base):
    __tablename__ = "dv_action"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    state = Column(BigInteger, name="state", default=0, nullable=False)
    result = Column(BigInteger, name="result", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class DvScoreAction(Base):
    __tablename__ = "dv_score_action"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    start = Column(Float, name="start", nullable=False)
    end = Column(Float, name="end", nullable=False)
    action = Column(BigInteger, name="action", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class EasemobRecord(Base):
    __tablename__ = "easemob_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    reason = Column(String, name="reason", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    content = Column(String, name="content", nullable=True)
    version = Column(String, name="version", nullable=True)
    system = Column(Integer, name="system", nullable=True)
    is_read = Column(Integer, name="is_read", nullable=True)
    admin_flag = Column(String, name="admin_flag", nullable=True)
    type = Column(Integer, name="type", nullable=True)
    noticesystem_id = Column(BigInteger, name="noticesystem_id", nullable=True)
    phone = Column(String, name="phone", nullable=True)
    user_agent = Column(String, name="user_agent", nullable=True)
    admin_user_id = Column(BigInteger, name="admin_user_id", nullable=True)
    gender = Column(Integer, name="gender", nullable=True)


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


class GlobalPermission(Base):
    __tablename__ = "global_permission"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", nullable=False)
    resource_type = Column(Integer, name="resource_type", nullable=True)
    url = Column(String, name="url", nullable=True)
    permission = Column(String, name="permission", nullable=True)
    parent_id = Column(BigInteger, name="parent_id", default=0, nullable=True)
    parent_ids = Column(String, name="parent_ids", nullable=True)
    available = Column(Integer, name="available", default=1, nullable=True)
    icon = Column(String, name="icon", nullable=True)
    permission_order = Column(Integer, name="permission_order", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    order = Column(BigInteger, name="order", nullable=True)


class GlobalRole(Base):
    __tablename__ = "global_role"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    role = Column(String, name="role", nullable=True)
    description = Column(String, name="description", nullable=True)
    available = Column(Integer, name="available", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class GlobalRolePermission(Base):
    __tablename__ = "global_role_permission"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    permission_id = Column(BigInteger, name="permission_id", nullable=False)
    role_id = Column(BigInteger, name="role_id", nullable=False)


class GlobalUserRole(Base):
    __tablename__ = "global_user_role"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    role_id = Column(BigInteger, name="role_id", nullable=False)


class GlobalUserRoleRecord(Base):
    __tablename__ = "global_user_role_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    oper_id = Column(BigInteger, name="oper_id", nullable=False)
    oper_name = Column(String, name="oper_name", nullable=False)
    oper_target_id = Column(BigInteger, name="oper_target_id", nullable=False)
    oper_target_name = Column(String, name="oper_target_name", nullable=False)
    oper_type = Column(String, name="oper_type", nullable=False)
    content_id = Column(BigInteger, name="content_id", nullable=False)
    content = Column(String, name="content", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=False)
    type = Column(String, name="type", nullable=False)


class H5Config0(Base):
    __tablename__ = "h5_config0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    title_name = Column(String, name="title_name", nullable=True)
    type = Column(SmallInteger, name="type", nullable=True)
    title_url = Column(String, name="title_url", nullable=True)
    head_title = Column(String, name="head_title", nullable=True)
    sub_title = Column(String, name="sub_title", nullable=True)
    share_url = Column(String, name="share_url", nullable=True)
    if_share = Column(Integer, name="if_share", nullable=True)
    share_config = Column(String, name="share_config", nullable=True)
    android_version = Column(String, name="android_version", nullable=True)
    ios_version = Column(String, name="ios_version", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)


class HotWord(Base):
    __tablename__ = "hot_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    word = Column(String, name="word", nullable=False)
    group_id = Column(BigInteger, name="group_id", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class HotWordGroup(Base):
    __tablename__ = "hot_word_group"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    rank = Column(BigInteger, name="rank", nullable=False)
    primary_tag_id = Column(BigInteger, name="primary_tag_id", nullable=False)
    primary_tag_name = Column(String, name="primary_tag_name", nullable=False)
    edit_time = Column(DateTime, name="edit_time", nullable=True)
    add_tag_id = Column(BigInteger, name="add_tag_id", nullable=True)
    add_tag_name = Column(String, name="add_tag_name", nullable=True)
    edit_admin_id = Column(BigInteger, name="edit_admin_id", nullable=True)
    safe_check_state = Column(Integer, name="safe_check_state", default=1, nullable=False)
    safe_check_desc = Column(String, name="safe_check_desc", nullable=True)
    safe_check_admin_id = Column(BigInteger, name="safe_check_admin_id", nullable=True)
    public_relation_check_state = Column(Integer, name="public_relation_check_state", default=1, nullable=False)
    public_relation_check_desc = Column(String, name="public_relation_check_desc", nullable=True)
    public_relation_check_admin_id = Column(BigInteger, name="public_relation_check_admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class HotWordPost(Base):
    __tablename__ = "hot_word_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    word_id = Column(BigInteger, name="word_id", nullable=False)
    group_id = Column(BigInteger, name="group_id", nullable=False)
    exposure = Column(BigInteger, name="exposure", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class HtmlPageConfig0(Base):
    __tablename__ = "html_page_config0"

    id = Column(Integer, name="id", primary_key=True, nullable=False, autoincrement=True)
    page_name = Column(String, name="page_name", default='', nullable=False)
    jump_content = Column(String, name="jump_content", nullable=True)
    jump_url = Column(String, name="jump_url", nullable=True)
    status = Column(Integer, name="status", default=1, nullable=False)
    attachment_url = Column(String, name="attachment_url", nullable=True)
    can_share = Column(Integer, name="can_share", default=2, nullable=False)
    share_title = Column(String, name="share_title", nullable=True)
    share_subtitle = Column(String, name="share_subtitle", nullable=True)
    share_img_url = Column(String, name="share_img_url", nullable=True)
    button_img_url = Column(String, name="button_img_url", nullable=True)
    button_width = Column(Integer, name="button_width", nullable=True)
    button_height = Column(Integer, name="button_height", nullable=True)
    btn_to_top = Column(Integer, name="btn_to_top", nullable=True)
    btn_to_left = Column(Integer, name="btn_to_left", nullable=True)
    ios_min_version = Column(String, name="ios_min_version", nullable=True)
    android_min_version = Column(String, name="android_min_version", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=False)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class IllegalSelfie(Base):
    __tablename__ = "illegal_selfie"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    url = Column(String, name="url", nullable=True)
    url_encode = Column(String, name="url_encode", nullable=True)
    remake = Column(String, name="remake", nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class InterestLabel(Base):
    __tablename__ = "interest_label"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    label_id = Column(String, name="label_id", nullable=True)
    label_name = Column(String, name="label_name", nullable=True)
    parent_id = Column(String, name="parent_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    state = Column(Integer, name="state", default=0, nullable=True)
    visibility = Column(Integer, name="visibility", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class InterestLabelQueue(Base):
    __tablename__ = "interest_label_queue"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    queue_id = Column(Integer, name="queue_id", nullable=False)
    queue_type = Column(Integer, name="queue_type", nullable=True)
    name = Column(String, name="name", nullable=True)
    first_label = Column(String, name="first_label", nullable=True)
    second_label = Column(String, name="second_label", nullable=True)
    priority = Column(Integer, name="priority", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    state = Column(Integer, name="state", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class InterestTestAnswer(Base):
    __tablename__ = "interest_test_answer"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    answer_id = Column(BigInteger, name="answer_id", nullable=True)
    content = Column(String, name="content", nullable=True)
    wx_image_url = Column(String, name="wx_image_url", nullable=True)
    out_image_url = Column(String, name="out_image_url", nullable=True)
    image_url = Column(String, name="image_url", nullable=True)
    background_image_url = Column(String, name="background_image_url", nullable=True)
    button_image_url = Column(String, name="button_image_url", nullable=True)
    button_jump_url = Column(String, name="button_jump_url", nullable=True)
    target_test_id = Column(BigInteger, name="target_test_id", default=0, nullable=True)
    threshold = Column(BigInteger, name="threshold", default=0, nullable=True)
    answer_x = Column(String, name="answer_x", nullable=True)
    answer_y = Column(String, name="answer_y", nullable=True)
    order = Column(Integer, name="order", nullable=True)
    market_template_type = Column(Integer, name="market_template_type", nullable=True)
    market_image_download_url = Column(String, name="market_image_download_url", nullable=True)


class InterestTestAnswerTemp(Base):
    __tablename__ = "interest_test_answer_temp"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    content = Column(String, name="content", nullable=True)
    wx_image_url = Column(String, name="wx_image_url", nullable=True)
    out_image_url = Column(String, name="out_image_url", nullable=True)
    image_url = Column(String, name="image_url", nullable=True)
    background_image_url = Column(String, name="background_image_url", nullable=True)
    button_image_url = Column(String, name="button_image_url", nullable=True)
    button_jump_url = Column(String, name="button_jump_url", nullable=True)
    target_test_id = Column(BigInteger, name="target_test_id", nullable=False)


class InterestTestList(Base):
    __tablename__ = "interest_test_list"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    content = Column(String, name="content", nullable=True)
    title_image_url = Column(String, name="title_image_url", nullable=True)
    index_image_url = Column(String, name="index_image_url", nullable=True)
    is_deleted = Column(Integer, name="is_deleted", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    order = Column(BigInteger, name="order", nullable=True)
    type = Column(String, name="type", nullable=True)
    target_url = Column(String, name="target_url", nullable=True)
    test_number = Column(BigInteger, name="test_number", default=0, nullable=True)
    exact_rate = Column(Float, name="exact_rate", default=1.00, nullable=True)
    show_type = Column(String, name="show_type", default='app', nullable=True)
    source_type = Column(Integer, name="source_type", nullable=True)
    has_answer_pic = Column(Integer, name="has_answer_pic", nullable=True)
    target_answer_type = Column(Integer, name="target_answer_type", nullable=True)
    question_count = Column(Integer, name="question_count", nullable=True)
    answer_count = Column(Integer, name="answer_count", nullable=True)
    index_image_x = Column(String, name="index_image_x", nullable=True)
    index_image_y = Column(String, name="index_image_y", nullable=True)
    show_last_question = Column(Integer, name="show_last_question", nullable=True)
    inaccuracy_count = Column(BigInteger, name="inaccuracy_count", default=0, nullable=True)
    accuracy_count = Column(BigInteger, name="accuracy_count", default=1, nullable=True)
    download_url = Column(String, name="download_url", nullable=True)
    test_background_image_url = Column(String, name="test_background_image_url", nullable=True)
    question_background_image_url = Column(String, name="question_background_image_url", nullable=True)
    option_background_image_url = Column(String, name="option_background_image_url", nullable=True)
    high_grade = Column(Float, name="high_grade", default=0.00, nullable=True)
    app_share_pv = Column(BigInteger, name="app_share_pv", default=0, nullable=True)


class InterestTestListTemp(Base):
    __tablename__ = "interest_test_list_temp"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    content = Column(String, name="content", nullable=True)
    title_image_url = Column(String, name="title_image_url", nullable=False)
    index_image_url = Column(String, name="index_image_url", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    order = Column(BigInteger, name="order", nullable=True)
    type = Column(String, name="type", nullable=True)
    target_url = Column(String, name="target_url", nullable=True)
    test_number = Column(BigInteger, name="test_number", default=0, nullable=True)
    exact_rate = Column(Float, name="exact_rate", default=1.00000000, nullable=True)
    show_type = Column(String, name="show_type", default='app', nullable=True)
    source_type = Column(Integer, name="source_type", nullable=True)


class InterestTestOption(Base):
    __tablename__ = "interest_test_option"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_question_id = Column(BigInteger, name="target_question_id", nullable=True)
    order = Column(BigInteger, name="order", nullable=True)
    skip_to_question_id = Column(BigInteger, name="skip_to_question_id", nullable=True)
    target_result_id = Column(String, name="target_result_id", nullable=True)
    content = Column(String, name="content", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    option_attachment_url = Column(String, name="option_attachment_url", nullable=True)
    skip_type = Column(Integer, name="skip_type", default=1, nullable=True)
    question_score = Column(BigInteger, name="question_score", default=0, nullable=True)


class InterestTestOptionTemp(Base):
    __tablename__ = "interest_test_option_temp"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_question_id = Column(BigInteger, name="target_question_id", nullable=False)
    order = Column(BigInteger, name="order", nullable=True)
    skip_to_question_id = Column(BigInteger, name="skip_to_question_id", nullable=True)
    target_result_id = Column(BigInteger, name="target_result_id", nullable=True)
    content = Column(String, name="content", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)


class InterestTestQuestion(Base):
    __tablename__ = "interest_test_question"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_test_id = Column(BigInteger, name="target_test_id", nullable=True)
    order = Column(BigInteger, name="order", nullable=True)
    question_title = Column(String, name="question_title", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)
    question_attachment_url = Column(String, name="question_attachment_url", nullable=True)


class InterestTestQuestionTemp(Base):
    __tablename__ = "interest_test_question_temp"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_test_id = Column(BigInteger, name="target_test_id", nullable=False)
    order = Column(BigInteger, name="order", nullable=True)
    question_title = Column(String, name="question_title", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)


class InterestTestRecord(Base):
    __tablename__ = "interest_test_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    target_test_id = Column(BigInteger, name="target_test_id", nullable=False)
    test_result = Column(String, name="test_result", nullable=True)
    test_result_image_url = Column(String, name="test_result_image_url", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class IpNation(Base):
    __tablename__ = "ip_nation"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    ip = Column(Integer, name="ip", default=0, nullable=False)
    country = Column(String, name="country", default='', nullable=False)


class IpNationCountries(Base):
    __tablename__ = "ip_nation_countries"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    code = Column(String, name="code", default='', nullable=False)
    iso_code_2 = Column(String, name="iso_code_2", default='', nullable=False)
    iso_code_3 = Column(String, name="iso_code_3", default='', nullable=True)
    iso_country = Column(String, name="iso_country", default='', nullable=False)
    country = Column(String, name="country", default='', nullable=False)
    country_cn = Column(String, name="country_cn", nullable=True)
    lat = Column(Float, name="lat", default=0, nullable=False)
    lon = Column(Float, name="lon", default=0, nullable=False)


class KeySearch(Base):
    __tablename__ = "key_search"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    name = Column(String, name="name", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class LabelQueueTag(Base):
    __tablename__ = "label_queue_tag"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    queue_id = Column(BigInteger, name="queue_id", nullable=True)
    tag_name = Column(String, name="tag_name", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    valid = Column(Integer, name="valid", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class LabelReviewPost(Base):
    __tablename__ = "label_review_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    post_state = Column(Integer, name="post_state", nullable=True)
    queue_code = Column(Integer, name="queue_code", nullable=True)
    pool_code = Column(Integer, name="pool_code", nullable=True)
    reason_labels = Column(String, name="reason_labels", nullable=True)
    all_labels = Column(String, name="all_labels", nullable=True)
    remark = Column(String, name="remark", nullable=True)
    post_handle_action = Column(SmallInteger, name="post_handle_action", default=-1, nullable=True)
    author_handle_action = Column(SmallInteger, name="author_handle_action", default=-1, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    watch_time = Column(DateTime, name="watch_time", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class LoginRecord(Base):
    __tablename__ = "login_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    success = Column(String, name="success", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    ip = Column(String, name="ip", default='', nullable=True)
    user_name = Column(String, name="user_name", nullable=False)


class LotteryInfo(Base):
    __tablename__ = "lottery_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    state = Column(Integer, name="state", default=0, nullable=True)
    source_type = Column(Integer, name="source_type", nullable=True)
    source_flag = Column(String, name="source_flag", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class LotteryRecord0(Base):
    __tablename__ = "lottery_record0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    prize_id = Column(BigInteger, name="prize_id", nullable=True)
    game_id = Column(Integer, name="game_id", nullable=True)
    result = Column(Integer, name="result", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class LuckyDrawRecord0(Base):
    __tablename__ = "lucky_draw_record0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    prize_id = Column(BigInteger, name="prize_id", nullable=True)
    result = Column(Integer, name="result", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class MakeGroup(Base):
    __tablename__ = "make_group"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    group_name = Column(String, name="group_name", nullable=True)
    group_color = Column(String, name="group_color", nullable=True)
    show_location = Column(String, name="show_location", nullable=True)
    show_page = Column(String, name="show_page", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class MakeInfo(Base):
    __tablename__ = "make_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    make_content = Column(String, name="make_content", nullable=True)
    group_id = Column(BigInteger, name="group_id", nullable=True)
    make_annotation = Column(String, name="make_annotation", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class MusicSensitiveWord(Base):
    __tablename__ = "music_sensitive_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=False)
    content = Column(String, name="content", nullable=False)
    valid = Column(Integer, name="valid", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class MusicSensitiveWordWhite(Base):
    __tablename__ = "music_sensitive_word_white"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=False)
    music_sensitive_id = Column(BigInteger, name="music_sensitive_id", nullable=False)
    content = Column(String, name="content", nullable=False)
    valid = Column(Integer, name="valid", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", nullable=True)


class NsCategory(Base):
    __tablename__ = "ns_category"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", nullable=True)


class NsWord(Base):
    __tablename__ = "ns_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    category_id = Column(BigInteger, name="category_id", nullable=True)
    word_type = Column(Integer, name="word_type", nullable=True)
    key_word = Column(String, name="key_word", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class OperLog(Base):
    __tablename__ = "oper_log"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    oper_id = Column(BigInteger, name="oper_id", nullable=True)
    oper_object = Column(Integer, name="oper_object", nullable=True)
    oper_object_id = Column(BigInteger, name="oper_object_id", nullable=True)
    oper_behavior = Column(String, name="oper_behavior", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class OperationFreshSquare(Base):
    __tablename__ = "operation_fresh_square"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    real_post_id = Column(BigInteger, name="real_post_id", nullable=True)
    influence = Column(BigInteger, name="influence", nullable=True)
    type = Column(String, name="type", nullable=True)


class OperationRecord(Base):
    __tablename__ = "operation_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    operator_id = Column(String, name="operator_id", nullable=True)
    operation_page = Column(String, name="operation_page", nullable=True)
    operation_event = Column(String, name="operation_event", nullable=True)
    operation_obj_id = Column(String, name="operation_obj_id", nullable=True)
    create_date = Column(DateTime, name="create_date", default=datetime.now(), nullable=False)
    update_date = Column(DateTime, name="update_date", default=datetime.now(), nullable=False)


class OperationRecordV2(Base):
    __tablename__ = "operation_record_v2"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    target_type = Column(Integer, name="target_type", nullable=False)
    target_id = Column(BigInteger, name="target_id", nullable=False)
    source = Column(Integer, name="source", nullable=False)
    action_type = Column(Integer, name="action_type", nullable=False)
    action_desc = Column(String, name="action_desc", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    page_obj_id = Column(BigInteger, name="page_obj_id", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", nullable=True)


class PageCategory(Base):
    __tablename__ = "page_category"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    page_name = Column(String, name="page_name", nullable=True)


class PayOperationRecord(Base):
    __tablename__ = "pay_operation_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    operation_type = Column(Integer, name="operation_type", nullable=True)
    operation_id = Column(BigInteger, name="operation_id", nullable=True)
    identity = Column(String, name="identity", nullable=True)
    before_operate = Column(String, name="before_operate", nullable=True)
    after_operate = Column(String, name="after_operate", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class PopupConfig(Base):
    __tablename__ = "popup_config"

    id = Column(Integer, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", default='', nullable=False)
    type = Column(Integer, name="type", default=1, nullable=False)
    priority = Column(Integer, name="priority", default=0, nullable=False)
    image_url = Column(String, name="image_url", default='', nullable=False)
    jump_url = Column(String, name="jump_url", default='', nullable=False)
    daily_count = Column(Integer, name="daily_count", default=0, nullable=False)
    sum_count = Column(Integer, name="sum_count", default=0, nullable=False)
    end_time = Column(DateTime, name="end_time", nullable=False)
    valid = Column(Integer, name="valid", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class PostAccess(Base):
    __tablename__ = "post_access"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    author_id = Column(BigInteger, name="author_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    content = Column(String, name="content", nullable=True)
    attachment = Column(String, name="attachment", nullable=True)
    access_status = Column(Integer, name="access_status", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class PostAdminHandleRecord(Base):
    __tablename__ = "post_admin_handle_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_pre_state = Column(Integer, name="post_pre_state", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    post_after_state = Column(Integer, name="post_after_state", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    create_by = Column(BigInteger, name="create_by", nullable=True)


class PostAutoHandleInfo(Base):
    __tablename__ = "post_auto_handle_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    post_pre_state = Column(Integer, name="post_pre_state", nullable=True)
    post_pre_handle_reason = Column(Integer, name="post_pre_handle_reason", nullable=True)
    post_pre_handle_remark = Column(String, name="post_pre_handle_remark", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    post_after_state = Column(Integer, name="post_after_state", nullable=True)
    post_handle_state = Column(Integer, name="post_handle_state", nullable=True)
    post_handle_admin = Column(BigInteger, name="post_handle_admin", nullable=True)
    post_handle_time = Column(DateTime, name="post_handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class PostDeleteRecord(Base):
    __tablename__ = "post_delete_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    author_id = Column(BigInteger, name="author_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class PostPattern(Base):
    __tablename__ = "post_pattern"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=True)
    level = Column(Integer, name="level", nullable=False)
    operation = Column(Integer, name="operation", default=0, nullable=True)
    expression = Column(String, name="expression", nullable=False)
    last_reviser_id = Column(BigInteger, name="last_reviser_id", nullable=False)
    status = Column(Integer, name="status", default=0, nullable=True)
    online_time = Column(DateTime, name="online_time", nullable=True)
    offline_time = Column(DateTime, name="offline_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class PostPatternRecord(Base):
    __tablename__ = "post_pattern_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    post_pattern_type = Column(Integer, name="post_pattern_type", nullable=True)
    post_pattern_id = Column(BigInteger, name="post_pattern_id", nullable=True)
    post_pattern_operation = Column(Integer, name="post_pattern_operation", default=0, nullable=True)
    post_pattern_expression = Column(String, name="post_pattern_expression", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class PostRecommendRecord(Base):
    __tablename__ = "post_recommend_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    author_id = Column(BigInteger, name="author_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    post_type = Column(Integer, name="post_type", nullable=True)
    content = Column(String, name="content", nullable=True)
    recommend_status = Column(Integer, name="recommend_status", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    queue = Column(Integer, name="queue", nullable=True)
    teenager_status = Column(Integer, name="teenager_status", nullable=True)
    all_admin_id = Column(BigInteger, name="all_admin_id", nullable=True)
    shell_admin_id = Column(BigInteger, name="shell_admin_id", nullable=True)
    cancel_admin_id = Column(BigInteger, name="cancel_admin_id", nullable=True)
    teen_admin_id = Column(BigInteger, name="teen_admin_id", nullable=True)


class PostRenew(Base):
    __tablename__ = "post_renew"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    state = Column(String, name="state", nullable=True)
    post_pv = Column(BigInteger, name="post_pv", nullable=True)
    post_weight = Column(Float, name="post_weight", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    content = Column(String, name="content", nullable=True)
    visibility = Column(String, name="visibility", nullable=True)
    tag_names = Column(String, name="tag_names", nullable=True)
    file_urls = Column(String, name="file_urls", nullable=True)
    comments = Column(BigInteger, name="comments", nullable=True)
    follows = Column(BigInteger, name="follows", nullable=True)
    likes = Column(BigInteger, name="likes", nullable=True)
    shares = Column(BigInteger, name="shares", nullable=True)
    author_id = Column(BigInteger, name="author_id", nullable=True)
    gender = Column(String, name="gender", nullable=True)
    user_state = Column(String, name="user_state", nullable=True)
    en_renew = Column(Integer, name="en_renew", default=0, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class PostReview(Base):
    __tablename__ = "post_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    post_state = Column(Integer, name="post_state", nullable=True)
    queue_code = Column(SmallInteger, name="queue_code", nullable=True)
    pool_code = Column(SmallInteger, name="pool_code", nullable=True)
    reason_labels = Column(String, name="reason_labels", nullable=True)
    all_labels = Column(String, name="all_labels", nullable=True)
    remark = Column(String, name="remark", nullable=True)
    post_handle_action = Column(SmallInteger, name="post_handle_action", default=-1, nullable=True)
    author_handle_action = Column(SmallInteger, name="author_handle_action", default=-1, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    watch_time = Column(DateTime, name="watch_time", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class PostReviewRecord(Base):
    __tablename__ = "post_review_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_author = Column(BigInteger, name="post_author", nullable=True)
    post_create_time = Column(DateTime, name="post_create_time", nullable=True)
    post_pre_handle_reason = Column(SmallInteger, name="post_pre_handle_reason", nullable=True)
    post_pre_handle_remark = Column(String, name="post_pre_handle_remark", nullable=True)
    review_type = Column(SmallInteger, name="review_type", nullable=True)
    review_pool = Column(SmallInteger, name="review_pool", nullable=True)
    post_handle_action = Column(SmallInteger, name="post_handle_action", default=999, nullable=True)
    author_handle_action = Column(SmallInteger, name="author_handle_action", default=999, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    create_by = Column(BigInteger, name="create_by", nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)
    modify_by = Column(BigInteger, name="modify_by", nullable=True)


class PostTopRecord(Base):
    __tablename__ = "post_top_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    author_id = Column(BigInteger, name="author_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    post_type = Column(Integer, name="post_type", nullable=True)
    content = Column(String, name="content", nullable=True)
    top_status = Column(Integer, name="top_status", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    top_time = Column(DateTime, name="top_time", nullable=True)
    queue = Column(Integer, name="queue", nullable=True)


class PraiseReview(Base):
    __tablename__ = "praise_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    target_user_id = Column(BigInteger, name="target_user_id", nullable=True)
    praise_content = Column(String, name="praise_content", nullable=True)
    nick_name = Column(String, name="nick_name", nullable=True)
    pool_code = Column(Integer, name="pool_code", default=1, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    praise_handle_action = Column(Integer, name="praise_handle_action", default=0, nullable=True)
    author_handle_action = Column(Integer, name="author_handle_action", default=0, nullable=True)
    handle_action = Column(Integer, name="handle_action", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    review_time = Column(DateTime, name="review_time", nullable=True)


class PremiumUser(Base):
    __tablename__ = "premium_user"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    source = Column(Integer, name="source", default=1, nullable=False)
    gender = Column(Integer, name="gender", default=0, nullable=False)
    phone_number = Column(String, name="phone_number", nullable=True)
    remark = Column(String, name="remark", nullable=True)
    valid = Column(Integer, name="valid", default=0, nullable=True)
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


class Prize0(Base):
    __tablename__ = "prize0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", nullable=True)
    state = Column(BigInteger, name="state", nullable=True)
    type = Column(BigInteger, name="type", nullable=True)
    commodity_id = Column(BigInteger, name="commodity_id", nullable=True)
    pic_url = Column(String, name="pic_url", nullable=True)
    group_id = Column(BigInteger, name="group_id", nullable=True)
    group_name = Column(String, name="group_name", nullable=True)
    everyday_num = Column(BigInteger, name="everyday_num", nullable=True)
    hit_ratio = Column(BigInteger, name="hit_ratio", nullable=True)
    result_desc = Column(String, name="result_desc", nullable=True)
    description = Column(String, name="description", nullable=True)
    redirect_url = Column(String, name="redirect_url", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    delete_time = Column(DateTime, name="delete_time", nullable=True)


class PrizeItem0(Base):
    __tablename__ = "prize_item0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    prize_id = Column(BigInteger, name="prize_id", nullable=True)
    prize_name = Column(String, name="prize_name", nullable=True)
    state = Column(Integer, name="state", nullable=True)
    prize_type = Column(Integer, name="prize_type", nullable=True)
    item_identity = Column(String, name="item_identity", nullable=True)
    pic_url = Column(String, name="pic_url", nullable=True)
    group_id = Column(BigInteger, name="group_id", nullable=True)
    group_name = Column(String, name="group_name", nullable=True)
    stock_limit = Column(BigInteger, name="stock_limit", nullable=True)
    hit_ratio = Column(Float, name="hit_ratio", default=0, nullable=True)
    result_desc = Column(String, name="result_desc", nullable=True)
    item_desc = Column(String, name="item_desc", nullable=True)
    redirect_url = Column(String, name="redirect_url", nullable=True)
    game_id = Column(Integer, name="game_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)
    prize_rules = Column(Integer, name="prize_rules", nullable=True)
    prize_data = Column(String, name="prize_data", nullable=True)
    result_url = Column(String, name="result_url", nullable=True)


class PushConfig(Base):
    __tablename__ = "push_config"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    push_group_name = Column(String, name="push_group_name", nullable=False)
    text = Column(String, name="text", nullable=False)
    text_type = Column(Integer, name="text_type", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)
    ops_admin = Column(String, name="ops_admin", default='', nullable=False)


class PushConfigHistory(Base):
    __tablename__ = "push_config_history"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    config_id = Column(BigInteger, name="config_id", nullable=True)
    push_group_name = Column(String, name="push_group_name", nullable=True)
    text = Column(String, name="text", nullable=True)
    text_type = Column(Integer, name="text_type", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    ops_admin = Column(String, name="ops_admin", default='', nullable=True)


class PushResourceConfig(Base):
    __tablename__ = "push_resource_config"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    resource_type = Column(Integer, name="resource_type", nullable=True)
    content = Column(String, name="content", nullable=True)
    link_url = Column(String, name="link_url", nullable=True)
    image_url = Column(String, name="image_url", nullable=True)
    main_title = Column(String, name="main_title", nullable=True)
    sub_title = Column(String, name="sub_title", nullable=True)
    state = Column(Integer, name="state", nullable=True)
    jump_type = Column(Integer, name="jump_type", nullable=True)
    jump_obj = Column(String, name="jump_obj", nullable=True)
    land_page = Column(Integer, name="land_page", nullable=True)
    push_people = Column(Integer, name="push_people", nullable=True)
    push_group = Column(String, name="push_group", nullable=True)
    push_time_type = Column(Integer, name="push_time_type", nullable=True)
    start_time = Column(DateTime, name="start_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class QueueLabelMapping(Base):
    __tablename__ = "queue_label_mapping"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    queue_id = Column(BigInteger, name="queue_id", nullable=True)
    first_label = Column(String, name="first_label", nullable=True)
    second_label = Column(String, name="second_label", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    valid = Column(Integer, name="valid", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class QuickRet(Base):
    __tablename__ = "quick_ret"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    content = Column(String, name="content", nullable=True)


class RandomAudio(Base):
    __tablename__ = "random_audio"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    author_id = Column(BigInteger, name="author_id", nullable=False)
    content = Column(String, name="content", nullable=True)
    admin_user_id = Column(BigInteger, name="admin_user_id", nullable=True)
    kind = Column(String, name="kind", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    resource_type = Column(Integer, name="resource_type", default=1, nullable=True)
    can_use = Column(Integer, name="can_use", default=1, nullable=True)
    state = Column(Integer, name="state", nullable=True)
    source = Column(Integer, name="source", default=1, nullable=False)


class RandomAudioKind(Base):
    __tablename__ = "random_audio_kind"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    kind_id = Column(BigInteger, name="kind_id", nullable=False)


class RandomKind(Base):
    __tablename__ = "random_kind"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    kind_name = Column(String, name="kind_name", nullable=False)
    state = Column(Integer, name="state", nullable=False)
    online_time = Column(DateTime, name="online_time", nullable=True)
    admin_user_id = Column(BigInteger, name="admin_user_id", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class RecommendHistory(Base):
    __tablename__ = "recommend_history"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    author_id = Column(BigInteger, name="author_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    rec_source = Column(Integer, name="rec_source", nullable=True)
    rec_type = Column(Integer, name="rec_type", nullable=True)
    rec_all = Column(Integer, name="rec_all", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    post_time = Column(DateTime, name="post_time", nullable=True)
    type = Column(Integer, name="type", nullable=True)
    recall_source = Column(Integer, name="recall_source", nullable=True)
    review_state = Column(Integer, name="review_state", default=1, nullable=True)


class ReviewDistribute(Base):
    __tablename__ = "review_distribute"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    page = Column(String, name="page", nullable=True)
    result = Column(String, name="result", nullable=True)
    trigger_content = Column(String, name="trigger_content", nullable=True)
    trigger_detail = Column(String, name="trigger_detail", nullable=True)
    pull_time = Column(DateTime, name="pull_time", nullable=True)
    enter_time = Column(DateTime, name="enter_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class ReviewPoolConfig(Base):
    __tablename__ = "review_pool_config"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    review_content = Column(SmallInteger, name="review_content", nullable=True)
    review_type = Column(SmallInteger, name="review_type", nullable=True)
    pool_code = Column(Integer, name="pool_code", nullable=True)
    pool_name = Column(String, name="pool_name", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=False)


class ReviewRecord(Base):
    __tablename__ = "review_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    page_source = Column(String, name="page_source", nullable=True)
    page_detail = Column(String, name="page_detail", nullable=True)
    record_id = Column(BigInteger, name="record_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    oper_action = Column(String, name="oper_action", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class ReviewSync(Base):
    __tablename__ = "review_sync"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    review_type = Column(String, name="review_type", nullable=True)
    content = Column(String, name="content", nullable=True)
    file_urls = Column(String, name="file_urls", nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    sync_time = Column(DateTime, name="sync_time", nullable=True)
    review_distribute_id = Column(BigInteger, name="review_distribute_id", nullable=True)


class ReviewUserInfo(Base):
    __tablename__ = "review_user_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    target_id = Column(BigInteger, name="target_id", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    page = Column(String, name="page", nullable=True)
    pool_code = Column(Integer, name="pool_code", nullable=True)
    state = Column(String, name="state", nullable=True)
    content = Column(String, name="content", nullable=True)
    action = Column(String, name="action", nullable=True)
    handle_time = Column(DateTime, name="handle_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)


class RoomMapping(Base):
    __tablename__ = "room_mapping"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    room = Column(String, name="room", nullable=True)
    type = Column(String, name="type", nullable=True)


class RoomNameReview(Base):
    __tablename__ = "room_name_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    room_id = Column(BigInteger, name="room_id", nullable=False)
    room_name = Column(String, name="room_name", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    room_handle = Column(Integer, name="room_handle", default=999, nullable=True)
    user_handle = Column(Integer, name="user_handle", default=999, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class SceneCommodity(Base):
    __tablename__ = "scene_commodity"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    scene_id = Column(BigInteger, name="scene_id", nullable=False)
    first_category = Column(String, name="first_category", nullable=False)
    item_identity = Column(String, name="item_identity", nullable=False)
    validation = Column(Integer, name="validation", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class SearchWhite(Base):
    __tablename__ = "search_white"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    white_word = Column(String, name="white_word", nullable=True)
    if_teenager_view = Column(Integer, name="if_teenager_view", nullable=True)
    status = Column(Integer, name="status", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)


class SensitiveUser(Base):
    __tablename__ = "sensitive_user"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False)
    phone = Column(String, name="phone", nullable=True)
    signature = Column(String, name="signature", nullable=True)
    make = Column(String, name="make", nullable=True)
    sensitive_source = Column(Integer, name="sensitive_source", nullable=True)
    sensitive_end_time = Column(DateTime, name="sensitive_end_time", nullable=True)
    sensitive_times = Column(Integer, name="sensitive_times", default=0, nullable=True)
    is_sensitive = Column(Integer, name="is_sensitive", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class SensitiveWord(Base):
    __tablename__ = "sensitive_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=True)
    content = Column(String, name="content", nullable=True)
    level = Column(Integer, name="level", nullable=True)
    pinyin_match_level = Column(Integer, name="pinyin_match_level", default=0, nullable=True)
    remark = Column(String, name="remark", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class SensitiveWordPost(Base):
    __tablename__ = "sensitive_word_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=True)
    post_content = Column(String, name="post_content", nullable=True)
    post_state = Column(Integer, name="post_state", nullable=True)
    post_time = Column(DateTime, name="post_time", nullable=True)
    sensitive_word_type = Column(Integer, name="sensitive_word_type", nullable=True)
    sensitive_word_content = Column(String, name="sensitive_word_content", nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", nullable=True)


class SensitiveWordWhite(Base):
    __tablename__ = "sensitive_word_white"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    sensitive_word_id = Column(BigInteger, name="sensitive_word_id", nullable=True)
    content = Column(String, name="content", nullable=True)


class SpecialWord(Base):
    __tablename__ = "special_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=True)
    content = Column(String, name="content", nullable=True)
    remark = Column(String, name="remark", nullable=True)


class SpecialWordRecord(Base):
    __tablename__ = "special_word_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    target_user_id = Column(BigInteger, name="target_user_id", nullable=False)
    special_word = Column(String, name="special_word", nullable=False)
    content = Column(String, name="content", nullable=False)
    state = Column(String, name="state", default='unreviewed', nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    admin_action = Column(String, name="admin_action", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=False)
    review_time = Column(DateTime, name="review_time", nullable=True)


class SpecialWordReview(Base):
    __tablename__ = "special_word_review"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(String, name="user_id", nullable=True)
    registe_days = Column(String, name="registe_days", nullable=True)
    user_state = Column(String, name="user_state", nullable=True)
    post_nums = Column(Integer, name="post_nums", nullable=True)
    follow_nums = Column(Integer, name="follow_nums", nullable=True)
    mobile = Column(String, name="mobile", nullable=True)
    target_user_id = Column(String, name="target_user_id", nullable=True)
    content = Column(String, name="content", nullable=False)
    special_word = Column(String, name="special_word", nullable=True)
    special_word_type = Column(Integer, name="special_word_type", nullable=True)
    state = Column(Integer, name="state", default=1, nullable=True)
    admin_id = Column(String, name="admin_id", nullable=True)
    admin_action = Column(String, name="admin_action", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    review_time = Column(DateTime, name="review_time", default=datetime.now(), nullable=False)


class SuperVipUpdateLog(Base):
    __tablename__ = "super_vip_update_log"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    order_no = Column(String, name="order_no", nullable=True)
    old_end_time = Column(DateTime, name="old_end_time", nullable=True)
    begin_time = Column(DateTime, name="begin_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    valid = Column(Integer, name="valid", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", nullable=False)


class SysPermission(Base):
    __tablename__ = "sys_permission"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", nullable=False)
    resource_type = Column(Integer, name="resource_type", nullable=True)
    url = Column(String, name="url", nullable=True)
    permission = Column(String, name="permission", nullable=True)
    parentid = Column(BigInteger, name="parentid", nullable=True)
    parentids = Column(String, name="parentids", nullable=True)
    available = Column(Integer, name="available", default=0, nullable=True)


class SysRole(Base):
    __tablename__ = "sys_role"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    role = Column(String, name="role", nullable=True)
    description = Column(String, name="description", nullable=True)
    available = Column(Integer, name="available", default=0, nullable=True)


class SysRolePermission(Base):
    __tablename__ = "sys_role_permission"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    permission_id = Column(BigInteger, name="permission_id", nullable=False)
    role_id = Column(BigInteger, name="role_id", nullable=False)


class SysUserRole(Base):
    __tablename__ = "sys_user_role"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    role_id = Column(BigInteger, name="role_id", nullable=False)


class SystemFriendlyRecord(Base):
    __tablename__ = "system_friendly_record"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    operation_type = Column(Integer, name="operation_type", nullable=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    operation_strategy = Column(String, name="operation_strategy", nullable=True)
    operation_result = Column(String, name="operation_result", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class TblAdminAction(Base):
    __tablename__ = "tbl_admin_action"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    action = Column(String, name="action", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    target_type = Column(String, name="target_type", nullable=True)
    target_id = Column(BigInteger, name="target_id", nullable=True)


class TrafficReviewPost(Base):
    __tablename__ = "traffic_review_post"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(BigInteger, name="post_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    post_pv = Column(BigInteger, name="post_pv", nullable=True)
    weight = Column(Float, name="weight", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    review_time = Column(DateTime, name="review_time", default=datetime.now(), nullable=True)


class UgcQueueConfig(Base):
    __tablename__ = "ugc_queue_config"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    queue_id = Column(Integer, name="queue_id", nullable=True)
    key_word = Column(String, name="key_word", nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)


class UgcWord(Base):
    __tablename__ = "ugc_word"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    type = Column(Integer, name="type", nullable=True)
    content = Column(String, name="content", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class UnblockAppeal(Base):
    __tablename__ = "unblock_appeal"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=True)
    reason = Column(String, name="reason", nullable=True)
    state = Column(SmallInteger, name="state", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    modify_time = Column(DateTime, name="modify_time", default=datetime.now(), nullable=True)
    appeal_type = Column(Integer, name="appeal_type", default=0, nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)


class UnblockAppealAttachment(Base):
    __tablename__ = "unblock_appeal_attachment"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    owner_id = Column(BigInteger, name="owner_id", nullable=True)
    type = Column(SmallInteger, name="type", nullable=True)
    url = Column(String, name="url", nullable=True)
    order = Column(SmallInteger, name="order", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)


class UserBannedLog(Base):
    __tablename__ = "user_banned_log"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    reason = Column(String, name="reason", nullable=True)
    del_flag = Column(Integer, name="del_flag", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    ban_source = Column(Integer, name="ban_source", default=1, nullable=True)


class UserCoinCommodityTimes(Base):
    __tablename__ = "user_coin_commodity_times"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", default=0, nullable=False)
    info = Column(Text, name="info", nullable=False)
    is_valid = Column(Integer, name="is_valid", default=0, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class UserFriendlyLog(Base):
    __tablename__ = "user_friendly_log"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    admin_id = Column(BigInteger, name="admin_id", nullable=False)
    reason = Column(String, name="reason", nullable=True)
    action = Column(String, name="action", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    friendly_source = Column(Integer, name="friendly_source", default=1, nullable=True)


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, name="name", nullable=True)
    password = Column(String, name="password", nullable=False)
    state = Column(Integer, name="state", default=0, nullable=False)
    user_name = Column(String, name="user_name", nullable=False)
    salt = Column(String, name="salt", nullable=True)
    phone = Column(String, name="phone", nullable=False)
    email = Column(String, name="email", nullable=False)
    create_time = Column(DateTime, name="create_time", nullable=True)
    update_time = Column(DateTime, name="update_time", nullable=True)
    operate_user = Column(BigInteger, name="operate_user", nullable=True)


class UserPackageCommodityUseInfo(Base):
    __tablename__ = "user_package_commodity_use_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", default=0, nullable=False)
    package_use_detail = Column(String, name="package_use_detail", default='', nullable=False)
    package_item_identity = Column(String, name="package_item_identity", default='', nullable=False)
    package_item_name = Column(String, name="package_item_name", default='', nullable=False)
    period_start = Column(DateTime, name="period_start", default=datetime.now(), nullable=False)
    period_end = Column(DateTime, name="period_end", default=datetime.now(), nullable=False)
    source_info = Column(String, name="source_info", default='', nullable=False)
    expired = Column(Integer, name="expired", default=0, nullable=False)
    valid = Column(Integer, name="valid", default=1, nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class UserPrivilegePkgRelation(Base):
    __tablename__ = "user_privilege_pkg_relation"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    privilege_package_identity = Column(String, name="privilege_package_identity", nullable=False)
    state = Column(Integer, name="state", nullable=True)
    begin_time = Column(DateTime, name="begin_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", nullable=True)


class UserSummary(Base):
    __tablename__ = "user_summary"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    spec_act_day_byte = Column(String, name="spec_act_day_byte", nullable=True)
    act_days = Column(Integer, name="act_days", nullable=True)
    act_max_time = Column(BigInteger, name="act_max_time", nullable=True)
    last_time = Column(DateTime, name="last_time", nullable=True)
    last_dau = Column(Integer, name="last_dau", nullable=True)
    access_hp_users = Column(Integer, name="access_hp_users", nullable=True)
    access_hp_max_user_id = Column(BigInteger, name="access_hp_max_user_id", nullable=True)
    access_laster_night_cnt = Column(Integer, name="access_laster_night_cnt", nullable=True)
    act_max_time_day = Column(DateTime, name="act_max_time_day", nullable=True)
    post_cnt = Column(Integer, name="post_cnt", nullable=True)
    get_like_cnt = Column(Integer, name="get_like_cnt", nullable=True)
    get_comment_cnt = Column(Integer, name="get_comment_cnt", nullable=True)
    follow_users = Column(Integer, name="follow_users", nullable=True)
    follow_users_nochat = Column(Integer, name="follow_users_nochat", nullable=True)
    access_hp_tuser_id = Column(BigInteger, name="access_hp_tuser_id", nullable=True)
    access_time_range = Column(Integer, name="access_time_range", nullable=True)
    access_hp_tuser_cnt = Column(Integer, name="access_hp_tuser_cnt", nullable=True)
    friend_cnt = Column(Integer, name="friend_cnt", nullable=True)
    chat_max_user_id = Column(BigInteger, name="chat_max_user_id", nullable=True)
    chat_max_remark1 = Column(BigInteger, name="chat_max_remark1", nullable=True)
    chat_max_remark2 = Column(BigInteger, name="chat_max_remark2", nullable=True)
    chat_max_remark3 = Column(BigInteger, name="chat_max_remark3", nullable=True)
    new_chated_cnt = Column(Integer, name="new_chated_cnt", nullable=True)
    unchat_user_id = Column(BigInteger, name="unchat_user_id", nullable=True)
    unchat_user_day = Column(DateTime, name="unchat_user_day", nullable=True)
    min_time = Column(DateTime, name="min_time", nullable=True)
    first_like_day = Column(DateTime, name="first_like_day", nullable=True)
    first_like_uid = Column(BigInteger, name="first_like_uid", nullable=True)
    first_gift_day = Column(DateTime, name="first_gift_day", nullable=True)
    first_gift_uid = Column(BigInteger, name="first_gift_uid", nullable=True)
    first_post_day = Column(DateTime, name="first_post_day", nullable=True)
    first_chat_day = Column(DateTime, name="first_chat_day", nullable=True)
    first_chat_uid = Column(BigInteger, name="first_chat_uid", nullable=True)
    bak_1 = Column(String, name="bak_1", nullable=True)
    bak_2 = Column(String, name="bak_2", nullable=True)
    bak_3 = Column(String, name="bak_3", nullable=True)
    bak_4 = Column(String, name="bak_4", nullable=True)
    valid = Column(Integer, name="valid", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class VoiceGameMeta0(Base):
    __tablename__ = "voice_game_meta0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    pic_url = Column(String, name="pic_url", nullable=True)
    pic_lines = Column(String, name="pic_lines", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class VoiceGameRecord0(Base):
    __tablename__ = "voice_game_record0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", nullable=False)
    tone_desc = Column(String, name="tone_desc", nullable=True)
    tone_appraise = Column(String, name="tone_appraise", nullable=True)
    tone_fortune = Column(String, name="tone_fortune", nullable=True)
    audit_status = Column(Integer, name="audit_status", default=0, nullable=True)
    voice_url = Column(String, name="voice_url", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)
    voice_duration = Column(Integer, name="voice_duration", nullable=True)
    admin_id = Column(BigInteger, name="admin_id", nullable=True)
    pic_url = Column(String, name="pic_url", nullable=True)
    pic_lines = Column(String, name="pic_lines", nullable=True)


class VoiceGameToneFortune0(Base):
    __tablename__ = "voice_game_tone_fortune0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    desc = Column(String, name="desc", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class VoiceGameToneMeta0(Base):
    __tablename__ = "voice_game_tone_meta0"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    origin_tone = Column(String, name="origin_tone", nullable=True)
    primary_tone = Column(String, name="primary_tone", nullable=True)
    first_tone = Column(String, name="first_tone", nullable=True)
    second_tone = Column(String, name="second_tone", nullable=True)
    third_tone = Column(String, name="third_tone", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=True)
    valid = Column(Integer, name="valid", default=1, nullable=True)


class WechatQrcode(Base):
    __tablename__ = "wechat_qrcode"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    image_url = Column(String, name="image_url", nullable=True)
    query_string = Column(String, name="query_string", nullable=True)
    sha1 = Column(String, name="sha1", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
