# Instructions

## How to add login
- In the project urls.py, add
    ```
        path('membership/', include('django.contrib.auth.urls')),
    ```
- create templates/authentication dir
- create templates/authentication/login.html file
- create login_user in views.py, app/urls.py, login.html
- create the form in login.html

## Update password
- Watch this: https://www.youtube.com/watch?v=lxdQ7y19wo4