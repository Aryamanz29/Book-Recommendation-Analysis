@app.route('/home')
@login_required
def home():
    return "<h1>" + current_user.username + "'s Home</h1>"

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registeredUser = users_repository.get_user(username)
        print('Users '+ str(users_repository.users))
        print('Register user %s , password %s' % (registeredUser.username, registeredUser.password))
        if registeredUser != None and registeredUser.password == password:
            print('Logged in..')
            login_user(registeredUser)
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
        return Response('''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        ''')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username , password , users_repository.next_index())
        users_repository.save_user(new_user)
        return Response("Registered Successfully")
    else:
        return Response('''
            <form action="" method="post">
            <p><input type=text name=username placeholder="Enter username">
            <p><input type=password name=password placeholder="Enter password">
            <p><input type=submit value=Login>
            </form>
        ''')