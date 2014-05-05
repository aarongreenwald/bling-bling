from sqlalchemy import *

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True)
    name = Column('name', VARCHAR(length = 50), nullable=False)
    code = Column('code', VARCHAR(length = 8), nullable=False)
    
class Task(Base):
    __tablename__ = 'task'
    task_id = Column('task_id', Integer(), primary_key = True, nullable=False)
    client_id = Column('client_id', Integer(), ForeignKey('client.client_id'), nullable=False)
    name = Column('name', VARCHAR(50), nullable=False)
    note = Column('note', TEXT(), nullable=True)
    estimated_time = Column('estimated_time', NUMERIC(precision=12, scale=2), nullable=False)
    invoice_amount = Column('invoice_amount', NUMERIC(precision=19, scale=4), nullable=False)
    approved_date = Column('approved_date', DATE(), nullable=True)
    completed_date = Column('completed_date', DATE(), nullable=True)
    paid_date = Column('paid_date', DATE(), nullable=True)  
    paid_amount = Column('paid_amount', NUMERIC(precision=19, scale=4), nullable=False)
    write_off_amount = Column('write_off_amount', NUMERIC(precision=19, scale=4), nullable=False)
    closed_date = Column('closed_date', DATE(), nullable=True)
                
class Worklog(Base):
    __tablename__ = 'worklog'
    worklog_id = Column('worklog_id', Integer(), primary_key = True, nullable=False)
    work_date = Column('work_date', DATE(), nullable=True)     
    task_id = Column('task_id', Integer(), ForeignKey('task.task_id'), nullable=False)
    time_spent = Column('time_spent', NUMERIC(precision=12, scale=2), nullable=False)    
    note = Column('note', TEXT(), nullable=True)
    is_billable = Column('is_billable', BOOLEAN(), nullable=False)
        
    
