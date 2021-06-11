from abc import ABCMeta, abstractmethod


class AbstractTuringMachine(metaclass=ABCMeta):

    @abstractmethod
    def move_tape(self, order):
        pass

    @abstractmethod
    @property
    def is_end(self, state):
        pass

    @abstractmethod
    @property
    def is_start(self):
        pass

    @abstractmethod
    def action(self, state):
        pass
# s0 = <,>,|; 1,3,4 ; 1,3,4:s1, 4,2,1: s2, 1,5,5:s2
# State structure: 's0' : {[1, #, #, ...]: ['s1', [L, R, N, ...], [1, #, 4, _, ...]],
# [#, #, #, ...]:['s2',[<, >, |, ...], [1, #, 4, _, ...]], ...}
# state[0] - state name
# state[1] - the dictionary of possible next states, if the read (focused) values correspond to one of the dictionary
# keys, according state is chosen, additionally each of the transitions to a new state (or the same one) is met with
# specific movement of the tape which is written in the dictionary value on the second element of the list


class TuringMachine(AbstractTuringMachine):
    def __init__(self, input, tapes_num, **kwargs):
        self.starting_tape = input
        self.tapes = []
        self.focused_cells = []
        for tape_index in range(0, tapes_num):
            self.tapes.append(['#'])
            self.focused_cells.append(0)
            if tape_index == 0:
                self.tapes.extend(list(input))
        self.state_dict = {}
        self.initial_state = 0
        self.final_states = []
        self.file_name = ''
        for key, value in kwargs:
            if key == 'filename':
                self.file_name = value

    def move_tape(self, order):
        tape_index = 0
        for move in order:
            if move == 'L':
                if self.focused_cells[tape_index] == 0:
                    self.tapes[tape_index].insert(0, '#')
                else:
                    self.focused_cells[tape_index] -= 1
            elif move == 'R':
                if self.focused_cells[tape_index] == len(self.tapes[tape_index])-1:
                    self.tapes[tape_index].append('#')

                self.focused_cells[tape_index] += 1
            else:
                pass

    def is_end(self, state):
        if state in self.final_states:
            return True
        else:
            return False

    def is_start(self):
        pass

    def action(self, state):
        if self.is_end(state):
            return 1
        else:
            transition = state[1].get(self.get_focused())
            if transition == None:
                transition = state[1].get('default')
            next_state = transition[0]
            tape_index = 0
            for value in transition[2]:
                if value == '_':
                    pass
                else:
                    self.tapes[tape_index][self.focused_cells[tape_index]] = value
                tape_index += 1
            self.move_tape(transition[1])
            self.action(self.state_dict[next_state])

    def get_focused(self):
        focused_values = []
        tape_index = 0
        for cell in self.focused_cells:
            focused_values.append(self.tapes[tape_index][cell])
        return focused_values

    def print_data(self):
        pass

    def add_state(self, state_name):
        self.state_dict.update({state_name: {}})

    def add_transition(self, state_name, transition):
        self.state_dict.update({state_name: {transition}})

    """def read_code(self):
        if self.file_name:
            file = open(self.file_name, 'r')
            for line in file:
                if line == "^initial state":
                    line.replace(" ", "")
                    equal_sign_list = line.split("=")
                    self.initial_state = equal_sign_list[1]
                if line == "^final state":
                    line.replace(" ", "")
                    equal_sign_list = line.split("=")
                    self.final_states = equal_sign_list[1].split(",")
                if line == "^[]"
    """



                    # s0 = <,>,|; 1,3,4 ; 1,3,4:s1, 4,2,1: s2, 1,5,5:s2



turing = TuringMachine("124+12356j+131+123j", 3)
turing.add_state("start")
turing.add_transition("start", {"default":["move to end", ['R', 'N', 'N'], ['_', '_', '_']]})

