from _ast import For
from tokenize import String

from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


class DB:
    _engine = create_engine('mysql+pymysql://admin:1234@localhost/test_setstatus')
    _base = declarative_base()

    def __init__(self):
        self.session_maker = sessionmaker(bind=self._engine)
        self.session = None

    def create_session(self):
        self.session = self.session_maker()

    def create_all_table(self):
        self._base.metadata.create_all(self._engine)

    class SubClass:
        id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    class Lesson(SubClass, _base):
        __tablename__ = 'lesson'
        lesson_name = Column('lesson_name',String(50))
        class_l = relationship('class_', backref='study')

    class Professor(SubClass, _base):
        __tablename__ = 'professor'
        firstname=Column('fist_name', String(50))
        lastname=Column('lastname', String(50))
        class_p = relationship('class_', backref='master')
        # professor_id_pct = relationship('Proffesor_class_time',backref='P_time_id')

    class class_(SubClass, _base):

        __tablename__ = 'class_'
        status_count = Column('status_count', Integer)
        professor_id = Column('professor_id', Integer, ForeignKey('professor.id'))
        lesson_id = Column('lesson_id', Integer, ForeignKey('lesson.id'))
        class_time_id = relationship('class_time', backref='c_time_id')

    class class_time(SubClass, _base):

        __tablename__ ='class_time'
        time = Column('time', String(50))
        date = Column('date', String(50))
        class_id_ = Column('class_id',Integer,ForeignKey('class_.id'))
        class_time_id_cti = relationship('Proffesor_class_time',backref='c_time_id')

    class Proffesor_class_time(SubClass, _base):
        __tablename__ = 'professor_class_time'
        professor_id_pct = Column('professor_id', Integer, ForeignKey('professor.id'))
        # lesson_id_pct = Column('lesson_id' , Integer, ForeignKey('lesson.id'))
        class_time_id = Column('class_time_id', Integer, ForeignKey('class_time.id'))


# if __name__ == '__main__':
# #     pass
#
#     db = DB()
#     db.create_all_table()
#     db.create_session()
#     lesson_1=db.Lesson(lesson_name='algoritm')
#     db.session.add(lesson_1)
#     db.session.commit()

#     professor_1 = db.Professor(firstname='reza', lastname='ramezani')
#     db.session.add(professor_1)
#     db.session.commit()
#     lesson_ = db.session.query(db.Lesson).one()
#     class_1 = db.class_(status_count=2, study=lesson_, master=professor_1)
#     db.session.add(class_1)
#     db.session.commit()
# #     print(class_1)
