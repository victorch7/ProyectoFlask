class Config:
    DEBUG = True
    # Otras configuraciones para tu aplicación

class DevelopmentConfig(Config):
    DEBUG = False
    # Configuraciones específicas para entorno de desarrollo

class ProductionConfig(Config):
    DEBUG = False
    # Configuraciones específicas para producción
    # Por ejemplo, configuración de base de datos, secretos, etc.
