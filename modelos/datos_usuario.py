from server.conexion_sql import conecciones


class ModeloUsuario:
    def __int__(self):
        self.conn = conecciones()

    def obtener_id_usuario(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idUsuario) FROM usuario")
        count = cursor.fetchone()[0]
        count = count + 1
        return count

    def obtener_ultimo_id_usuario(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(idUsuario) FROM usuario")
        count = cursor.fetchone()[0]
        return count

    def obtener_usuario(self):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM usuario"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def insertarUsuario(self, usuario, contrasena, nombre, apellido, puesto):
        print("datos tomados---")
        self.conn = conecciones()
        id = self.obtener_id_usuario()
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO usuario (idUsuario,usuario,nombre,apellido,puesto) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (id, usuario, contrasena, nombre, apellido, puesto))
            self.conn.commit()

    def getUsuario(self, cod):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuario WHERE idUsuario = '"+cod+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def eliminarUsuario(self, id):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "DELETE FROM `proyecto_carro`.`usuario` WHERE idUsuario = '"+id+"'"
            cursor.execute(sql)
            self.conn.commit()
