from datetime import datetime as tiempo


class Log:

    @classmethod
    def log(cls, mensaje: str) -> None:
        """Genera un log visualizable en la terminal"""
        fecha_crudo = tiempo.now()
        primer_parte = f'[{fecha_crudo.year}-{fecha_crudo.month}-{fecha_crudo.day}'
        segunda_parte = f'{fecha_crudo.hour}:{fecha_crudo.minute}:{fecha_crudo.second}]'
        fecha_log = primer_parte + ' ' + segunda_parte + ' ' + mensaje
        print(fecha_log)
