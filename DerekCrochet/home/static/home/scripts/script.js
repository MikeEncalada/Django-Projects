function scrollCatalogo(idCatalogo, direccion) {
    const catalogo = document.getElementById(idCatalogo);
    const scrollAmount = 300; // Ajusta la cantidad de desplazamiento según sea necesario
    if (direccion === 'derecha') {
      catalogo.scrollLeft += scrollAmount;
    } else if (direccion === 'izquierda') {
      catalogo.scrollLeft -= scrollAmount;
    }
  }