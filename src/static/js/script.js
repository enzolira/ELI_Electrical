function confirmar(event) {
  if (!confirm('¿Estás seguro de que quieres cerrar sesión?')) {
    event.preventDefault();
  }
}

const icon = document.querySelector(".bi-cart-check");

icon.addEventListener("click", function() {
  this.classList.add("rotate-once");

  setTimeout(() => {
    this.classList.remove("rotate-once");
  }, 500);
});

// -------------------------------------------------------
// -------------------------------------------------------
