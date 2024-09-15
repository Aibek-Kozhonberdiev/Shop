

def path_avatar_user(instance, file) -> str:
    return f"user_{instance.pk}/img/{file}"
