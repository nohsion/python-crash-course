import logging


def setup_logger(level=logging.INFO):
    lol_logger = logging.getLogger('lol-logger')
    lol_logger.setLevel(level)

    # 콘솔 핸들러 생성
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 포맷터 생성
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # 로거에 핸들러 추가
    lol_logger.addHandler(console_handler)

    return lol_logger


# 전역 로거 생성
logger = setup_logger()
