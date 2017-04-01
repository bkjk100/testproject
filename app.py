from flask import Flask, render_template, request, json 
from flaskext.mysql import MySQL

mysql = MySQL()
app=Flask(__name__)
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'bkelley'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tombrady'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'ec2-34-223-242-146.us-west-2.compute.amazonaws.com'
mysql.init_app(app)

@app.route("/")
#def main():
#	cr = mysql.get_db()
#	cursor=cr.cursor()
#	add_usr = "INSERT INTO username (username) VALUES (%s)"
#	data_usr="bke"
#	t="INSERT INTO username (username) VALUES ('bk')"
#	cursor.execute(add_usr,data_usr)
#	cr.commit()
#	cursor.close();
#	return "b"

def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        print(_name)
        # validate the received values
        if _name:
            
            # All Good, let's call MySQL
            print('here')
            conn = mysql.get_db()
            cursor = conn.cursor()
            add_usr = "INSERT INTO username (username) VALUES (%s)"
	    data_usr="bke"
            #t="INSERT INTO username (username) VALUES ('bk')"
            #cursor.execute(add_usr,data_usr)
	    # cr.commit()
            cursor.execute(add_usr,_name);
	  #  conn.commit()
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 

if __name__=="__main__":
	app.run();


