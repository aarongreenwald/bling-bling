from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

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


@view_config(route_name='home', renderer='templates/bling.pt')
def my_view(request):
	return { 'project': 'bling-bling'}

@view_config(route_name='clients', renderer='json')
def clients(request):
    return DBSession.query(Client).all()    
    
@view_config(route_name='tasks', renderer='json')
def tasks(request):
    return DBSession.query(Task).all()
        
@view_config(route_name='worklogs', renderer='json')
def worklogs(request):    
    return DBSession.query(Worklog).all()
    
