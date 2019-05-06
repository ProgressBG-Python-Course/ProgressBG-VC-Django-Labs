class MusicCatalogLegacyDbRouter:
    """
    A router to control all database operations on models 
    in the music_catalog_app.
    """
    def db_for_read(self, model, **hints):
        # Attempts to read music_catalog_app go to music_catalog_legacy_db.
        if model._meta.app_label == 'music_catalog_app':
            return 'music_catalog_legacy_db'
        return None

    def db_for_write(self, model, **hints):
        # Attempts to write music_catalog_app go to music_catalog_legacy_db.
        if model._meta.app_label == 'music_catalog_app':
            return 'music_catalog_legacy_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are part of the worlddata app
        if obj1._meta.app_label == 'music_catalog_app' and \
            obj2._meta.app_label == 'music_catalog_app':
            return True
        # Allow if neither is part of worlddata app
        elif 'music_catalog_app' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        # by default return None - "undecided"

    def allow_migrate(self, db, app_label, model_name=None, **hints):       
        # allow migrations on the "default" (django related data) DB
        if db == 'default' and app_label != 'music_catalog_app':
            return True

        # allow migrations on the legacy database too
        # this will enable us to actually alter the database schema of the legacy DB.
        if db == 'music_catalog_legacy_db' and app_label == "music_catalog_app":
           return True

        return False