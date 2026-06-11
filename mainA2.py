#Actividad 2: Manipulación de listas, tuplas y diccionarios
carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")


personas: list[tuple[str, str, int, int]] = [
    # nombre, apellido, edad, carrera
]
 
estudiantes: list[dict[str, str | int]] = [
    # Lista de diccionario con nombre, apellido, edad, carrera
]
for _ in range(5):
    # Solicita los datos aquí
    nombre = input("Ingrese su nombre :")
    apellido = input("Ingrese su apellido :")
    edad = int(input("Ingrese su edad :"))
    carrera = int(input("Ingresa su carrera (ingrese: 0 = Ingeniería de Software, 1 = Contabilidad, 2 = Derecho):"))
    print("")

    #creacion de tupla
    datos = (nombre, apellido, edad, carrera)
    personas.append(datos)#tupla agregada a la lista de personas

    #recorrido de la lista personas
    for datos in personas:
        nombre = datos[0]
        apellido = datos[1]
        edad = datos[2]
        carrera = carreras[datos[3]]

        diccionario = {"nombre": nombre, "apellido": apellido, "edad": edad, "carrera": carrera}
        estudiantes.append(diccionario)
        print("")

        for estudiante in estudiantes:
            nombre = estudiante["nombre"]
            apellido = estudiante["apellido"]
            edad = estudiante["edad"]
            carrera = estudiante["carrera"]

        print(nombre, apellido, "tiene", edad, " años y estudia", carrera)

