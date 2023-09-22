from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 3847632
    API_HASH = "1a9708f807ddd06b10337f2091c67657"
    # the name to display in your alive message
    ALIVE_NAME = "broken hero"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://okuddbyb:w0ZhUOd3eK0HOP87x1sLZiCQXUt-Noic@mahmud.db.elephantsql.com/okuddbyb"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGgBu4m1GGcRUL-iZ5s-TYYh12SpwmEURAvD5TZJJ5OyoTQyc8M_XYxz4sQd7CMwlST5VRRWGWNMe4uhtLf7DphphHbpOzbJsI5uSDuUK7mkUP9Fa5PyBI4nuOh2UWnUu6m5uihUKBMI_uPW5hQgofrDSTWmUvPfRPWtU-K_7XAsj6kZlLApx8_ShQ52HjYn2twe611usajU0E3iyhm4Erqd3WNZF6rFL9HqEWgjy_t9SX972ZAOWagkZb-vPde25VKEuPqrzvc93Hdq11w37HOmSyE8luAn0eAqbwH0b7vqKHlUx6JmkOhp3R3ZCt2meP9-2lD6mY2LBjsqX3F07ljcq1Q="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6094160840:AAH5TUZAfFb_b8PyATJVzLQIAa1e2QNRwvY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001879747251
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
