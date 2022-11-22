CREATE TABLE "Clientes" (
	"IdCliente"	INTEGER NOT NULL UNIQUE,
	"Nombre"	TEXT(50) NOT NULL,
	"Email"	TEXT(50) UNIQUE,
	"Dni"	INTEGER(11) NOT NULL,
	"Direccion"	TEXT(100),
	"Activo"	INTEGER DEFAULT 1,
	"NumeroTelefonico"	INTEGER(25) NOT NULL,
	PRIMARY KEY("IdCliente")
)

CREATE TABLE "Productos" (
    "IdProducto"        INTEGER PRIMARY KEY AUTOINCREMENT,
    "NombreProducto"    TEXT,
    "CantidadProducto"  INTEGER,
    "PrecioProducto"    FLOAT,
    "CategoriaProducto" TEXT
)

CREATE TABLE "Categorias" (
    "IdCategoria"        INTEGER PRIMARY KEY AUTOINCREMENT,
    "NombreCategoria"    TEXT(25)
)

CREATE TABLE "Empleados" (
	"IdEmpleado" INTEGER NOT NULL UNIQUE,
	"Cargo" TEXT(20) NOT NULL, 
	"Nombre"	TEXT(50) NOT NULL,
	"Edad" INTEGER(2) NOT NULL,
	"Email"	TEXT(50) UNIQUE NOT NULL,
	"Dni"	INTEGER(11) NOT NULL,
	"Direccion"	TEXT(100) NOT NULL,
	"NumeroTelefonico"	INTEGER(25) NOT NULL,
	PRIMARY KEY("IdEmpleado")
)

CREATE TABLE "Factura" (
    "IdFacturas"        INTEGER PRIMARY KEY AUTOINCREMENT,
    "CargadoDatos"    TEXT(9999999)
)

CREATE TABLE "CodigoFactura" (
    "IdFactura"        INTEGER PRIMARY KEY AUTOINCREMENT,
    "ANombreDe"    TEXT(45)
)

