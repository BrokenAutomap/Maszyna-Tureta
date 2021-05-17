def read_code(self, path):
    code = open(path, "r")
    line = "a"
    line_index = 0
    while line != '':
        line = code.readline()
        line_index += 1
        if line == "^initial state":
            pass
        elif line == "^final state":
            pass
        elif line == "^#+":
            pass
        else:
            definition = line.split('=')
            definition[0].strip()
            if definition[0] == "^[a-zA-Z0-9_]+$":
                self.state_list[len(self.state_list) - 1][0] = definition[0]
            else:
                error_message = "Invalid state name at line: {} (state names can consist only of " \
                                "upper and lowercase letters, numbers and underscores".format(line_index)
                raise NameError(error_message)

            definition_data = definition[1].split(";")
            definition_data[0].replace(" ", "")
            tape_movement_list = definition_data[0].split(",")
            for value in tape_movement_list:
                if value != "^[<>|]$":
                    error_message = "Invalid tape movement indicator at line: {} " \
                                    "(only <, >, or | allowed)".format(line_index)
                    raise Exception(error_message)
            self.state_list[len(self.state_list) - 1][1] = tape_movement_list

            definition_data[1].replace(" ", "")
            replacement_list = definition_data[1].split(",")
            for value in replacement_list:
                if value == "":
                    error_message = "Invalid replacement character at line: {} " \
                                    "(can't be a whitespace)".format(line_index)
                    raise Exception(error_message)
            self.state_list[len(self.state_list) - 1][2] = replacement_list

            definition_data[2].replace(" ", "")
            state_transitions_list = definition_data[2].split(",")
            for state_transition in state_transitions_list:
                key_value = state_transition.split(":")
                key_value[0]