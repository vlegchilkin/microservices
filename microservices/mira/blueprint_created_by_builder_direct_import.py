from flask import Blueprint


def builder() -> Blueprint:
    return Blueprint(
        name='blueprint_direct_import',
        import_name=__name__,
        url_prefix='/blueprint_direct_import'
    )


direct_import_blueprint = builder()


@direct_import_blueprint.route('/route_method')
def route_method():
    return {'response': 'route method (GET / HEAD / OPTIONS)'}


@direct_import_blueprint.get('/get_method')
def get_method():
    return {'response': 'GET method'}


@direct_import_blueprint.post('/post_method')
def post_method():
    return {'response': 'POST method'}


@direct_import_blueprint.put('/put_method')
def put_method():
    return {'response': 'PUT method'}


@direct_import_blueprint.delete('/delete_method')
def delete_method():
    return {'response': 'DELETE method'}


@direct_import_blueprint.patch('/patch_method')
def patch_method():
    return {'response': 'PATCH method'}
