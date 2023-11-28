import yaml

FILE_PATH = "src\\config\\prompts_config\\prompts.yml"

class PromptsConfig:

    admin_prompt = None
    manager_prompt = None
    create_new_user_role =None
    asset_assignable_prompt  =None
    employee_prompt = None
    track_assets_prompt = None
    maintenance_prompt = None

    @classmethod
    def load(cls):
        with open(FILE_PATH,'r') as file:
            data = yaml.safe_load(file)
            cls.admin_prompt = data['admin_prompt']
            cls.manager_prompt = data['manager_prompt']
            cls.create_new_user_role = data['create_new_user_role']
            cls.asset_assignable_prompt  = data['asset_assignable_prompt']
            cls.employee_prompt = data['employee_prompt']
            cls.track_assets_prompt = data['track_assets_prompt']
            cls.maintenance_prompt = data['maintenance_prompt']