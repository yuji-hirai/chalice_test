from chalice import Chalice
from chalicelib.reservation import dispatch
from chalicelib.cancel import cancel_for_user
app = Chalice(app_name='chalice_test')

@app.lambda_function(name='reservation')
def reservation(event, context):
    return dispatch(event)

@app.lambda_function(name='cancel')
def cancel(event, context):
    return cancel_for_user(event)
