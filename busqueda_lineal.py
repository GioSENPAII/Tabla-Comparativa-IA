## función de búsqueda
def buscar_elemento(arr, n, elemento):

	## iterando a través del array
	for i in range(n):

		## comprobando el elemento actual con el elemento requerido
		if arr[i] == elemento
			## devolviendo True en caso de coincidencia
			devolver True

	## no se encuentra el elemento de ahí que la ejecución venga aquí
	devolver Falso


if __name__ == '__main__':
	## inicializar el array, la longitud y el elemento a buscar
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n = 10
	elemento_a_buscar = 6
	# elemento_a_buscar = 11

	if buscar_elemento(arr, n, elemento_a_buscar):
		print(elemento_a_buscar, "se ha encontrado")
	si no
		print(elemento_a_buscar, "no se encuentra")
