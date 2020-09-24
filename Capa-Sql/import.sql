-----------
-----------
-----------EJECUTE PRIMERO ESTE SCRIPT
-----------
-----------

-- Database: prueba_app
-- DROP DATABASE prueba_app;
CREATE DATABASE prueba_app
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Colombia.1252'
    LC_CTYPE = 'Spanish_Colombia.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-----------
-----------
-----------EJECUTE PRIMERO ESTE SCRIPT
-----------
-----------


-----------
-----------
-----------EJECUTE SEGUNDO ESTE SCRIPT
-----------
-----------
--//////////////////////////////////////////
--////////////////////ROLES/////////////////
--//////////////////////////////////////////

-- SEQUENCE: public.Roles_Id_seq
-- DROP SEQUENCE public."Roles_Id_seq";
CREATE SEQUENCE public."Roles_Id_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;
ALTER SEQUENCE public."Roles_Id_seq"
    OWNER TO postgres;
-- Table: public.Roles
-- DROP TABLE public."Roles";
CREATE TABLE public."Roles"
(
    "Id" integer NOT NULL DEFAULT nextval('"Roles_Id_seq"'::regclass),
    "nombreRoll" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Roles_pkey" PRIMARY KEY ("Id"),
    CONSTRAINT "Roles_nombreRoll_key" UNIQUE ("nombreRoll")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
ALTER TABLE public."Roles"
    OWNER to postgres;


--//////////////////////////////////////////
--/////////////////USUARIOS APP/////////////
--//////////////////////////////////////////
-- SEQUENCE: public.UsuariosApp_Id_seq
-- DROP SEQUENCE public."UsuariosApp_Id_seq";
CREATE SEQUENCE public."UsuariosApp_Id_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;
ALTER SEQUENCE public."UsuariosApp_Id_seq"
    OWNER TO postgres;

-- Table: public.UsuariosApp
-- DROP TABLE public."UsuariosApp";
CREATE TABLE public."UsuariosApp"
(
    "Id" integer NOT NULL DEFAULT nextval('"UsuariosApp_Id_seq"'::regclass),
    "NombreApp" text COLLATE pg_catalog."default" NOT NULL,
    "Correo" text COLLATE pg_catalog."default",
    "IdRoles" integer NOT NULL,
    "Clave" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "UsuariosApp_pkey" PRIMARY KEY ("Id"),
    CONSTRAINT "UsuariosApp_Correo_key" UNIQUE ("Correo"),
    CONSTRAINT "UsuariosApp_NombreApp_key" UNIQUE ("NombreApp")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
ALTER TABLE public."UsuariosApp"
    OWNER to postgres;




--////////////////////////////////////////////////////////////////
--/////////////////TABLA DE SERVICOS FRONTEND BACKEND/////////////
--///////////////////////////////////////////////////////////////
--Crear una tabla con cuatro columnas: Created (fecha), State, Number, Title

-- SEQUENCE: public.Tabla1_Id_seq
-- DROP SEQUENCE public."Tabla1_Id_seq";
CREATE SEQUENCE public."Tabla1_Id_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;
ALTER SEQUENCE public."Tabla1_Id_seq"
    OWNER TO postgres;
-- Table: public.Tabla1
-- DROP TABLE public."Tabla1";
CREATE TABLE public."Tabla1"
(
    "Id" integer NOT NULL DEFAULT nextval('"Tabla1_Id_seq"'::regclass),
    "Created" date NOT NULL DEFAULT now(),
    "State" text COLLATE pg_catalog."default" NOT NULL,
    "Number" text COLLATE pg_catalog."default" NOT NULL,
    "Title" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Tabla1_pkey" PRIMARY KEY ("Id")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
ALTER TABLE public."Tabla1"
    OWNER to postgres;


--//////////////////////////////////////////
--/////////////////ASOCIACIONES/////////////
--//////////////////////////////////////////
-- SEQUENCE: public.Asociaciones_Id_seq
-- DROP SEQUENCE public."Asociaciones_Id_seq";
CREATE SEQUENCE public."Asociaciones_Id_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;
ALTER SEQUENCE public."Asociaciones_Id_seq"
    OWNER TO postgres;

-- Table: public.Asociaciones
-- DROP TABLE public."Asociaciones";
CREATE TABLE public."Asociaciones"
(
    "Id" integer NOT NULL DEFAULT nextval('"Asociaciones_Id_seq"'::regclass),
    "NomAsociacion" text COLLATE pg_catalog."default" NOT NULL,
    "Tipo" text COLLATE pg_catalog."default",
    "NIT" text COLLATE pg_catalog."default" NOT NULL,
    "Direcciones" text COLLATE pg_catalog."default" NOT NULL,
    "Telefonos" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Asociaciones_pkey" PRIMARY KEY ("Id"),
    CONSTRAINT "Asociaciones_NIT_key" UNIQUE ("NIT"),
    CONSTRAINT "Asociaciones_NomAsociacion_key" UNIQUE ("NomAsociacion")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
ALTER TABLE public."Asociaciones"
    OWNER to postgres;

-----------
-----------
-----------EJECUTE SEGUNDO ESTE SCRIPT
-----------
-----------


-----------
-----------
-----------EJECUTE RERCERO  ESTE SCRIPT
-----------
-----------

--//////////////////////////////////////////
--/////////////////ROLES USUARIOS/////////////
--//////////////////////////////////////////
--IMPORTANTE PARA USUARIO TOKEN
INSERT INTO public."Roles"("nombreRoll")VALUES ('Admin');

INSERT INTO public."UsuariosApp"("NombreApp", "Correo", "IdRoles", "Clave")
VALUES ('Applicacion1', 'app1@gmail.com', 1, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJOb21icmVBcHAiOiJBcHBsaWNhY2lvbjEiLCJJZFJvbGVzIjoxLCJDbGF2ZSI6IiQyYiQxMCRsdVNRR0VjV2xxMExBS3dldmprL0Z1SGxUTjJPcnE5U2JNZHVMVWliUW52QzkuMHJnbmNnMiIsIm5vbWJyZVJvbGwiOiJBZG1pbiJ9.3YTBpaFlSsYfQwBaFnhjHWfo1Uqj7tMpQ5Q8kCSFWOo');



--//////////////////////////////////////////
--/////////////////DATOS DE PRUEBA IN/////////////
--//////////////////////////////////////////
--Llene la tabla con 10 registros que usted desee
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '1', 'titulo1');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '2', 'titulo2');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '3', 'titulo3');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '4', 'titulo4');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '5', 'titulo5');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '6', 'titulo6');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '7', 'titulo7');
INSERT INTO public."Tabla1"("State", "Number", "Title")
VALUES ('activo', '8', 'titulo8');

