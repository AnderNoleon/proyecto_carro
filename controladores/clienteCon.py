from server.conexion_sql import conecciones


class RegistarCliente:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idCliente) FROM cliente")
        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_ultimo_id_cliente(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idCliente) FROM cliente")

        count = cursor.fetchone()[0]
        return count

    def obtener_cliente(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarCliente(self, nombre, nit, celular, direccion, tipo):
        print("----datos ------")
        self.conn = conecciones()
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cliente (idCliente, nombre_cliente, nit, celular,direccion, Tipo_idTipo) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, nit, celular, direccion, tipo))
            self.conn.commit()
        print("----Hecho ------")

    def insertarClienteee(self, nombre, nit, celular, direccion, tipo):
        print("----datos ------")
        self.conn = conecciones()
        id = self.obtener_id()
        with self.conn.cursor() as cursor:
            if not nit:
                nit = None
            sql = """INSERT INTO cliente (idCliente, nombre_cliente, nit, celular, direccion, Tipo_idTipo) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, nombre, nit, celular, direccion, tipo))
            self.conn.commit()
        print("----Hecho ------")

    def getcliente(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM cliente WHERE idCliente = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarcliente(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto_carro`.`cliente` WHERE idCliente = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()

    def subirCliente(self, Id, nombre, nit, celular, direccion, tipo):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET nombre_cliente = %s, nit = %s, celular = %s,
            direccion = %s, Tipo_idTipo = %s WHERE idCliente= %s """
            cursor.execute(sql, (nombre, nit, celular, direccion, tipo, Id))
            self.conn.commit()
