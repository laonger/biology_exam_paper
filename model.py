#!/usr/bin/python
# encoding: utf-8

import sha

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased

from sqlalchemy import Column, String, Integer
from sqlalchemy import select

from sqlalchemy import and_


Base = declarative_base()
engine = create_engine('sqlite:///data/a.db')
session = sessionmaker()
session.configure(bind=engine)

class ModelBase(object):
    """# ModelBase: docstring"""


    @classmethod
    def in_(cls, attr_name, value_list):
        s = session()
        l = s.query(cls).filter(getattr(cls, attr_name).in_(value_list))
        return l

    @classmethod
    def and_in_(cls, attr_name_1, value_list_1, attr_name_2, value_list_2):
        s = session()
        l = s.query(cls).filter(and_(getattr(cls, attr_name_1).in_(value_list_1), getattr(cls, attr_name_2).in_(value_list_2)))
        return l


    @classmethod
    def delete(cls, id):
        s = session()
        n = s.query(cls).get(id)
        s.delete(n)
        s.commit()

    @classmethod
    def new(cls, timu, peitu, daan, xueqi, nandu):
        """# new: docstring """
        n = cls()
        n.timu = timu
        n.peitu = peitu if peitu else ''
        n.daan = daan
        n.xueqi = xueqi
        n.nandu = nandu

        n.id = sha.new(''.join([
            n.timu.encode('utf-8'),
            n.peitu.encode('utf-8'),
            n.daan.encode('utf-8'),
            str(n.xueqi),
            str(n.nandu),
        ])).hexdigest()
        s = session()
        s.add(n)
        s.commit()
        return n

    @classmethod
    def list_all(cls, ):
        s = session()
        all = s.execute(select([
            cls.id,
            cls.timu,
            cls.peitu,
            cls.daan,
            cls.xueqi,
            cls.nandu,
        ]))
        return all


class Xuanzeti(Base, ModelBase):
    """# Xuanzeti: 选择题储存表"""
    __tablename__ = "xuanzeti"
    id = Column(String, primary_key=True)
    timu = Column(String)
    peitu = Column(String)
    daan = Column(String)
    xueqi = Column(String)
    nandu = Column(Integer)


class Tiankongti(Base, ModelBase):
    """# Tiankongti: 填空题储存表"""
    __tablename__ = "tiankongti"
    id = Column(String, primary_key=True)
    timu = Column(String)
    peitu = Column(String)
    daan = Column(String)
    xueqi = Column(String)
    nandu = Column(Integer)




Base.metadata.create_all(engine)
