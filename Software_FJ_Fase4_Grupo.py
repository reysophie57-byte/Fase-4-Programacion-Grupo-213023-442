
# ==========================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Programa: Ingeniería de Sistemas
# Curso: Programación - 213023
# Fase 4: Componente práctico - Prácticas simuladas
# Proyecto: Sistema Integral de Gestión de Clientes,
# Servicios y Reservas - Software FJ
# ==========================================================

# INTEGRANTES DEL GRUPO
# Integrante 1: Sofía del Pilar Reyes Bernal
# Integrante 2: Juan José Díaz Valderrama
# Integrante 3: Diego Fernando González Yara
# Integrante 4: Luisa Fernanda Galeano Montealegre


# ==========================================================
# PARTE 1. IMPORTACIÓN DE LIBRERÍAS
# Responsable: Sofía
# ==========================================================

from abc import ABC, abstractmethod
import re


# ==========================================================
# PARTE 2. ENTIDAD GENERAL DEL SISTEMA
# Responsable: Sofía del Pilar Reyes Bernal
# ==========================================================

class EntidadSistema(ABC):
    """
    Clase abstracta que contiene las características
    generales de las entidades del sistema Software FJ.
    """

    def __init__(self, identificacion):

        # Comprueba que la identificación sea válida.
        if not isinstance(identificacion, (str, int)):
            raise ValueError("La identificación debe ser texto o número.")

        identificacion = str(identificacion).strip()

        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        if not identificacion.isalnum():
            raise ValueError("La identificación contiene caracteres no permitidos.")

        self._identificacion = identificacion

    @property
    def identificacion(self):
        """Permite consultar la identificación."""
        return self._identificacion

    @abstractmethod
    def mostrar_informacion(self):
        """Método que deben implementar las clases derivadas."""
        pass


# ==========================================================
# PARTE 3. CLASE CLIENTE
# Responsable: Sofía del Pilar Reyes Bernal
# ==========================================================

class Cliente(EntidadSistema):
    """
    Representa a los clientes registrados en Software FJ.
    Valida y protege sus datos personales.
    """

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        self.__nombre = self._validar_nombre(nombre)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

    def _validar_nombre(self, nombre):
        """Comprueba que el nombre contenga letras y espacios."""

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        nombre = nombre.strip()

        if not all(
            letra.isalpha() or letra.isspace()
            for letra in nombre
        ):
            raise ValueError("El nombre solo debe contener letras y espacios.")

        return nombre

    def _validar_correo(self, correo):
        """Verifica que el correo tenga una estructura válida."""

        if not isinstance(correo, str):
            raise ValueError("El correo debe ser un texto.")

        correo = correo.strip()

        patron = r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, correo):
            raise ValueError("El correo electrónico no es válido.")

        return correo.lower()

    def _validar_telefono(self, telefono):
        """Comprueba que el teléfono tenga entre 7 y 15 dígitos."""

        if not isinstance(telefono, (str, int)):
            raise ValueError("El teléfono debe contener números.")

        telefono = str(telefono).strip()

        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener dígitos.")

        if not 7 <= len(telefono) <= 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        return telefono

    # ------------------------------------------------------
    # PROPIEDADES PARA CONSULTAR LOS DATOS DEL CLIENTE
    # ------------------------------------------------------

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # ------------------------------------------------------
    # MÉTODO PARA MOSTRAR LA INFORMACIÓN
    # ------------------------------------------------------

    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )


# ==========================================================
# PARTE 4. LISTA INTERNA DE CLIENTES
# Responsable: Sofía
# ==========================================================

clientes_registrados = []


def registrar_cliente(cliente):
    """
    Agrega un cliente a la lista si no está registrado.
    """

    if not isinstance(cliente, Cliente):
        raise TypeError("El objeto recibido no corresponde a un cliente.")

    for registrado in clientes_registrados:
        if registrado.identificacion == cliente.identificacion:
            raise ValueError("El cliente ya se encuentra registrado.")

    clientes_registrados.append(cliente)

    print("Cliente registrado correctamente.")


# ==========================================================
# PARTE 5. PRUEBAS INICIALES DEL APORTE
# Responsable: Sofía
# ==========================================================

def ejecutar_prueba(descripcion, operacion):

    print("\n" + "=" * 55)
    print("PRUEBA:", descripcion)

    try:
        operacion()

    except (ValueError, TypeError) as error:
        print("Error controlado:", error)

    except Exception as error:
        print("Error inesperado:", error)

    else:
        print("Operación realizada correctamente.")

    finally:
        print("Finalizó la prueba.")


# ----------------------------------------------------------
# PRUEBA 1. REGISTRO DE CLIENTE VÁLIDO
# ----------------------------------------------------------

def prueba_cliente_valido():

    cliente = Cliente(
        "1001",
        "María López",
        "maria@gmail.com",
        "3001234567"
    )

    registrar_cliente(cliente)
    print(cliente.mostrar_informacion())


# ----------------------------------------------------------
# PRUEBA 2. REGISTRO CON IDENTIFICACIÓN VACÍA
# ----------------------------------------------------------

def prueba_identificacion_invalida():

    cliente = Cliente(
        "",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3001234567"
    )

    registrar_cliente(cliente)


# ----------------------------------------------------------
# PRUEBA 3. REGISTRO CON NOMBRE VACÍO
# ----------------------------------------------------------

def prueba_nombre_invalido():

    cliente = Cliente(
        "1002",
        "",
        "ana@gmail.com",
        "3001234567"
    )

    registrar_cliente(cliente)


# ----------------------------------------------------------
# PRUEBA 4. REGISTRO CON CORREO INCORRECTO
# ----------------------------------------------------------

def prueba_correo_invalido():

    cliente = Cliente(
        "1003",
        "Ana Torres",
        "correo_incorrecto",
        "3001234567"
    )

    registrar_cliente(cliente)


# ----------------------------------------------------------
# PRUEBA 5. REGISTRO CON TELÉFONO INCORRECTO
# ----------------------------------------------------------

def prueba_telefono_invalido():

    cliente = Cliente(
        "1004",
        "Pedro Gómez",
        "pedro@gmail.com",
        "ABC123"
    )

    registrar_cliente(cliente)


# ----------------------------------------------------------
# EJECUCIÓN DE LAS PRUEBAS
# ----------------------------------------------------------

if __name__ == "__main__":

    ejecutar_prueba(
        "Registro de cliente válido",
        prueba_cliente_valido
    )

    ejecutar_prueba(
        "Identificación vacía",
        prueba_identificacion_invalida
    )

    ejecutar_prueba(
        "Nombre vacío",
        prueba_nombre_invalido
    )

    ejecutar_prueba(
        "Correo incorrecto",
        prueba_correo_invalido
    )

    ejecutar_prueba(
        "Teléfono incorrecto",
        prueba_telefono_invalido
    )


# ==========================================================
# PARTE 6. SERVICIOS
# Responsable: Juan José Díaz Valderrama
# Pendiente de integrar su desarrollo.
# ==========================================================


# ==========================================================
# PARTE 7. RESERVAS
# Responsable: Diego Fernando González Yara
# Pendiente de integrar su desarrollo.
# ==========================================================


# ==========================================================
# PARTE 8. EXCEPCIONES, LOGS Y PRUEBAS GENERALES
# Responsable: Luisa Fernanda Galeano Montealegre
# Pendiente de integrar su desarrollo.
# ==========================================================


