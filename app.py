from base import create_app
import os

app = create_app()
app_name = "generation"

# with app.app_context():
#     if os.path.exists(f'{app_name}.db'):
#         pass
#         # db.drop_all()
#     else:
#         db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
