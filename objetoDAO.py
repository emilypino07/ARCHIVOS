from Datos.conexion import Conexion
from Dominio.objeto import Objeto


class ObjetoDAO:

    _INSERT = """
    INSERT INTO objeto
    (
        nombre, apellido, cedula, email,
        campo1, campo2, campo3, campo4, campo5,
        fecha
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    @classmethod
    def insertar(cls, obj):
        try:
            with Conexion.obtener_cursor() as cursor:

                datos = (
                    obj.nombre,
                    obj.apellido,
                    obj.cedula,
                    obj.email,
                    obj.campo1,
                    obj.campo2,
                    obj.campo3,
                    obj.campo4,
                    obj.campo5,
                    obj.fecha
                )

                cursor.execute(cls._INSERT, datos)
                Conexion.obtener_conexion().commit()

                print("Insertado correctamente")
                return cursor.rowcount

        except Exception as e:
            print("Error:", e)
            return -1


if __name__ == "__main__":
    obj = Objeto(
        "Sofia",
        "Vasquez",
        "0999999999",
        "sofivasquez@gmail.com",
        1,
        2,
        3,
        4,
        5,
        "2026-07-01"
    )

    ObjetoDAO.insertar(obj)