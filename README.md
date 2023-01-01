
# dataclasses-dynamodb

A databclasses Dynamo db extension

Inspired by dataclasses, dataclasses-json & fastclasses-json the idea is to have a simple abstraction from dataclasses to dynamodb.

In searching for something that already did this I found dataclassesdynamodb which is very simple but does the job. I wanted something that could easily be integrated with an api wsgi server that have already encoded the payload as a dictionary.

Here is how I envisage it would work:

    db = dataclasses-dynamodb.Dynamo(table='mytable')
    db.create()

    @dataclasses-dynaomdb(db)
    @fastclaseses-json  # or @dataclasses-json
    @dataclasses
    class Person():
        name: str
        children: Optional[List[Person]] = None

    me = Person.from_dict({'name': 'Ian'}).put()
    me_from_dynamodb = Person.get(me.index())

    people = Person.list()
