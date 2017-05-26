#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""using postgresql"""
from datetime import datetime

from ..manage import db


class User(db.Model):
    """user表"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), primary_key=True, unique=True)
    email = db.Column(db.String, primary_key=True, unique=True)
    password = db.Column(db.String)
    invitation = db.Column(db.String, unique=True)
    code = db.Column(db.String)
    permission = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def verify_password(self, password):
        return self.password == password


class Post(db.Model):
    """文章表"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=True, unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.Column(db.Text)


class InviteCode(db.Model):
    """邀请码单设一个表"""

    __tablename__ = "invitecode"

    id = db.Column(db.Integer, primary_key=True)
    invitation = db.Column(db.String, primary_key=True, unique=True)
