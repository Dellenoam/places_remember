def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None

    if backend.name == 'vk-oauth2':
        url = response.get('user_photo')

    if url:
        user.profile.avatar = url
        user.profile.save()
