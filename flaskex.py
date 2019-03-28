from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello Flask!'

@app.route('/profile/<username>')
def get_profile(username):
  return 'profile : %s ' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return 'post : %d ' % post_id

if __name__ == '__main__':
  app.run()