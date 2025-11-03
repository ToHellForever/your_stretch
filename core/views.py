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
        context['banners'] = Banner.objects.all()
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
                area = request.POST.get('area', 0)
                corners = request.POST.get('corners', 0)
                lights = request.POST.get('lights', 0)
                pipes = request.POST.get('pipes', 0)
                ceiling_type = request.POST.get('ceiling_type', '')
                comment = request.POST.get('comment', '')
                phone = request.POST.get('phone')

                # Создаем новый заказ
                order = Order.objects.create(
                    area=area or 0,
                    corners=corners or 0,
                    lights=lights or 0,
                    pipes=pipes or 0,
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
