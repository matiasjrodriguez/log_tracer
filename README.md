## Instalación

Use el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar Log Tracer.

```bash
pip install -i https://test.pypi.org/simple/ log-tracer
```

## Uso

```python
from log_tracer import Log


log = Log()
log.log('Hola mundo')

```

## Salida

```bash
[2022-11-20 20:18:32] Hola mundo
```