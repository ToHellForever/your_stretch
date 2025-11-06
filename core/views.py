from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from .models import Product, Profile, Gallery, Banner, MobileBanner, Order, CallbackRequest
import json
from django.http import JsonResponse

class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dekstop_banners'] = Banner.objects.all()
        context['mobile_banners'] = MobileBanner.objects.all()
        context['products'] = Product.objects.all()
        context['profiles'] = Profile.objects.all()
        context['galleries'] = Gallery.objects.prefetch_related('images').all()
        return context

    @method_decorator(csrf_exempt)
    @method_decorator(ratelimit(key='ip', rate='3/m', method='POST', block=True))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            # Обработка формы заказа натяжных потолков
            if 'phone' in request.POST and 'area' in request.POST:
                area = request.POST.get('area', '0')  # Устанавливаем значение по умолчанию
                corners = request.POST.get('corners', '0')  # Устанавливаем значение по умолчанию
                lights = request.POST.get('lights', '0')  # Устанавливаем значение по умолчанию
                pipes = request.POST.get('pipes', '0')  # Устанавливаем значение по умолчанию
                ceiling_type = request.POST.get('ceiling_type', 'Не указан')  # Устанавливаем значение по умолчанию
                comment = request.POST.get('comment', '')  # Устанавливаем значение по умолчанию
                phone = request.POST.get('phone')

                # Проверяем, что телефон не пустой
                if not phone:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Пожалуйста, укажите ваш телефон.'
                    }, status=400)

                from decimal import Decimal, InvalidOperation

                # Преобразуем значения в корректные типы
                try:
                    area_value = Decimal(area) if area else 0
                except InvalidOperation:
                    area_value = 0

                corners_value = int(corners) if corners else 0
                lights_value = int(lights) if lights else 0
                pipes_value = int(pipes) if pipes else 0

                # Создаем новый заказ
                order = Order.objects.create(
                    area=area_value,
                    corners=corners_value,
                    lights=lights_value,
                    pipes=pipes_value,
                    ceiling_type=ceiling_type or 'Не указан',
                    comment=comment,
                    phone=phone
                )

                # Возвращаем успешный ответ
                return JsonResponse({
                    'status': 'success',
                    'message': 'Ваш заказ успешно отправлен! Мы свяжемся с вами в ближайшее время.'
                })

            # Обработка запроса обратного звонка
            elif 'callback_phone' in request.POST:
                phone = request.POST.get('callback_phone')

                # Проверяем, что телефон не пустой
                if not phone:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Пожалуйста, укажите ваш телефон.'
                    }, status=400)

                # Создаем запрос обратного звонка
                callback = CallbackRequest.objects.create(phone=phone)

                # Возвращаем успешный ответ
                return JsonResponse({
                    'status': 'success',
                    'message': 'Спасибо! Мы скоро свяжемся с вами.'
                })

            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Некорректные данные формы.'
                }, status=400)

        except Exception as e:
            import traceback
            print(f"Ошибка при обработке формы: {e}")
            print(traceback.format_exc())
            return JsonResponse({
                'status': 'error',
                'message': f'Произошла ошибка при обработке формы: {str(e)}'
            }, status=500)
