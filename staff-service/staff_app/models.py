from django.db import models


# Staff service doesn't need its own product models - it manages products 
# via REST API calls to laptop-service and mobile-service.
# The Staff model extends Django's built-in User model for staff-specific data.
