from sqlalchemy import text

def send_subscribe_mail(subject, email, name):
    query = text("SELECT * FROM users WHERE name = :name")
    result = db.engine.execute(query, name=name)
    # ...