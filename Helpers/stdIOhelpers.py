def disable_warnings():
    import logging

    logging.basicConfig()
    logging.getLogger().setLevel(logging.ERROR)
    logging.captureWarnings(True)
