from django.shortcuts import redirect


class OwnerCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.owner != self.request.user and not self.request.user.groups.filter(name='moderators').exists() \
                and not self.request.user.is_superuser:
            return redirect('catalog:home')

        return super().dispatch(request, *args, **kwargs)
