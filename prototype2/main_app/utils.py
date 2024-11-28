from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Manage general erorrs over 403 and 404
    """
    response = exception_handler(exc, context)

    logger.error(f"Exception occurred: {exc}", exc_info=True)

    if response is not None:
        if isinstance(exc, NotFound):
            return Response(
                {
                    'success': False,
                    'error': 'The requested resource was not found.',
                    'details': response.data
                },
                status=status.HTTP_404_NOT_FOUND
            )

        elif isinstance(exc, PermissionDenied):
            return Response(
                {
                    'success': False,
                    'error': 'You do not have permission to perform this action.',
                    'details': response.data
                },
                status=status.HTTP_403_FORBIDDEN
            )

        return Response(
            {
                'success': False,
                'error': response.data
            },
            status=response.status_code
        )

    return Response(
        {
            'success': False,
            'error': 'An unexpected error occurred. ********************',
            'details': str(exc)
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )



# from rest_framework.views import exception_handler
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.exceptions import (
#     NotAuthenticated, PermissionDenied, AuthenticationFailed,
#     ValidationError, ParseError, NotFound, Throttled, MethodNotAllowed,
#     UnsupportedMediaType
# )
# import logging

# logger = logging.getLogger(__name__)

# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     logger.error(f"Exception occurred: {exc}", exc_info=True)

#     # Personalizar mensajes para errores comunes
#     if isinstance(exc, NotFound):
#         return Response({'success': False, 'error': 'Resource not found'}, status=404)
#     elif isinstance(exc, PermissionDenied):
#         return Response({'success': False, 'error': 'Permission denied'}, status=403)
#     elif isinstance(exc, NotAuthenticated):
#         return Response({'success': False, 'error': 'Authentication required'}, status=401)
#     elif isinstance(exc, AuthenticationFailed):
#         return Response({'success': False, 'error': 'Invalid credentials'}, status=401)
#     elif isinstance(exc, ValidationError):
#         return Response({'success': False, 'error': 'Validation error', 'details': response.data}, status=400)
#     elif isinstance(exc, Throttled):
#         return Response({'success': False, 'error': 'Too many requests. Please try again later.'}, status=429)
#     elif isinstance(exc, MethodNotAllowed):
#         return Response({'success': False, 'error': 'HTTP method not allowed'}, status=405)
#     elif isinstance(exc, UnsupportedMediaType):
#         return Response({'success': False, 'error': 'Unsupported media type'}, status=415)

#     # Manejo global de excepciones no controladas
#     return Response(
#         {'success': False, 'error': 'An unexpected error occurred.', 'details': str(exc)},
#         status=status.HTTP_500_INTERNAL_SERVER_ERROR
#     )
