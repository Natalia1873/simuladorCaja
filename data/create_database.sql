CREATE TABLE "productos" (
	"id"	INTEGER UNIQUE,
	"nombre"	TEXT NOT NULL,
	"precio_unitario"	REAL NOT NULL,
	PRIMARY KEY("id")
);
