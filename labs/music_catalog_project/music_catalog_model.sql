BEGIN;
--
-- Create model Album
--
CREATE TABLE "music_catalog_album" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "date" datetime NULL, "about" text NULL, "thumbnail" varchar(100) NOT NULL, "is_fav" bool NOT NULL, "release_date" date NULL);
--
-- Create model Artist
--
CREATE TABLE "music_catalog_artist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "about" text NULL, "thumbnail" varchar(100) NOT NULL, "birth_date" date NULL, "is_fav" bool NOT NULL);
--
-- Create model Genre
--
CREATE TABLE "music_catalog_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "notes" text NULL);
--
-- Create model Track
--
CREATE TABLE "music_catalog_track" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "duration" bigint NULL, "lyrics" text NULL, "is_fav" bool NOT NULL, "album_id" integer NOT NULL REFERENCES "music_catalog_album" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "music_catalog_track_artist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "track_id" integer NOT NULL REFERENCES "music_catalog_track" ("id") DEFERRABLE INITIALLY DEFERRED, "artist_id" integer NOT NULL REFERENCES "music_catalog_artist" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field artist to album
--
CREATE TABLE "music_catalog_album_artist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "album_id" integer NOT NULL REFERENCES "music_catalog_album" ("id") DEFERRABLE INITIALLY DEFERRED, "artist_id" integer NOT NULL REFERENCES "music_catalog_artist" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field genre to album
--
CREATE TABLE "music_catalog_album_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "album_id" integer NOT NULL REFERENCES "music_catalog_album" ("id") DEFERRABLE INITIALLY DEFERRED, "genre_id" integer NOT NULL REFERENCES "music_catalog_genre" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "music_catalog_track_album_id_1129d3d2" ON "music_catalog_track" ("album_id");
CREATE UNIQUE INDEX "music_catalog_track_artist_track_id_artist_id_195bc04d_uniq" ON "music_catalog_track_artist" ("track_id", "artist_id");
CREATE INDEX "music_catalog_track_artist_track_id_87048fc0" ON "music_catalog_track_artist" ("track_id");
CREATE INDEX "music_catalog_track_artist_artist_id_ad06a5d0" ON "music_catalog_track_artist" ("artist_id");
CREATE UNIQUE INDEX "music_catalog_album_artist_album_id_artist_id_857de457_uniq" ON "music_catalog_album_artist" ("album_id", "artist_id");
CREATE INDEX "music_catalog_album_artist_album_id_9d580a9c" ON "music_catalog_album_artist" ("album_id");
CREATE INDEX "music_catalog_album_artist_artist_id_5441251d" ON "music_catalog_album_artist" ("artist_id");
CREATE UNIQUE INDEX "music_catalog_album_genre_album_id_genre_id_8ff8f1fb_uniq" ON "music_catalog_album_genre" ("album_id", "genre_id");
CREATE INDEX "music_catalog_album_genre_album_id_57a73030" ON "music_catalog_album_genre" ("album_id");
CREATE INDEX "music_catalog_album_genre_genre_id_86a43f90" ON "music_catalog_album_genre" ("genre_id");
COMMIT;
