GitHub --> Entrega 1 - Agustin Ariel Diaz y Agustin Alejando Diaz

Descripción: Entrega intermedia de proyecto final 01/09:

Integrantes:
- Diaz, Agustin Ariel
- Diaz, Agustin Alejandro

Instrucciones, paso a paso explicado:

1. Primero con python manage.py runserver, nos dirigimos a http://127.0.0.1:8000, luego entramos a http://127.0.0.1:8000/AppIntermedia/inicio/  --> con el botón 'Inicio' vuelve a esa misma dirección.

2. Como segundo paso, se pueden recorrer los botones creados en la parte superior de la página: 'Buscar', 'Supervisores', 'Empleados' y 'Usuarios'; que cada uno contiene un formulario respectivo a su modelo, para rellenar/completar con datos que son guardados en la base de datos. Ej.![image](https://user-images.githubusercontent.com/110953463/187737827-721b2af6-466a-4aca-97aa-e82966bd5df7.png)

Por otro lado, el botón 'Buscar', contiene específicamente un campo para introducir datos/búsquedas por nombre.

--> Estos aparecen y se ven en admin/ ![image](https://user-images.githubusercontent.com/110953463/187737715-a2b5676b-206a-4989-8551-39ca0e1fa575.png)
    Acá ejemplo del model Empleado: ![image](https://user-images.githubusercontent.com/110953463/187737976-08a245ba-dbe4-4354-bb52-3aa2423292d1.png)

3. Por último, el formulario o campo para buscar datos en la base de datos, fue creado en base a la clase del modelo 'Empleado' en el cual, si se busca 'Agustin', 'Pedro' o 'Ludmila', filtra y encuentra por apellido y nombre sus datos del nombre.
Ej.: ![image](https://user-images.githubusercontent.com/110953463/187740056-1042b5f6-885e-4622-b0f0-c5f797d9e0fe.png) -- Buscamos el nombre 'Agustin' y le damos al botón 'Buscar' y el resultado es este: ![image](https://user-images.githubusercontent.com/110953463/187740154-472be9c9-da76-4716-bf4a-8a12b6c96ee9.png)
