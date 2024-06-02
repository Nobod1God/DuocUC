Proceso SaludoConContador
    // Inicializar el contador
    Definir contadorSaludos como entero;
    contadorSaludos <- 0;
	
    // Definir la variable saludo fuera del bucle
    Definir saludo como caracter;
    Definir saludarDeNuevo como caracter;
	
    Repetir
        // Incrementar el contador
        contadorSaludos <- contadorSaludos + 1;
		
        // Ingresar un mensaje
        Escribir "Escribe un mensaje:";
        Leer saludo;
		
        // Saludar
        Escribir "Hola Humano";
		
        // Preguntar al usuario si desea saludar de nuevo
        Escribir "¿Quieres saludarme de nuevo? (si/no):";
        Leer saludarDeNuevo;
		
    Hasta que saludarDeNuevo <> "si";
	
    // Mostrar el número total de saludos realizados
    Escribir "Número total de saludos que me haz realizado: ", contadorSaludos;
FinProceso