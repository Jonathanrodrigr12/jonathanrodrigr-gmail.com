-- Table: public."MessageWorld"

-- DROP TABLE public."MessageWorld";

CREATE TABLE public."MessageWorld"
(
    "Id" integer,
    "Message" character varying(50) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public."MessageWorld"
    OWNER to postgres;


INSERT INTO public."MessageWorld"(
	"Id", "Message")
	VALUES (1, 'Hola Mundo');