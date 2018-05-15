
VALID_COMMANDS = ["CREATE", "ADD", "REMOVE", 
            "START", "FOCUS", "CONF", 
            "PLAY", "SHOW", "LIST", 
            "HELP", "EXIT", "QUIT"]

class Command:
    def create(options):
        print("You are inside CREATE game function!")
        print("Options given: {}".format(options))
        # TODO: check options
        return "created {} sucessfuly.".format(options[0])

    def conf_play(options):
        print("You are inside CONF PLAY game function!")
        print("Options given: {}".format(options))
        # TODO: check options
        return "configured play {} with option {} sucessfuly.".format(
                options[0], options[1])





