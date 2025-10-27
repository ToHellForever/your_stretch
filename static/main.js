  document.addEventListener("DOMContentLoaded", function() {
    const swiper = new Swiper(".mySwiper", {
      spaceBetween: 30, // Расстояние между слайдами
      pagination: false, // Отключаем пагинацию
      loop: true, // Зацикливаем слайды
      centeredSlides: true, // Центрируем активный слайд
      autoplay: {
        delay: 3000, // Пауза между слайдами (в миллисекундах)
        disableOnInteraction: false, // Разрешаем автопрокрутку после нажатия на кнопку
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
      },
      initialSlide: 1, // Начинаем со второго слайда (чтобы был центральный)
      breakpoints: {
        // Для мобильных устройств
        "@0": {
          slidesPerView: 1.2,
          centeredSlides: true,
        }
      }
    });

    // Добавляем обработчики событий для кнопок навигации внутри слайдов
    document.querySelectorAll('.swiper-slide-prev').forEach(button => {
      button.addEventListener('click', function() {
        swiper.slidePrev();
      });
    });

    document.querySelectorAll('.swiper-slide-next').forEach(button => {
      button.addEventListener('click', function() {
        swiper.slideNext();
      });
    });
  });

