from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserModel(Base):

    __tablename__ = "users"

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    hashed_password = sa.Column(sa.String)

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow)


class PageModel(Base):

    __tablename__ = "pages"

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    page_url = sa.Column(sa.String(128))
    task_id = sa.Column(sa.String(36))

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow)


class ProductModel(Base):

    __tablename__ = "products"

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)

    name = sa.Column(sa.String(256))
    price = sa.Column(sa.String(128))
    state = sa.Column(sa.String(128))
    location = sa.Column(sa.String(256))
    image_src = sa.Column(sa.String(512))
    product_url = sa.Column(sa.String(512))

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow)

    page_id = sa.Column(sa.Integer(), sa.ForeignKey('pages.id'))
