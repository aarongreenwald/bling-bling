from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import forbidden_view_config
from pyramid.view import notfound_view_config

import pyramid

from .models import (
    DBSession,
    Client,
    Task,
    Worklog,    
    )


def format(obj):    
    if isinstance(obj, datetime.date):
        return str(obj)
    elif isinstance(obj, numbers.Number):
        return str(obj) 
    else:
        return obj

def serialize(result_set):          
    if not isinstance(result_set, list):
        result = {c.name: format(getattr(result_set, c.name)) for c in result_set.__table__.columns}
    else:
        result = []
        for row in result_set:
            serialized = {c.name: format(getattr(row, c.name)) for c in row.__table__.columns}
            result.append(serialized)
    return result

@view_config(route_name='clients', renderer='json')
def clients(request):
    return DBSession.query(Client).all()    
    
@view_config(route_name='tasks', renderer='json')
def tasks(request):
    return DBSession.query(Task).all()
        
@view_config(route_name='worklogs', renderer='json')
def worklogs(request):    
    return DBSession.query(Worklog).all()
    
@view_config(route_name='worklog', request_method='POST', renderer='json')
def post_worklog(request):    
    data = request.json_body['worklog']
    worklog = Worklog()
    
    worklog.note = data['note']
    worklog.time_spent = data['timeSpent']
    worklog.task_id = data['taskId']
    worklog.work_date = data['workDate']
    worklog.is_billable = data['isBillable']
    
    DBSession.add(worklog)
    
    return True

@view_config(route_name='worklog', request_method='GET', renderer='json')
def get_worklog(request):    
    return 'Hello World'
            
@notfound_view_config()
def notfound(request):
    return Response('NOT FOUND!', status='404 Not Found')    
    
