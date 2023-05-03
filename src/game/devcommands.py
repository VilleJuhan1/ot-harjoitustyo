class Devcommands:
    """ Used as a developer tool to test different things.

    Attributes:
        file = The .txt-file where the dev parameters are stored.
        commands = Parameters saved to a dictionary.
    """

    def __init__(self, command="game_init", file_path="src/game/devcommands.txt"):
        """ The constructor

        Args:
            command (str, optional): Used to differentiate function calls made by dev and game.
            file_path (str, optional): The file where necessary info is stored. 
                                       Defaults to "src/game/devcommands.txt".
        """
        self.file = file_path
        self.commands = self.initialize()
        if command != "game_init":
            if command == "mode":
                self.change_mode()
            elif command == "url":
                self.change_url()
            elif command == "reset":
                self.reset_devcommands()

    def initialize(self):
        """ Used in the constructor. Translates the .txt-file into a dictionary.

        Returns:
            dict: Contains information on game mode and map url.
        """
        commands_dict = {}
        with open(self.file, "r") as file:  # pylint: disable=unspecified-encoding
            file = file.read().split("\n")
            for item in file:
                if item == "":
                    break
                item = item.split(";")
                commands_dict[item[0]] = item[1]

        return commands_dict

    def offline_or_online(self):
        """ Returns the current game mode status.

        Returns:
            str: Is either "online" or "offline".
        """
        return self.commands["mode"]

    def return_map_url(self):
        """ Returns the url of the map.csv-file.

        Returns:
            str: An url-address in string-format.
        """
        return self.commands["url"]

    def change_mode(self):
        """ A dev tool to switch game mode between online and offline.

        """
        mode = ""
        while mode not in ["online", "offline"]:
            mode = input(
                "Which mode do you want the game in? Type 'online' or 'offline': ")
        self.commands["mode"] = mode
        self.write_file()
        print(f"Game mode is now set {mode}.")

    def change_url(self):
        """ A dev tool to switch the url where map.csv-file is loaded from.

        """
        url = input("Paste the Google Drive url you want to use in-game: ")
        url_ok = self.test_url(url)
        if not url_ok:
            print("The link provided is not in proper format. No changes done.")
        else:
            self.commands["url"] = url
            self.write_file()
            print(f"Map url is now set to: {url}.")

    def test_url(self, url: str):
        """ Used in testing whether the url dev provided is a proper one.

        Args:
            url (str): The url-address for loading the map.csv

        Returns:
            bool: Is the address a proper Google Drive address?
        """
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
        """ Writes the changes to a file.

        """
        with open(self.file, "w") as file:  # pylint: disable=unspecified-encoding
            for key, value in self.commands.items():
                file.write(f"{key};{value}\n")

    def reset_devcommands(self):
        """ Resets the game parameters to the default state.

        """
        self.commands["mode"] = "offline"
        self.commands["url"] = "https://drive.google.com/file/d/1ZsHfubrB7LQwKMvhbGr_UNvfk_GHJcix/view?usp=share_link"  # pylint: disable=line-too-long
        with open(self.file, "w") as file:  # pylint: disable=unspecified-encoding
            for key, value in self.commands.items():
                file.write(f"{key};{value}\n")
        print("The settings are now reset to default values.")


# This is only triggered when running the code directly as a dev tool.
if __name__ == "__main__":
    print("Greetings overlord, what do you want to do?")
    print("Type 'mode' to alter game mode.")
    print("Type 'url' to alter the download link for level map.")
    print("Type 'reset' if you want to reset to default settings.")
    print("Type anything else if you changed your mind and want to go back.")
    dev_input = input("Greetings underling, I want to: ")
    if dev_input in ['mode', 'url', 'reset']:
        dev = Devcommands(dev_input, "src/game/devcommands.txt")
    else:
        print("Very well.")
