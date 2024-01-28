# TPM-httptool-template

Template/example for new [TPM](https://github.com/fjfjgg/TPM) tools over HTTP.

# Descripción

Herramienta en python que solo muestra información del fichero enviado y de los parámetros pasados.

Puede servir como base para invocar otros programas de corrección. 

## Estado del proyecto

Funciona correctamente.

## Tecnologías usadas

* Python

## Instalación

Instalar dependencias: 

```shell
python3 -m pip install flask requests werkzeug
```

Ejecutar con:

````shell
python3 http-tool-python.py
````

Probar con:

``` shell
curl -F "file=@test.txt" -F "userid=user" http://localhost:5000/httptool
```

El resultado debería ser algo como:

```json
{"file":"test.txt","score":100,"sha256sum":"...","size":14,"userid":"user"}
```

Cuando se cree la herramienta en TPM usar una configuración similar a la contenida en `config.json` sustituyendo el nombre del servidor.

## Licencia

Distributed under the GNU GENERAL PUBLIC LICENSE Version 3. See `LICENSE.txt` for more information.

## Contacto

Francisco José Fernández Jiménez - [@fjfjes](ht) - fjfj @ us.es

Project Link: <https://github.com/fjfjgg/tpm>

## Referencias

- [TPM](https://github.com/fjfjgg/TPM)