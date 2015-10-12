### run site ###
python index.py runserver -h 0.0.0.0 -p 3001 -r

### database ###
db.drop_all()
db.create_all()

admin_role=Role(name='Admin')
mod_role=Role(name='Moderator')
user_role=Role(name='User')

user_john=User(username='john',role=admin_role)
user_susan=User(username='susan',role=user_role)
user_david=User(username='david',role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

db.session.commit()

print admin_role.id
print mod_role.id
print user_role.id

admin_role.name="Jenkingwong"
db.session.add(admin_role)
db.session.commit()

db.session.delete(mod_role)
db.session.commit()

trace( Role.query.all() )
trace( User.query.filter_by(role=user_role).all() )

res=user_role.users.order_by(User.username).all()
trace(res)
trace(user_role.users.count())
