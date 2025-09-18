


class BasicUser:
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password

    def login(self,user_name,password,email):
       return  self.user_name == user_name and password == password and email == email

class Admin(BasicUser):
    def __init__(self, user_name, email, password):
        super().__init__(self, user_name, email,password)

    def admin_login(self,user_name,password,email):
        return self.user_name == user_name and self.password == password and self.email == email

    def delete_user(self, user_name):
        print("Deleting user.. "+ user_name)
        return "Deleted user "+ user_name


class Moderator(BasicUser):
    def __init__(self, user_name, email, password):
        super().__init__(user_name, email, password)

    def moderator_login(self,user_name,password,email):
        return self.user_name == user_name and password == password and self.email == email

    def ban_user(self, user_name):
        print("Banning user.. "+ user_name)
        return "Banned user "+ user_name


class regular_user(BasicUser):
    def __init__(self, user_name, email, password):
        super().__init__(user_name, email, password)
    def post_comment(self, comment):
        print("Posting comment. "+ comment)

