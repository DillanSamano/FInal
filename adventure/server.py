from flask_app import app 
from flask_app.controllers import user_controller
from flask_app.controllers import adventure_controller
from flask_app.controllers import posts_controller
from flask_app.controllers import post_likes_controller
from flask_app.controllers import comment_controller
from flask_app.controllers import comment_likes_controller



if __name__ =='__main__':
    app.run(debug=True)