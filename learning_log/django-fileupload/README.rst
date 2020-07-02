=======
learning_logs
=======

Fileupload is a app to upload files.

Quick start
-----------

1. Add "fileapp" to your INSTALLED_APPS setting like this::
        INSTALLED_APPS = [
                ...
                'learning_logs',
        ]

2. Include the polls URLconf in your project urls.py like this::
        path('learning_logs/',include('learning_logs.urls'),name='learning_logs'),

3. Run "python manage.py migrate" to create the models.
