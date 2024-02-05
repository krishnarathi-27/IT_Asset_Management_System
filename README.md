# IT ASSET MANAGEMENT SYSTEM

## Introduction 
```bash 
    This application is designed to manage IT assets in an organisations. It provides 
    functionality for Admins, Asset Manager and Employee. Details about assets such 
    as category and vendor of asset is managed by keeping track of the inventory of 
    all assets available in the organisations along with which assets are assigned 
    to which employee.
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
|   app.py
|   logs.txt
|   __init__.py
|   
+---config
|   |   app_config.py
|   |   flask_config.py
|   |   queries.py
|   |   __init__.py
|   |   
|   \---prompts
|           prompts.py
|           prompts.yaml
|           __init__.py
|           
+---controller
|   |   __init__.py
|   |   
|   +---asset_controller
|   |       create_asset_controller.py
|   |       update_asset_controller.py
|   |       view_asset_controller.py
|   |       __init__.py
|   |       
|   +---auth_controller
|   |       login_controller.py
|   |       logout_controller.py
|   |       __init__.py
|   |       
|   +---category_controller
|   |       create_category_controller.py
|   |       view_category_controller.py
|   |       __init__.py
|   |       
|   +---issue_controller
|   |       create_issue_controller.py
|   |       update_issue_controller.py
|   |       view_issue_controller.py
|   |       __init__.py
|   |       
|   +---user_controller
|   |       create_user_controller.py
|   |       update_user_controller.py
|   |       view_user_controller.py
|   |       __init__.py
|   |       
|   \---vendor_controller
|           create_vendor_controller.py
|           delete_vendor_controller.py
|           view_vendor_controller.py
|           __init__.py
|           
+---database
|       database.py
|       database_context.py
|       __init__.py
|       
+---handlers
|   |   auth_handler.py
|   |   __init__.py
|   |   
|   +---asset_handler
|   |       create_asset_handler.py
|   |       update_asset_handler.py
|   |       view_asset_handler.py
|   |       __init__.py
|   |       
|   +---category_handler
|   |       create_category_handler.py
|   |       view_category_handler.py
|   |       __init__.py
|   |       
|   +---issue_handler
|   |       create_issue_handler.py
|   |       update_issue_handler.py
|   |       view_issue_handler.py
|   |       __init__.py
|   |       
|   +---user_handler
|   |       create_user_handler.py
|   |       update_user_handler.py
|   |       view_user_handler.py
|   |       __init__.py
|   |       
|   \---vendor_handler
|           create_vendor_handler.py
|           delete_vendor_handler.py
|           view_vendor_handler.py
|           __init__.py
|           
+---routes
|       asset_routes.py
|       auth_routes.py
|       category_routes.py
|       issue_routes.py
|       track_routes.py
|       user_routes.py
|       vendor_routes.py
|       __init__.py
|       
+---schemas
|       asset_schema.py
|       issue_schema.py
|       user_schema.py
|       __init__.py
|       
\---utils
        common_helper.py
        error_handler.py
        exceptions.py
        mapped_roles.py
        rbac.py
        response.py
        secure_password.py
        __init__.py
            
```   
