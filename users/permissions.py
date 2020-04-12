from django.contrib.auth.models import User
from rest_framework import permissions


class IsAccessDeleteCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            stockins = obj.supplierstockout.filter(is_init=False).exists()
            if stockins:
                return False

        return True


class IsAccessDeleteSupplier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            stocks = obj.supplierstockin.filter(is_init=False).exists()
            if stocks:
                return False

        return True


class IsSelfOrAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            pk = view.kwargs.get('pk')
            if pk:
                obj = User.objects.get(pk=pk)
                if not request.user.is_superuser:
                    if obj.username != request.user.username:
                        return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_superuser:
            if obj.username != request.user.username:
                return False
        return True


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_superuser)
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        print(request.user.is_superuser)
        return request.user.is_superuser