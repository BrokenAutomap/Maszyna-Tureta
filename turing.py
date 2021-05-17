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
# State structure: [s0, [<, >, |, ...], [1, #, 4, _, ...], {[1, #, #, ...]: 's1', [#, #, #, ...]:'s2', ...}]
# state[0] - state name
# state[1] - the list of tape movements, if first sign is < then it moves the first tape to the left and so on
# state[2] - the list of signs being placed at each tape, in the example above 4 is being placed on the third tape
# the '_' means that nothing is changed and the '#' is a blank cell
# state[3] - the dictionary of possible next states, if the read (focused) values correspond to one of the dictionary
# keys, according state is chosen


class TuringMachine(AbstractTuringMachine):
    def __init__(self, input, tapes_num):
        super().__init__()
        self.starting_tape = input
        self.tapes = []
        self.focused_cells = []
        for tape_index in range(0, tapes_num):
            self.tapes.append(['#'])
            self.focused_cells.append(0)
            if tape_index == 0:
                self.tapes[0] = input
        self.state_list = []
        self.initial_state = 0
        self.final_states = []

    def move_tape(self, order):
        tape_index = 0
        for move in order:
            if move == '<':
                if self.focused_cells[tape_index] == 0:
                    self.tapes[tape_index].insert(0, '#')
                else:
                    self.focused_cells[tape_index] -= 1
            elif move == '>':
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
            next_state = state[3].get(self.get_focused())
            tape_index = 0
            for value in state[2]:
                if value == '_':
                    pass
                else:
                    self.state_list[tape_index][2][tape_index] = value
                tape_index += 1
            self.move_tape(state[1])
            self.action(next_state)

    def get_focused(self):
        focused_values = []
        tape_index = 0
        for cell in self.focused_cells:
            focused_values.append(self.tapes[tape_index][cell])
        return focused_values

    def print_data(self):
        pass

    def add_state(self, state):
        self.state_list.append(state)


