import gettext

gettext.bindtextdomain("messages", "locales")
gettext.textdomain("messages")
_ = gettext.gettext


def main():
    print(_("Hello, world!"))


if __name__ == "__main__":
    main()
    