from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    
class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return hasattr(request.user, 'teacher')
    
class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

class IsAdminOrTeacherViewingTheirStudents(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or hasattr(request.user, 'teacher')
    

class AttendancePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return request.method in SAFE_METHODS
        elif hasattr(user, 'teacher'):
            return True
        elif hasattr(user, 'student'):
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return request.method in SAFE_METHODS
        elif hasattr(user, 'teacher'):
            return obj.lesson.teacher == user.teacher
        elif hasattr(user, 'student'):
            return obj.student == user.student and request.method in SAFE_METHODS
        return False

class IsAdminOrStudentReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (hasattr(user, 'student') or user.is_staff)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if hasattr(request.user, 'student'):
            return obj.student_group.student == request.user.student
        return False

class AddressPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser or user.is_staff:
            return True  # admin full access

        if hasattr(user, 'student') and obj == user.address:
            return request.method in SAFE_METHODS

        if hasattr(user, 'teacher'):
            teacher = user.teacher
            student_users = [s.user for s in teacher.student_set.all()]
            if obj in [s.address for s in student_users if s.address]:
                return request.method in SAFE_METHODS

        return False
    
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)