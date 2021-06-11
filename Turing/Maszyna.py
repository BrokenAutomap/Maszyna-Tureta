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

turing.add_state("addition without reminder")
turing.add_state("upper number ends")
turing.add_state("both numbers end")
turing.add_state("bottom number ends")
turing.add_state("addition finished")

turing.add_transition("addition without reminder", {['0','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {['1','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {['0','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {['2','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['0','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['3','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['0','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['4','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['0','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['5','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['0','5','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['6','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['0','6','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['7','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['0','7','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['8','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['0','8','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['9','0','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {['0','9','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {['1','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['2','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['1','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['3','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['1','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['4','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['1','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['5','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['1','5','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['6','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['1','6','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['7','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['1','7','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['8','1','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {['1','8','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {['2','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['3','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['2','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['4','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['2','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['5','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['2','5','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['6','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['2','6','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['7','2','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {['2','7','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {['3','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['4','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['3','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['5','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['3','5','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['6','3','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {['3','6','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {['4','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['5','4','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {['4','5','#']: ["addition without reminder", ['L','L','L'], ['#','#','9']]})



turing.add_transition("addition without reminder", {['5','5','#']: ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {['6','5','#']: ["addition with reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {['5','6','#']: ["addition with reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {['7','5','#']: ["addition with reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['5','7','#']: ["addition with reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['8','5','#']: ["addition with reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['5','8','#']: ["addition with reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['9','5','#']: ["addition with reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['5','9','#']: ["addition with reminder", ['L','L','L'], ['#','#','4']]})

turing.add_transition("addition without reminder", {['6','6','#']: ["addition with reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['7','6','#']: ["addition with reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['6','7','#']: ["addition with reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['8','6','#']: ["addition with reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['6','8','#']: ["addition with reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['9','6','#']: ["addition with reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['6','9','#']: ["addition with reminder", ['L','L','L'], ['#','#','5']]})

turing.add_transition("addition without reminder", {['7','7','#']: ["addition with reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['8','7','#']: ["addition with reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['7','8','#']: ["addition with reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['9','7','#']: ["addition with reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['7','9','#']: ["addition with reminder", ['L','L','L'], ['#','#','6']]})

turing.add_transition("addition without reminder", {['8','8','#']: ["addition with reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['9','8','#']: ["addition with reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['8','9','#']: ["addition with reminder", ['L','L','L'], ['#','#','7']]})

turing.add_transition("addition without reminder", {['9','9','#']: ["addition with reminder", ['L','L','L'], ['#','#','8']]})



turing.add_transition("addition without reminder", {['+','0','#']: ["upper numbers ends", ['N','L','L'], ['_','#','0']]})
turing.add_transition("addition without reminder", {['+','1','#']: ["upper numbers ends", ['N','L','L'], ['_','#','1']]})
turing.add_transition("addition without reminder", {['+','2','#']: ["upper numbers ends", ['N','L','L'], ['_','#','2']]})
turing.add_transition("addition without reminder", {['+','3','#']: ["upper numbers ends", ['N','L','L'], ['_','#','3']]})
turing.add_transition("addition without reminder", {['+','4','#']: ["upper numbers ends", ['N','L','L'], ['_','#','4']]})
turing.add_transition("addition without reminder", {['+','5','#']: ["upper numbers ends", ['N','L','L'], ['_','#','5']]})
turing.add_transition("addition without reminder", {['+','6','#']: ["upper numbers ends", ['N','L','L'], ['_','#','6']]})
turing.add_transition("addition without reminder", {['+','7','#']: ["upper numbers ends", ['N','L','L'], ['_','#','7']]})
turing.add_transition("addition without reminder", {['+','8','#']: ["upper numbers ends", ['N','L','L'], ['_','#','8']]})
turing.add_transition("addition without reminder", {['+','9','#']: ["upper numbers ends", ['N','L','L'], ['_','#','9']]})



turing.add_transition("addition without reminder", {['+','#','#']: ["both numbers end", ['L','N','L'], ['#','#','+']]})



turing.add_transition("addition without reminder", {['0','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {['1','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {['2','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {['3','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {['4','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {['5','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {['6','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {['7','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {['8','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {['9','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','9']]})



turing.add_transition("upper numbers ends", {['+','#','#']: ["addition finished", ['L','N','L'], ['#','#','+']]})



turing.add_transition("upper numbers ends", {['+','0','#']: ["upper numbers ends", ['N','L','L'], ['+','#','0']]})
turing.add_transition("upper numbers ends", {['+','1','#']: ["upper numbers ends", ['N','L','L'], ['+','#','1']]})
turing.add_transition("upper numbers ends", {['+','2','#']: ["upper numbers ends", ['N','L','L'], ['+','#','2']]})
turing.add_transition("upper numbers ends", {['+','3','#']: ["upper numbers ends", ['N','L','L'], ['+','#','3']]})
turing.add_transition("upper numbers ends", {['+','4','#']: ["upper numbers ends", ['N','L','L'], ['+','#','4']]})
turing.add_transition("upper numbers ends", {['+','5','#']: ["upper numbers ends", ['N','L','L'], ['+','#','5']]})
turing.add_transition("upper numbers ends", {['+','6','#']: ["upper numbers ends", ['N','L','L'], ['+','#','6']]})
turing.add_transition("upper numbers ends", {['+','7','#']: ["upper numbers ends", ['N','L','L'], ['+','#','7']]})
turing.add_transition("upper numbers ends", {['+','8','#']: ["upper numbers ends", ['N','L','L'], ['+','#','8']]})
turing.add_transition("upper numbers ends", {['+','9','#']: ["upper numbers ends", ['N','L','L'], ['+','#','9']]})




turing.add_transition("both numbers end", {['0','#','#']: ["addition finished", ['N','N','N'], ['_','_','_']]})


turing.add_transition("bottom numbers end", {['+','#','#']: ["addition finished", ['L','N','L'], ['#','#','+']]})


turing.add_transition("bottom numbers end", {['0','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','0']]})
turing.add_transition("bottom numbers end", {['1','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','1']]})
turing.add_transition("bottom numbers end", {['2','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','2']]})
turing.add_transition("bottom numbers end", {['3','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','3']]})
turing.add_transition("bottom numbers end", {['4','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','4']]})
turing.add_transition("bottom numbers end", {['5','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','5']]})
turing.add_transition("bottom numbers end", {['6','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','6']]})
turing.add_transition("bottom numbers end", {['7','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','7']]})
turing.add_transition("bottom numbers end", {['8','#','#']: ["bottom numbers end", ['L','N','L'], ['#','#','8']]})



turing.add_transition("start", {['default']: ["move to end", ['R','N','N'], ['_','_','_']]})



turing.add_transition("move to end", {['default']: ["move to end", ['R','N','N'], ['_','_','_']]})


turing.add_transition("move to end", {['#','#','#']: ["copy down", ['L','N','N'], ['_','_','_']]})


turing.add_transition("copy down", {['j','#','#']: ["copy down", ['L','L','N'], ['#','j','_']]})


turing.add_transition("copy down", {['+','#','#']: ["align upper tape", ['L','N','N'], ['#','#','#']]})


turing.add_transition("align upper tape", {['default']: ["align upper tape", ['L','N','N'], ['_','_','_']]})


turing.add_transition("align upper tape", {['j','#','_']: ["align middle tape", ['N','R','N'], ['_','_','_']]})


turing.add_transition("align middle tape", {['default']: ["align middle tape", ['N','R','N'], ['_','_','_']]})


turing.add_transition("align middle tape", {['j','j','#']: ["addition without reminder", ['L','L','N'], ['#','#','j']]})