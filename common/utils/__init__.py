from datetime import datetime


def save_picture(instance, filename):
    """
    Generate a unique filename for saving a picture associated with an
    instance.

    Args:
        instance: The instance (e.g., a model instance) for which the
        picture is being saved.
        filename (str): The original filename of the picture.

    Returns:
        str: The unique filename for saving the picture.
    """
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name
    my_date = str(datetime.now().isoformat())

    picture_name = "".join(
        [
            "".join(filename.split('.')[:-1]),
            my_date,
            ".",
            filename.split('.')[-1]
        ]
    )
    return (f"{app_name}/{model_name}/{instance.pk}/{instance.pk}_"
            f"{picture_name}")
