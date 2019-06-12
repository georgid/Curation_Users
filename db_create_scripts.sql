
CREATE TABLE "license" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 "num_users_allowed" integer NOT NULL,
 "name" varchar(50) NOT NULL);

INSERT INTO "license" VALUES(1,1,'Free Plan');
INSERT INTO "license" VALUES(2,3,'Basic License Plan');
INSERT INTO "license" VALUES(3,5,'Professional License Plan');



CREATE TABLE "role" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 "name" varchar(50) NOT NULL);

INSERT INTO "role" VALUES(1,'Ordinary User');
INSERT INTO "role" VALUES(2,'Company Admin');
INSERT INTO "role" VALUES(3,'System Admin');



CREATE TABLE "user_company_role" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"company_id" integer NULL REFERENCES "company" ("id"),
"role_id" integer NULL REFERENCES "role" ("id"), 
"user_id" integer NULL REFERENCES "auth_user" ("id")
);

INSERT INTO "user_company_role" VALUES(3,1,2,2);
INSERT INTO "user_company_role" VALUES(4,2,1,2);


CREATE TABLE "permission" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(50) NOT NULL, 
"code" integer NOT NULL, 
"Type" integer NOT NULL);

INSERT INTO "permission" VALUES(1,'Create User',1,1);
INSERT INTO "permission" VALUES(2,'Delete User',2,1);
INSERT INTO "permission" VALUES(3,'Create Orgnisation',3,1);




CREATE TABLE "company" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"name" varchar(50) NOT NULL, 
"license_id" integer NULL REFERENCES "license" ("id")
);

INSERT INTO "company" VALUES(1,'Company 1',2);
INSERT INTO "company" VALUES(2,'Company 2',1);



CREATE TABLE "permission_role" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
 "error_id" integer NOT NULL, 
 "permission_id" integer NULL REFERENCES "companies_permission" ("id") ,
 "role_id" integer NULL REFERENCES "companies_role" ("id")
 );

INSERT INTO "permission_role" VALUES(1,1,1,1);
INSERT INTO "permission_role" VALUES(2,1,2,1);
INSERT INTO "permission_role" VALUES(3,2,3,1);
INSERT INTO "permission_role" VALUES(4,2,3,2);

