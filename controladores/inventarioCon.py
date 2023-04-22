from server.conexion_sql import conecciones


class RegistrarInventario:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idInventario) FROM inventario")
        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_producto(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM inventario"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProduct(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM inventario WHERE Id_inventario = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def obtener_por_codigo(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM inventario WHERE codigo_producto = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def subirproducto(self, id, codigo, producto, Existencia, precio_costo, precio_venta):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """UPDATE inventario SET codigo_carro = %s, producto = %s, existencia = %s,
            precio_costo = %s, precio_venta = %s WHERE IdInventario = %s """
            cursor.execute(sql, (codigo, producto, Existencia, precio_costo, precio_venta, id))
            self.conn.commit()

    def insertarProducto(self, codigo, producto, existencia, precio_costo, precio_venta):
        self.conn = conecciones()
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO inventario (idInventario,codigo_carro,producto,existencia,precio_costo,precio_venta) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, codigo, producto, existencia, precio_costo, precio_venta))
            self.conn.commit()

    def eliminarproducto(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto`.`inventario` WHERE Id_inventario = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()
