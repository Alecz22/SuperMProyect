from dal.db import Db
import sqlite3

def agregarp(nombrep,cantidadp,preciop,catprod):    
    sql = "INSERT INTO Productos(NombreProducto,CantidadProducto,PrecioProducto,CategoriaProducto) VALUES(?, ?, ?,?);"
    parametros = (nombrep,cantidadp,preciop,catprod)
    Db.ejecutar(sql, parametros)

def listarp():
    sql = '''SELECT e.IdProducto, e.NombreProducto, e.CantidadProducto, e.PrecioProducto, e.CategoriaProducto
     FROM Productos e;'''
    # INNER JOIN Categorias r ON e.IdCategoria = r.IdCategoria;'''
    result = Db.consultar(sql)
    return result

def obtener_idp(prod_id):
    sql = '''SELECT e.IdProducto, e.NombreProducto, e.CantidadProducto, e.PrecioProducto, e.CategoriaProducto
            FROM Productos e
            WHERE e.IdProducto = ?;'''
            # INNER JOIN Categorias r ON e.IdCategoria = r.IdCategoria
    parametros = (prod_id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existep(producto):
    sql = "SELECT COUNT(*) FROM Productos WHERE NombreProducto = ?;"
    parametros = (producto,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def eliminarp(id, logical = True):    
    if logical:
        sql = '''DELETE FROM Productos WHERE IdProducto = ? ;'''
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def actualizarp(id,nombrep,cantidadp,preciop,catprod):    
    sql = "UPDATE Productos SET NombreProducto = ?, CantidadProducto = ?, PrecioProducto = ?, CategoriaProducto = ? WHERE IdProducto = ?;"
    parametros = (nombrep,cantidadp,preciop,catprod,id)
    Db.ejecutar(sql, parametros)   
