import _opaquepy as rust_mod


def generate_keys() -> tuple[str, str]:
    """

    :return: Tuple of encoded private key and public key, respectiely.
    """
    return rust_mod.generate_keys_py()


def register(client_request: str, public_key: str) -> tuple[str, str]:
    """

    :param client_request:
    :param public_key:
    :return: Tuple of encoded response to the client and register state to be saved, respectively.
    """
    return rust_mod.register_server_py(client_request, public_key)


def register_finish(client_request_finish: str, register_state: str) -> str:
    """

    :param client_request_finish:
    :param register_state:
    :return: Password file to be saved.
    """
    return rust_mod.register_server_finish_py(client_request_finish, register_state)


def register_client(password: str) -> tuple[str, str]:
    """

    :param password:
    :return: Tuple of encoded response to the server and register state to be saved, respectively.
    """
    return rust_mod.register_client_py(password)


def register_client_finish(client_register_state: str, server_message: str) -> str:
    """

    :param client_register_state:
    :param server_message:
    :return: Encoded response to the server.
    """
    return rust_mod.register_client_finish_py(client_register_state, server_message)


def login(password_file: str, client_request: str, private_key: str) -> tuple[str, str]:
    """

    :param password_file:
    :param client_request:
    :param private_key:
    :return: Tuple of encoded response to the client and login state to be saved, respectively.
    """
    return rust_mod.login_server_py(password_file, client_request, private_key)


def login_finish(client_request_finish: str, login_state: str) -> str:
    """
    Finish the login process on the backend.

    :param client_request_finish: Client request to finish login, base64url-encoded.
    :param login_state: Saved login state from the previous step, base64url-encoded.
    :return: The session key, base64url-encoded.
    """
    return rust_mod.login_server_finish_py(client_request_finish, login_state)
