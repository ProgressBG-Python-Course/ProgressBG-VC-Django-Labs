#!/usr/bin/env python

from cgi import parse_qs, escape

html = """
<html>
<body>
    <h1>Your data:</h1>
    <p>
        Age: %(age)s<br>
        Hobbies: %(hobbies)s
    </p>
</body>
</html>
"""

def application (environ, start_response):
    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    age = d.get('age', [''])[0]
    hobbies = d.get('hobbies', [])

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % {
        'checked-software': ('', 'checked')['software' in hobbies],
        'checked-tunning': ('', 'checked')['tunning' in hobbies],
        'age': age or 'Empty',
        'hobbies': ', '.join(hobbies or ['No Hobbies?'])
    }

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]