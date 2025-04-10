from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    # Estamos reajeitando a função has_permission para ficar do jeito que queremos, pegando os Models, Métodos e Views, que precisamos
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    # '{app_name}.{action_name}_{model_name}' : Precisamos dessa string
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name               # Vai retornar qual model esta procurando
            app_label = view.queryset.model._meta.app_label                 # Vai retornar qual app esta procurando
            action = self.__get_action_sufix(method)                        # Vai retornar o método que está sendo usado
            return f'{app_label}.{action}_{model_name}'                     # A string completa
        except AttributeError:
            return None

    # Capturando todos os métodos que precisamos
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
