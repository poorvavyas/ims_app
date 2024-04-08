IMS
==============================
* End to End incident and user flow
* Rest-api for User and Incident

Basic Commands
--------------
#. Steps To setup database.
    * CREATE DATABASE imsdb OWNER postgres;
    * In settings.py change database setting (edit username, password)
    * python manage.py makemigrations
    * python manage.py migrate

#. Steps to setup project
    * create a virtual environment.
    * install requirement using command pip install -r requirements.txt
    * python manage.py runserver to start the server

End To End Flow
^^^^^^^^^^^^^^^^^^^^^
Once the server is started browse following URL in browser for end to end UI flow :
    localhost_ Home Page.

    create_account_ To create User.


    login_ To login with username and password.

.. _localhost: http://127.0.0.1:8000/
.. _create_account: http://localhost:8000/user/add_user/
.. _login: http://localhost:8000/user/login_user/

Rest API
^^^^^^^^^^^^^^^^^^^^^
The rest api end-point starts with api/

#. To Add user
    * add_user_
        .. _add_user: http://127.0.0.1:8081/api/account/

        request object format::

        {   "username": "", "first_name": "", "last_name": "", "email": "", "password": ""}


#. To Add, update incident username password is required, if running from postman user Authorization -> Basic Auth, if using DRF login from top right login option.
   For **incident_status** you can pass **'O', 'P', 'C'**
   For **priority** you can pass **'L', 'M', 'H'**
    * add_incident_
        .. _add_incident: http://127.0.0.1:8081/api/incident/

        request object format::

        { "incident_detail": "", "priority": "L", "incident_status": "O"}

    * update_incident_
        .. _update_incident: http://127.0.0.1:8081/api/incident/4/

        request object format::

        { "id": 4 , "incident_detail": "", "priority": "L", "incident_status": "O"}

#. To search specific incident based on Incident_ID( username, password is required)
    * incident_by_id_
        .. _incident_by_id: http://127.0.0.1:8000/api/incident/by_incident_id/RMG000032022/
