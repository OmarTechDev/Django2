# main_app/middleware/validator_middleware.py
import json
import importlib
from django.utils.deprecation import MiddlewareMixin
from main_app.handlers.validator_handler import ValidatorHandler
class ValidatorMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_class = getattr(view_func, 'cls', None)
        if not view_class:
            return None
        view_name = view_class.__name__
        method_name = self.get_method_name(request)
        module_name = view_name.split('ViewSet')[0].lower()
        validator_module_path = f"main_app.request_validator.{module_name}_validator_setting"
        validator_module = importlib.import_module(validator_module_path)
        VALIDATORS = getattr(validator_module, 'VALIDATORS', None)
        if view_name in VALIDATORS and method_name in VALIDATORS[view_name]:
            validators = ValidatorHandler.load_validators(view_name, method_name)
            if request.method != "GET":
                ValidatorHandler.execute_validators(validators, json.loads(request.body.decode('utf-8')))
        return None

    def get_method_name(self, request):
        method_map = {
            'POST': 'create',
            'GET': 'list' if 'pk' not in request.resolver_match.kwargs else 'retrieve',
            'PUT': 'update',
            'PATCH': 'partial_update',
            'DELETE': 'destroy',
        }
        return method_map.get(request.method)