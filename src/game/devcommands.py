class Devcommands:
    def __init__(self, command="game_init"):
        self.commands = self.initialize()
        if command != "game_init":
            if command == "mode":
                self.change_mode()
            elif command == "url":
                self.change_url()
            elif command == "reset":
                self.reset_devcommands()

    def initialize(self):
        commands_dict = {}
        with open("src/game/devcommands.txt", "r") as file: #pylint: disable=unspecified-encoding
            file = file.read().split("\n")
            for item in file:
                if item == "":
                    break
                item = item.split(";")
                commands_dict[item[0]] = item[1]

        return commands_dict

    def offline_or_online(self):
        return self.commands["mode"]

    def return_map_url(self):
        return self.commands["url"]

    def change_mode(self):
        mode = ""
        while mode not in ["online", "offline"]:
            mode = input(
                "Which mode do you want the game in? Type 'online' or 'offline': ")
        self.commands["mode"] = mode
        self.write_file()
        print("Game mode is now set online.")

    def change_url(self):
        url = input("Paste the Google Drive url you want to use in-game: ")
        url_ok = self.test_url(url)
        if not url_ok:
            print("The link provided is not in proper format. No changes done.")
        else:
            self.commands["url"] = url
            self.write_file()
            print(f"Map url is now set to: {url}.")

    def test_url(self, url: str):
        if "https://" not in url:
            return False
        if "drive.google.com" not in url:
            return False
        if "view?" not in url:
            return False
        if "share_link" not in url:
            return False
        return True

    def write_file(self):
        with open("src/game/devcommands.txt", "w") as file: #pylint: disable=unspecified-encoding
            for key, value in self.commands.items():
                file.write(f"{key};{value}\n")

    def reset_devcommands(self):
        self.commands["mode"] = "offline"
        self.commands["url"] = "https://drive.google.com/file/d/1ZsHfubrB7LQwKMvhbGr_UNvfk_GHJcix/view?usp=share_link" # pylint: disable=line-too-long
        with open("src/game/devcommands.txt", "w") as file: #pylint: disable=unspecified-encoding
            for key, value in self.commands.items():
                file.write(f"{key};{value}\n")
        print("The settings are now reset to default values.")

# This is only triggered when running the code directly.
if __name__ == "__main__":
    print("Greetings overlord, what do you want to do?")
    print("Type 'mode' to alter game mode.")
    print("Type 'url' to alter the download link for level map.")
    print("Type 'reset' if you want to reset to default settings.")
    print("Type anything else if you changed your mind and want to go back.")
    dev_input = input("Greetings underling, I want to: ")
    if dev_input in ['mode', 'url', 'reset']:
        dev = Devcommands(dev_input)
    else:
        print("Very well.")
