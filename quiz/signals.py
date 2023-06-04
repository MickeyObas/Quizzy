from django import dispatch

quiz_completed = dispatch.Signal(providing_args=['quiz_id', 'user'])

