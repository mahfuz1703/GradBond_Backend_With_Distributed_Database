class CoreDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations based on the model's database."""
        if model.__name__ == 'AlumniModel':
            return 'alumni'
        elif model.__name__ == 'StudentModel':
            return 'student'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direct write operations based on the model's database."""
        if model.__name__ == 'AlumniModel':
            return 'alumni'
        elif model.__name__ == 'StudentModel':
            return 'student'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations within the same database."""
        db_set = {'default', 'alumni', 'student'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations for each model go to the correct database."""
        if model_name == 'alumnimodel':
            return db == 'alumni'
        elif model_name == 'studentmodel':
            return db == 'student'
        return db == 'default'
