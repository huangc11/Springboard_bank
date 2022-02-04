import logging


format_def='%(asctime)s:%(filename)s:%(name)s:%(levelname)s:%(message)s'
glb_logger= logging.getLogger(__name__)
glb_logger.setLevel(logging.INFO)
glb_formatter = logging.Formatter('%(asctime)s:%(filename)s:%(name)s:%(levelname)s:%(message)s')

glb_file_handler = logging.FileHandler('logs\log_global.log')
glb_file_handler.setLevel(logging.INFO)
glb_file_handler.setFormatter(glb_formatter)
glb_logger.addHandler((glb_file_handler))


class Utility:
    logger_excption =None
    logger_app = None

    def print_one(one):
        print('********** {} **************'.format(one))

    def print_error(one):
        print('####### {} ########'.format(one))

    def print_success(one):
       # print('!!!!!!!!!! {} !!!!!!!!!!!!'.format(one)
        print(one.center(70,'!'))

    def log_exeption(e):
        glb_logger.info(e)
        Utility.logger_excption.exception(e)

    def log_info(msg):
        glb_logger.info(msg)

    def print_debug(one):
        print('!!{} '.format(one))





def setup_logger(name, log_file, level=logging.INFO, format=format_def):
            """To setup as many loggers as you want"""

            f_handler = logging.FileHandler(log_file)
            f_formatter = logging.Formatter(format)
            f_handler.setFormatter(f_formatter)

            logger = logging.getLogger(name)
            logger.setLevel(level)
            logger.addHandler(f_handler)

            return logger




Utility.logger_excption = setup_logger('logger_expt', 'logs\log_excepion.log')

Utility.logger_app = setup_logger('logger_app', 'logs\log_app.log')
