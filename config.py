import os

class Config:
    '''
    General configuration parent class
    '''
    BASE_URL=''
    API_KEY=os.environ.get('MOVIE_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config : the parent configuration class with General configuration settings
    '''
    DEBUG = True



config_options={
    'development':DevConfig,
    'production':ProdConfig
}