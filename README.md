# MiniBanco_TalentoB
Reto 2 Talento B - Ingeniería de software
Para el correcto funcionamiento local de la aplicación hay que instalar paquetes en
la terminal:
pip install "fastapi[all]"
pip install python-multipart sqlalchemy jinja2

Procedimiento realizado para la creación de la aplicación:

1) Se importa los módulos y paquetes necesarios
2) Se crea las tablas en la base de datos: se utiliza el motor SQLAlchemy para crear
las tablas en la base de datos, utilizando las definiciones de modelos
3) Se configura las plantillas Jinja2: Se crea una instancia de Jinja2Templates para
cargar las plantillas HTML
4) Se crea una instancia de la aplicación FastAPI
5) Se define una función para obtener la sesión de la base de datos
6) Se define las rutas y funciones de manejo de solicitudes
Este código muestra una aplicación web básica que utiliza FastAPI para crear rutas y manejar
solicitudes HTTP. La aplicación interactúa con una base de datos utilizando SQLAlchemy y renderiza
plantillas HTML utilizando Jinja2.
En resumen, es un CRUD con interfaz sencilla de formularios para el usuario, que permite:
• Registrar usuarios para la creación de cuenta bancaria
• Editar cuenta bancaria
• Retirarse del banco generando una transacción que disminuye el saldo de la cuenta a cero
• Eliminar cuenta bancaria
Todo lo anterior está conectado a la base de datos ‘bancodb’ y se puede ejecutar en SQLite Server
(3.4.4) para ver que las solicitudes se actualizan automáticamente dentro de la tabla ‘cuentas’.
También se tiene un formulario pensado para realizar transacciones entre cuentas, pero, mis
conocimientos actualmente en el framework no me permiten tener la lógica para usar los
condicionales y métodos necesarios para permitir hacer transacciones entre cuentas y que los
saldos se actualicen automáticamente en las tablas ‘movimientos’ y ‘tipo_transaccion’.
