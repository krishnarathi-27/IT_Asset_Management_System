# IT ASSET MANAGEMENT SYSTEM

## Introduction 
```bash 
    This application is designed to manage IT assets in an organisations. It provides functionality for Admins, Asset Manager and Employee. Details about assets such as category and vendor of asset is managed by keeping track of the inventory of all assets available in the organisations along with which assets are assigned to which employee.
```

## Project Installation & Getting Started

```bash
1. Clone this repository
    https://github.com/krishnarathi-27/IT_Asset_Management_System.git

2. Install project dependencies using
    python -m pipenv install

3. Make .env file in the project root directory along with following :
    ADMIN_MAPPING=
    MANAGER_MAPPING=
    EMPLOYEE_MAPPING=
    MYSQL_USER=
    MYSQL_PASSWORD=
    MYSQL_HOST=
    MYSQL_DB=
    JWT_SECRET_KEY=

4. Run Application using the following command
    cd .\src\
    python -m flask run

```

##  Project Structure

```bash
    |   .env
    |   .flaskenv
    |   .gitignore
    |   Pipfile
    |   Pipfile.lock
    |   pytest.ini
    |   README.md
    |   tree.txt
    |   
    +---src
    |   |   app.py
    |   |   logs.txt
    |   |   __init__.py
    |   |   
    |   +---config
    |   |   |   app_config.py
    |   |   |   queries.py
    |   |   |   __init__.py
    |   |   |   
    |   |   \---prompts
    |   |           prompts.py
    |   |           prompts.yaml
    |   |           __init__.py
    |   |           
    |   +---controller
    |   |   +---asset_controller
    |   |   |       create_asset_controller.py
    |   |   |       update_asset_controller.py
    |   |   |       view_asset_controller.py
    |   |   |       
    |   |   +---auth_controller
    |   |   |       login_controller.py
    |   |   |       logout_controller.py
    |   |   |       
    |   |   +---category_controller
    |   |   |       create_category_controller.py
    |   |   |       view_category_controller.py
    |   |   |       
    |   |   +---issue_controller
    |   |   |       create_issue_controller.py
    |   |   |       update_issue_controller.py
    |   |   |       view_issue_controller.py
    |   |   |       
    |   |   +---user_controller
    |   |   |       create_user_controller.py
    |   |   |       update_user_controller.py
    |   |   |       view_user_controller.py
    |   |   |       
    |   |   \---vendor_controller
    |   |           create_vendor_controller.py
    |   |           delete_vendor_controller.py
    |   |           view_vendor_controller.py
    |   |           
    |   +---database
    |   |       database.py
    |   |       database_context.py
    |   |       __init__.py
    |   |       
    |   +---handlers
    |   |       asset_handler.py
    |   |       auth_handler.py
    |   |       category_handler.py
    |   |       issue_handler.py
    |   |       user_handler.py
    |   |       vendor_handler.py
    |   |       
    |   +---routes
    |   |       asset_routes.py
    |   |       auth_routes.py
    |   |       category_routes.py
    |   |       issue_routes.py
    |   |       track_routes.py
    |   |       user_routes.py
    |   |       vendor_routes.py
    |   |       
    |   \---schemas
    |           asset_schema.py
    |           issue_schema.py
    |           user_schema.py
    |           
    \---tests
        |   __init__.py
        |   
        +---test_controllers
        |       test_admin_controllers.py
        |       test_asset_controllers.py
        |       test_asset_data_controllers.py
        |       test_auth_controllers.py
        |       test_employee_controllers.py
        |       test_manager_controllers.py
        |       __init__.py
        |       
        +---test_utils
        |       test_app_decorator.py
        |       test_common_helper.py
        |       test_validations.py
        |       __init__.py
        |       
        \---test_views
                test_admin_views.py
                test_employee_views.py
                test_maintenance_views.py
                test_manager_views.py
                test_track_asset_views.py
```   
