# from rest_framework import permissions
# from rest_framework_simplejwt.tokens import BlacklistedToken

# class BlacklistCheckPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         try:
#             auth_header = request.META.get('HTTP_AUTHORIZATION')
#             prefix, token = auth_header.split(' ')
#             if prefix.lower() == 'bearer':
#                 BlacklistedToken(token)  # Raise exception if blacklisted
#             return True
#         except BlacklistedToken:
#             return False
#         except Exception:  
#             return False