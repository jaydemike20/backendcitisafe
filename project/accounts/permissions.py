from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.role == 'ADMIN')
    
class EnforcerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.role == 'ENFORCER')
    
class TreasurerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.role == 'TREASURER')
    
