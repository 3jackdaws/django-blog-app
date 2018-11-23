# Django Blog App

## Creation Process
1.  `git clone http://github.com/3jackdaws/django-ws-starter`
2.  Scrap pretty much everything in there
3.  Create new blog app
4.  Create Post model
5.  Create Post Form
6.  Realize I want to use AJAX
7.  Struggle to choose between using a ModelForm, manually defining everything in a normal Form, or defining a form just in HTML
8.  Decide on using rest_framework's render_form tag and delete PostForm
9.  Create Post serializer
10. Create Post ViewSet
11. Create a bunch of routes
12. Write UI
13. Add AJAX stuff to UI
14. Write tests
15. Run tests
16. Realize PUT method doesn't behave correctly
17. Fix PUT method
18. Add some padding and max-width to containers
19. Change timezone
20. Change database to SQLite instead of postgres so that Docker and standard deployments are the same


## Deployment

### Docker
1.  `docker-compose up`

### Standard/Non-Docker
1.  Install python 3.6 or so
2.  `pip install -r requirements.txt`
3.  `./manage.py makemigrations`
4.  `./manage.py migrate`
5.  `./manage.py runserver`


## Tests
### PostAPI
Very briefly covers creating and editing a Post.  Obviously should test with more strings.  It would also be nice to get some actual UI tests in there with selenium.