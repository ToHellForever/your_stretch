document.addEventListener("DOMContentLoaded", function() {
  // Инициализация основной карусели
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
    slidesPerView: 1, // Показываем больше слайдов по краям по умолчанию
    breakpoints: {
      // Когда ширина экрана меньше или равна 767px (мобильные устройства)
      767: {
        slidesPerView: 1.6, // Показываем только один слайд на мобильных устройствах
      }
    }
  });

  // Инициализация карусели для примеров работ (мобильная версия)
  const workSwiper = new Swiper(".work-swiper-mobile", {
    spaceBetween: 20, // Расстояние между слайдами
    loop: true, // Зацикливаем слайды
    slidesPerView: 1, // Показываем один слайд
    centeredSlides: true, // Центрируем активный слайд
    navigation: {
      nextEl: ".work-swiper-next",
      prevEl: ".work-swiper-prev"
    },
    autoplay: {
      delay: 5000, // Пауза между слайдами
      disableOnInteraction: false,
    }
  });

  // Инициализация карусели для галереи (мобильная версия)
  const gallerySwiper = new Swiper(".gallery-swiper-mobile", {
    spaceBetween: 10, // Расстояние между слайдами
    loop: true, // Зацикливаем слайды
    slidesPerView: 1, // Показываем одну фотографию на слайде
    centeredSlides: true, // Центрируем активный слайд
    navigation: {
      nextEl: ".gallery-swiper-next",
      prevEl: ".gallery-swiper-prev"
    },
    autoplay: {
      delay: 3000, // Пауза между слайдами
      disableOnInteraction: false,
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


// для модального окна
document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('callback-modal');
  const openButtons = document.querySelectorAll('.open-modal');
  const closeButtons = document.querySelectorAll('.close-modal');

  // Функция для открытия модального окна
  function openModal() {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden'; 
  }

  // Функция для закрытия модального окна
  function closeModal() {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto'; 
  }

  // Открытие модального окна по кнопке
  openButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      e.preventDefault(); 
      openModal();
    });
  });

  // Закрытие модального окна по кнопке закрытия
  closeButtons.forEach(button => {
    button.addEventListener('click', closeModal);
  });

  // Закрытие модального окна при клике вне его
  modal.addEventListener('click', function(event) {
    if (event.target === modal) {
      closeModal();
    }
  });

  // Закрытие модального окна по нажатию ESC
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && modal.style.display === 'flex') {
      closeModal();
    }
  });
});


document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('burger');
    const mobileMenu = document.getElementById('mobileMenu');
    const closeBtn = document.getElementById('closeMenu');
    const modal = document.getElementById('callback-modal');
    const mobileOrderButton = document.querySelector('#mobileMenu .header_button.open-modal');

    burger.addEventListener('click', () => {
        mobileMenu.classList.remove('d-none');
    });

    closeBtn.addEventListener('click', () => {
        mobileMenu.classList.add('d-none');
    });

    // Обработчик для кнопки "Заказать звонок" в мобильном меню
    mobileOrderButton.addEventListener('click', (e) => {
        e.preventDefault();
        // Закрываем мобильное меню
        mobileMenu.classList.add('d-none');
        // Открываем модальное окно обратного звонка
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    });

    // Можно добавить закрытие меню при клике вне его области
    mobileMenu.addEventListener('click', (e) => {
        if (e.target === mobileMenu) {
            mobileMenu.classList.add('d-none');
        }
    });
});
