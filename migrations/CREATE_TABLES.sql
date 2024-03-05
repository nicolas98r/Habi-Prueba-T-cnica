/* Create Tables */

CREATE TABLE "PROPERTY"
(
	property_id varchar(32) NOT NULL,
	property_name varchar(50) NOT NULL,
	description varchar(200) NULL,
	year_of_build date NOT NULL,
	address varchar(70) NOT NULL,
	status_id integer NULL
)
;

CREATE TABLE "PROPERTY_STATUS"
(
	status_id integer NOT NULL,
	status_name varchar(50) NOT NULL
)
;

/* Create PK And FK */

ALTER TABLE "PROPERTY" ADD CONSTRAINT "PK_PROPERTY"
	PRIMARY KEY (property_id)
;

ALTER TABLE "PROPERTY_STATUS" ADD CONSTRAINT "PK_PROPERTY_STATUS"
	PRIMARY KEY (status_id)
;

ALTER TABLE "PROPERTY" ADD CONSTRAINT "FK_PROPERTY_PROPERTY_STATUS"
	FOREIGN KEY (status_id) REFERENCES "PROPERTY_STATUS" (status_id) ON DELETE No Action ON UPDATE No Action
;