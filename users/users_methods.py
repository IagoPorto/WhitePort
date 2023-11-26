from flask import request

app = Flask(__name)

@app.route('/whiteport', methods=['GET', 'POST'])



def postUserCredentials(username, password):
    try:
        response, status_code = insert_user_credentials(username, password)

        return response, status_code
    except Exception as e:
        return str(e), 500


def validate_login(username, password):
    if username in db_users and db_users[username] == password:
        return True
    else:
        return False

def login():
    try:
        username = request.form.get("username")
        password = request.form.get("password")

        if validate_login(username, password):
            return "Usuario incorrecto", 200
        else:
            return "Usuario correcto", 401

    except Exception as e:
        return str(e), 500

def delete_user():
    try:
        username_to_delete = request.form.get("username")

        if username_to_delete in db_users:
            del db_users[username_to_delete]
            return f"Usuario eliminado", 200
        else:
            return f"Usuario no encontrado", 404

    except Exception as e:
        return str(e), 500