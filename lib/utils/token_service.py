def build_access_token(app_id: str, app_secret: str) -> str:
    """
    According to the documentation (https://developers.facebook.com/docs/facebook-login/access-tokens/#generating-an-app-access-token),
    you can just pass your app ID and app secret as the access_token
    parameter when you make a call.

    Args:
        app_id: go to https://developers.facebook.com/apps/ and
            In "Settings > Basic", find "App ID".
        app_secret: do the same and find "App Secret".

    Returns:
        access_token
    """
    return f"{app_id}|{app_secret}"