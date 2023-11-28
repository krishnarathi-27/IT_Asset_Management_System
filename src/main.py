import logging
#local imports
from utils.helper_functions import config_loader
from config.statements.statements import StatementsConfig
from config.logs_config.log_statements import LogStatements
from authentication.authentication import Authentication

if __name__ == "__main__":

    @config_loader
    def fun_main() -> None:
        '''Method where logger is initialised and program starts'''
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            level = logging.DEBUG,
            filename = LogStatements.log_file_location
        )
        logger = logging.getLogger('main')
        logger.info(LogStatements.starting_application_log)
        print(StatementsConfig.starting_application)
        '''Creates all the tables of database if not exists already'''
        authentication_obj = Authentication()
        authentication_obj.login()

    fun_main()
    