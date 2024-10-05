

def path_avatar_user(instance, file) -> str:
    return f"user_{instance.pk}/img/{file}"


def path_logo_shop(instance, file) -> str:
    return f"user_{instance.user_id}/shop/{file}"


def path_background_shop(instance, file) -> str:
    return f"user_{instance.user_id}/shop/{file}"


def path_screenshot_complaint(instance, file) -> str:
    return f"user_{instance.user_id}/screenshot/{file}"
