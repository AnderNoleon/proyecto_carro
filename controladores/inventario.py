from server.conexion_sql import conecciones


class clase_inventario:
    def __int__(self):
        self.conn = conecciones()

    def obtener_por_codigo_usuario(self, code):
        self.conn = conecciones()
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuario WHERE usuario = '" + code + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result

    def obtener_key(self):
        self.conn = conecciones()
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuario")

        count = cursor.fetchone()[0]
        count = count + 1
        return count