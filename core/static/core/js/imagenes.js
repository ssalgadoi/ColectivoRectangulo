// document.addEventListener("DOMContentLoaded", function() {
//   const imagenes = document.querySelector(".imagenes");

//   if (imagenes) {
//     let isDragStart = false, prevPageX, prevScrollLeft;

//     const dragStart = (e) => {
//       isDragStart = true;
//       prevPageX = e.pageX;
//       prevScrollLeft = imagenes.scrollLeft;
//     }

//     const dragging = (e) => {
//       if (!isDragStart) return;
//       e.preventDefault();
//       let positionDiff = e.pageX - prevPageX;
//       imagenes.scrollLeft = prevScrollLeft - positionDiff;
//     }

//     const dragStop = () => {
//       isDragStart = false;
//     }

//     imagenes.addEventListener("mousedown", dragStart);
//     imagenes.addEventListener("mousemove", dragging);
//     imagenes.addEventListener("mouseup", dragStop);
//   } else {
//     console.error("El elemento .imagenes no se encontró en el DOM.");
//   }
// });

