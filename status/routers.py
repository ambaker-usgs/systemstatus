class PingRouter(object):
    """
    A router to control all database operations on models in the
    ping application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read assays models go to ping_db.
        """
        if model._meta.app_label == 'ping':
            return 'ping_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write assays models go to ping_db.
        """
        if model._meta.app_label == 'ping':
            return 'ping_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ping app is involved.
        """
        if obj1._meta.app_label == 'ping' or \
           obj2._meta.app_label == 'ping':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Prevent migration to ping_db and migration of ping models
        """
        if app_label == 'ping':
            return False
        if db == 'ping_db':
            return False
        return None
