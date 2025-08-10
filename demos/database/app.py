body = form.body.data
note = Note(body=text("'%s'" % body))
db.session.add(note)
db.session.commit()