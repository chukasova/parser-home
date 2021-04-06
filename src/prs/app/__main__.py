import os
import argparse

BASE_DIR = os.path.abspath(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    __file__,
                ),
            ),
        ),
    ),
)


def get_version():
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()


def create_parser():
    parser = argparse.ArgumentParser(
        prog="News parser",
        description=(
            "Мега крутая программа для парсинга новостей\n"
            "с сайта \n"
            "Закостылил (c) Я "
        ),
        add_help=False,
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Вывести данное сообщение.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Текущая версия.",
        version=get_version(),
    )
    parser.add_argument(
        "-d",
        "--daemon",
        action="store_true",
        required=False,
        help="Запуск приложения в режиме демона.",
    )
    parser.add_argument(
        "-k",
        "--kill",
        action="store_true",
        help="Остановить приложение.",
    )
    return parser


parser = create_parser()
args = parser.parse_args()
print(args)