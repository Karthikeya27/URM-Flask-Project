from sqlalchemy import create_engine,text

connection_string = "mysql+mysqlconnector://5nechykp9juilt651e90:pscale_pw_ch3nzg4HXEXzue5ILcbSYGKMLYZeidyt90lKRltNUgd@aws.connect.psdb.cloud:3306/kittusdatabase"
engine = create_engine(connection_string, echo=True)

def login_details(data):
  with engine.connect() as connection:
    string = text("insert into login_table(loginid,password) values( :loginid, :password)")

    params  = {
      
      "loginid" : data["email"],
      "password" : data["password"]
    }
    connection.execute(string, params)
    connection.commit()


def register_submitted(data):
  with engine.connect() as connection:
    string = text("insert into Registration_table (Firstname,LastName,email,contactnumber,password,confirmpassword)values(:Firstname, :LastName, :email, :contactnumber, :password, :confirmpassword)")

    params = {
      "Firstname" : data['first name'],
      "LastName"  : data["last name"],
      "email"  : data["email"],
      "contactnumber"  : data["contactnumber"],
      "password"  : data["newpassword"],
      "confirmpassword"  : data["confirm password"]
    }
    connection.execute(string, params)
    connection.commit()
  
                                
  