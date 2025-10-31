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
      nextEl: ".swiper-slide-next",
      prevEl: ".swiper-slide-prev"
    },
    initialSlide: 1, // Начинаем со второго слайда (чтобы был центральный)
    slidesPerView: 1.6, // Показываем больше слайдов по краям
    
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


// для модального окна
document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('callback-modal');
  const openButton = document.querySelector('.open-modal');
  const closeButton = document.querySelector('.close-modal');

  openButton.addEventListener('click', function () {
    modal.style.display = 'block'; // Открывает модалку
  });

  closeButton.addEventListener('click', function () {
    modal.style.display = 'none'; // Закрывает модалку
  });

  window.onclick = function(event) {
    if (event.target === modal) {
      modal.style.display = 'none'; // Закрывает модалку при щелчке вне нее
    }
  };
});