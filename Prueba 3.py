
flag = True    
while flag == True:
    listaPuntaje = ["ID jugador: ", "Nombre: ", "Apellido: ", "Valorant: ", "Fortnite: ", "Fifa: ", "Tipo: "]

    print("****REGISTRO DE PUNTAJES****")
    print("1. Registrar puntajes torneo")
    print("2. Listar los tipos de puntaje")
    print("3. Imprimir por tipo")
    print("4. Salir del programa")

    opcion = 1
        
    while opcion < 4 and opcion > 0:
        opcion = int(input("Seleccione un opcion: "))
        if opcion == 1:
                
            idjugador = ""
            while idjugador == "":
                idjugador = input("Ingrese el ID del jugador: ")
                listaPuntaje.append(idjugador)
                
            nombre = ""
            while nombre == "":
                nombre = input("Ingrese el nombre del jugador: ")
                listaPuntaje.append(nombre)

            apellido = ""
            while apellido == "":
                apellido = input("Ingresa el apellido del jugador: ")
                listaPuntaje.append(apellido)
                
            valorant = -1
            while valorant < 0:
                valorant = int(input("Ingresa el puntaje en valorant: "))
                listaPuntaje.append(valorant)

            fortnite = -1
            while fortnite < 0:
                fortnite = int(input("Ingresa el puntaje en Fortnite: "))
                listaPuntaje.append(fortnite)

            fifa = -1
            while fifa < 0:
                fifa = int(input("Ingresa el puntaje en fifa: "))
                listaPuntaje.append(fifa)

            opc = -1
            while opc < 1 or opc > 3:
                print("1. Principiante \n2. Avanzado \n3. Experto")
                opc = int(input("Ingresa una opcion: "))
                if opc == 1:
                    tipo = "Principiante"           
                    listaPuntaje.append(tipo)
                elif opc == 2:
                    tipo = "Avanzado"
                    listaPuntaje.append(tipo)
                elif opc == 3:
                    tipo = "Experto"
                    listaPuntaje.append(tipo)
            
        elif opcion == 2:
            print(listaPuntaje)

        elif opcion == 3:
            print(listaPuntaje)
        elif opcion == 4:
            print("Saliendo")
            flag = False
