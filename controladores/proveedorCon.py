from server.conexion_sql import conecciones


class R_proveedor:
    def __int__(self):
        self.conn = conecciones()

    def obtener_proveedor(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM proveedor"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarProveedor(self, empresa, cantidad, precio, codigo, imagen):
        print("---Guardando---")
        self.conn = conecciones()
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO proveedor (idProveedor, empresa, cantidad, precio, codigo,imagen) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, empresa, cantidad, precio, codigo, imagen))
            self.conn.commit()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idProveedor) FROM proveedor")
        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def getProveedor(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM proveedor WHERE idProveedor = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarproveedor(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto_carro`.`proveedor` WHERE idPprovedor = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()