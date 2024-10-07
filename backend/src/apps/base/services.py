def path_avatar_user(instance, file) -> str:
    return f"user_{instance.pk}/img/{file}"


def path_logo_shop(instance, file) -> str:
    return f"user_{instance.user_id}/shop/{file}"


def path_background_shop(instance, file) -> str:
    return f"user_{instance.user_id}/shop/{file}"


def path_screenshot_complaint(instance, file) -> str:
    return f"user_{instance.user_id}/screenshot/{file}"


def path_photo_product(instance, file) -> str:
    return f"user_{instance.product_id.user_id}/shop/{file}"


def path_image_message(instance, file) -> str:
    return f"user_{instance.user_id}/chat_{instance.chat_id}/images/{file}"


def path_file_message(instance, file) -> str:
    return f"user_{instance.user_id}/chat_{instance.chat_id}/files/{file}"
