  document.addEventListener("DOMContentLoaded", function() {
    const swiper = new Swiper(".mySwiper", {
      slidesPerView: 3, // Показываем 3 слайда
      spaceBetween: 30, // Расстояние между слайдами
      pagination: false, // Отключаем пагинацию
      // зацикаваемость слайдов
      loop: true, // Зацикливаем слайды
      autoplay: {
        delay: 3000, // Пауза между слайдами (в миллисекундах)
        disableOnInteraction: false, // Разрешаем автопрокрутку после нажатия на кнопку
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
      },
      initialSlide: 0, // Начинаем с первого слайда
      centeredSlides: false // Отключаем центрирование, чтобы все 3 слайда были видны
    });
  });
