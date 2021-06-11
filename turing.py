from abc import ABCMeta, abstractmethod


class AbstractTuringMachine(metaclass=ABCMeta):

    @abstractmethod
    def move_tape(self, order):
        pass

    @abstractmethod
    def is_end(self, state):
        pass

    @abstractmethod
    def is_start(self, state):
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
        self.focused_cells_values = ""
        for tape_index in range(0, tapes_num):
            self.tapes.append(['#'])
            self.focused_cells.append(0)
            if tape_index == 0:
                for character in input:
                    self.tapes[tape_index].append(character)
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
            tape_index += 1

    def is_end(self, state):
        if state in self.final_states:
            return True
        else:
            return False

    def is_start(self, state):
        if state == self.initial_state:
            return True
        else:
            return False

    def action(self, state):
        print("current state: ", end="")
        print(state)
        if self.is_end(state):
            self.print_data()
            return 1
        else:
            current_state_dict = self.state_dict.get(state)
            transition = current_state_dict.get(self.get_focused())

            if transition == None:
                transition = current_state_dict.get('default')
            print("current transition: ", end="")
            print(transition)
            next_state = transition[0]
            tape_index = 0
            for value in transition[2]:
                if value == '_':
                    pass
                else:
                    self.tapes[tape_index][self.focused_cells[tape_index]] = value
                tape_index += 1
            self.move_tape(transition[1])
            self.print_data()
            self.action(next_state)

    def get_focused(self):
        focused_values = ""
        tape_index = 0
        for cell in self.focused_cells:
            focused_values += self.tapes[tape_index][cell]
            tape_index += 1
        return focused_values

    def print_data(self):
        print("------------------------------------------")
        for tape in self.tapes:
            print(tape, end="\n")
        print("------------------------------------------")
        print("focused cells indexes: ", end="")
        print(self.focused_cells)
        print("focused cells values: ", end="")
        print(self.get_focused())

    def add_state(self, state_name):
        if self.state_dict.get(state_name) == None:
            self.state_dict.update({state_name: {}})

    def add_transition(self, state_name, transition):
        chosen_state_dict = self.state_dict.get(state_name)
        if chosen_state_dict == None:
            self.add_state(state_name)
            chosen_state_dict = self.state_dict.get(state_name)
        chosen_state_dict.update(transition)



                    # s0 = <,>,|; 1,3,4 ; 1,3,4:s1, 4,2,1: s2, 1,5,5:s2



turing = TuringMachine("919123+12383j+131+120j", 3)
turing.final_states = ["finish"]
turing.initial_state = "start"
turing.add_transition("start", {"default": ["move to end", ['R', 'N', 'N'], ['_', '_', '_']]})

turing.add_state("start")
turing.add_transition("move to end", {"default":["move to end", ['R', 'N', 'N'], ['_', '_', '_']]})

turing.add_state("addition without reminder")
turing.add_state("upper number ends")
turing.add_state("both numbers end")
turing.add_state("bottom number ends")
turing.add_state("addition finished")

turing.add_transition("addition without reminder", {'00#': ["addition without reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'10#': ["addition without reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {'01#': ["addition without reminder", ['L','L','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {'20#': ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {'02#': ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {'30#': ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {'03#': ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {'40#': ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'04#': ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'50#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'05#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'60#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'06#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'70#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'07#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'80#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'08#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'90#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {'09#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {'11#': ["addition without reminder", ['L','L','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {'21#': ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {'12#': ["addition without reminder", ['L','L','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {'31#': ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'13#': ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'41#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'14#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'51#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'15#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'61#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'16#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'71#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'17#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'81#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {'18#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {'22#': ["addition without reminder", ['L','L','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'32#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'23#': ["addition without reminder", ['L','L','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'42#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'24#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'52#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'25#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'62#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'26#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'72#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {'27#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {'33#': ["addition without reminder", ['L','L','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'43#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'34#': ["addition without reminder", ['L','L','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'53#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'35#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'63#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {'36#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})

turing.add_transition("addition without reminder", {'44#': ["addition without reminder", ['L','L','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'54#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})
turing.add_transition("addition without reminder", {'45#': ["addition without reminder", ['L','L','L'], ['#','#','9']]})



turing.add_transition("addition without reminder", {'19#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'28#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'29#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'37#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'38#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'39#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'46#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'47#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'48#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'49#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'55#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'56#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'57#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'58#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'59#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'64#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'65#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'66#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'67#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'68#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'69#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'73#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'74#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'75#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'76#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'77#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'78#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'79#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'82#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'83#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'84#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'85#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'86#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'87#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'88#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'89#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'91#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'92#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'93#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'94#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'95#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'96#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'97#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'98#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'99#': ["addition with reminder", ['L','L','L'], ['#','#','0']]})




turing.add_transition("addition without reminder", {'+0#': ["upper number ends", ['N','L','L'], ['_','#','0']]})
turing.add_transition("addition without reminder", {'+1#': ["upper number ends", ['N','L','L'], ['_','#','1']]})
turing.add_transition("addition without reminder", {'+2#': ["upper number ends", ['N','L','L'], ['_','#','2']]})
turing.add_transition("addition without reminder", {'+3#': ["upper number ends", ['N','L','L'], ['_','#','3']]})
turing.add_transition("addition without reminder", {'+4#': ["upper number ends", ['N','L','L'], ['_','#','4']]})
turing.add_transition("addition without reminder", {'+5#': ["upper number ends", ['N','L','L'], ['_','#','5']]})
turing.add_transition("addition without reminder", {'+6#': ["upper number ends", ['N','L','L'], ['_','#','6']]})
turing.add_transition("addition without reminder", {'+7#': ["upper number ends", ['N','L','L'], ['_','#','7']]})
turing.add_transition("addition without reminder", {'+8#': ["upper number ends", ['N','L','L'], ['_','#','8']]})
turing.add_transition("addition without reminder", {'+9#': ["upper number ends", ['N','L','L'], ['_','#','9']]})



turing.add_transition("addition without reminder", {'+##': ["both numbers end", ['L','N','L'], ['#','#','+']]})



turing.add_transition("addition without reminder", {'0##': ["bottom number ends", ['L','N','L'], ['#','#','0']]})
turing.add_transition("addition without reminder", {'1##': ["bottom number ends", ['L','N','L'], ['#','#','1']]})
turing.add_transition("addition without reminder", {'2##': ["bottom number ends", ['L','N','L'], ['#','#','2']]})
turing.add_transition("addition without reminder", {'3##': ["bottom number ends", ['L','N','L'], ['#','#','3']]})
turing.add_transition("addition without reminder", {'4##': ["bottom number ends", ['L','N','L'], ['#','#','4']]})
turing.add_transition("addition without reminder", {'5##': ["bottom number ends", ['L','N','L'], ['#','#','5']]})
turing.add_transition("addition without reminder", {'6##': ["bottom number ends", ['L','N','L'], ['#','#','6']]})
turing.add_transition("addition without reminder", {'7##': ["bottom number ends", ['L','N','L'], ['#','#','7']]})
turing.add_transition("addition without reminder", {'8##': ["bottom number ends", ['L','N','L'], ['#','#','8']]})
turing.add_transition("addition without reminder", {'9##': ["bottom number ends", ['L','N','L'], ['#','#','9']]})



turing.add_transition("upper number ends", {'+##': ["addition finished", ['L','N','L'], ['#','#','+']]})



turing.add_transition("upper number ends", {'+0#': ["upper number ends", ['N','L','L'], ['+','#','0']]})
turing.add_transition("upper number ends", {'+1#': ["upper number ends", ['N','L','L'], ['+','#','1']]})
turing.add_transition("upper number ends", {'+2#': ["upper number ends", ['N','L','L'], ['+','#','2']]})
turing.add_transition("upper number ends", {'+3#': ["upper number ends", ['N','L','L'], ['+','#','3']]})
turing.add_transition("upper number ends", {'+4#': ["upper number ends", ['N','L','L'], ['+','#','4']]})
turing.add_transition("upper number ends", {'+5#': ["upper number ends", ['N','L','L'], ['+','#','5']]})
turing.add_transition("upper number ends", {'+6#': ["upper number ends", ['N','L','L'], ['+','#','6']]})
turing.add_transition("upper number ends", {'+7#': ["upper number ends", ['N','L','L'], ['+','#','7']]})
turing.add_transition("upper number ends", {'+8#': ["upper number ends", ['N','L','L'], ['+','#','8']]})
turing.add_transition("upper number ends", {'+9#': ["upper number ends", ['N','L','L'], ['+','#','9']]})




turing.add_transition("both numbers end", {'###': ["addition finished", ['N','N','N'], ['_','_','_']]})


turing.add_transition("bottom number ends", {'+##': ["addition finished", ['L','N','L'], ['#','#','+']]})


turing.add_transition("bottom number ends", {'0##': ["bottom number ends", ['L','N','L'], ['#','#','0']]})
turing.add_transition("bottom number ends", {'1##': ["bottom number ends", ['L','N','L'], ['#','#','1']]})
turing.add_transition("bottom number ends", {'2##': ["bottom number ends", ['L','N','L'], ['#','#','2']]})
turing.add_transition("bottom number ends", {'3##': ["bottom number ends", ['L','N','L'], ['#','#','3']]})
turing.add_transition("bottom number ends", {'4##': ["bottom number ends", ['L','N','L'], ['#','#','4']]})
turing.add_transition("bottom number ends", {'5##': ["bottom number ends", ['L','N','L'], ['#','#','5']]})
turing.add_transition("bottom number ends", {'6##': ["bottom number ends", ['L','N','L'], ['#','#','6']]})
turing.add_transition("bottom number ends", {'7##': ["bottom number ends", ['L','N','L'], ['#','#','7']]})
turing.add_transition("bottom number ends", {'8##': ["bottom number ends", ['L','N','L'], ['#','#','8']]})



turing.add_transition("start", {'default': ["move to end", ['R','N','N'], ['_','_','_']]})



turing.add_transition("move to end", {'default': ["move to end", ['R','N','N'], ['_','_','_']]})


turing.add_transition("move to end", {'###': ["copy down", ['L','N','N'], ['_','_','_']]})

turing.add_transition("copy down", {'j##': ["copy down", ['L','L','N'], ['#','j','_']]})
turing.add_transition("copy down", {'0##': ["copy down", ['L','L','N'], ['#','0','_']]})
turing.add_transition("copy down", {'1##': ["copy down", ['L','L','N'], ['#','1','_']]})
turing.add_transition("copy down", {'2##': ["copy down", ['L','L','N'], ['#','2','_']]})
turing.add_transition("copy down", {'3##': ["copy down", ['L','L','N'], ['#','3','_']]})
turing.add_transition("copy down", {'4##': ["copy down", ['L','L','N'], ['#','4','_']]})
turing.add_transition("copy down", {'5##': ["copy down", ['L','L','N'], ['#','5','_']]})
turing.add_transition("copy down", {'6##': ["copy down", ['L','L','N'], ['#','6','_']]})
turing.add_transition("copy down", {'7##': ["copy down", ['L','L','N'], ['#','7','_']]})
turing.add_transition("copy down", {'8##': ["copy down", ['L','L','N'], ['#','8','_']]})
turing.add_transition("copy down", {'9##': ["copy down", ['L','L','N'], ['#','9','_']]})



turing.add_transition("copy down", {'+##': ["align upper tape", ['L','N','N'], ['#','#','#']]})


turing.add_transition("align upper tape", {'default': ["align upper tape", ['L','N','N'], ['_','_','_']]})


turing.add_transition("align upper tape", {'j##': ["align middle tape", ['N','R','N'], ['_','_','_']]})


turing.add_transition("align middle tape", {'default': ["align middle tape", ['N','R','N'], ['_','_','_']]})


turing.add_transition("align middle tape", {'jj#': ["addition without reminder", ['L','L','L'], ['#','#','j']]})

turing.add_state("addition with reminder")
turing.add_state("upper number ends (reminder)")
turing.add_state("both numbers end (reminder)")
turing.add_state("bottom number ends (reminder")

turing.add_transition("addition with reminder", {'19#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'28#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'29#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'37#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'38#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'39#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'46#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'47#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'48#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'49#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'55#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'56#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'57#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'58#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'59#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'64#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'65#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'66#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'67#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'68#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'69#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'73#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'74#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'75#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'76#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'77#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'78#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'79#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'82#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'83#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'84#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'85#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'86#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'87#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'88#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'89#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'91#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'92#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'93#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'94#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'95#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'96#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'97#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'98#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'99#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '9']]})

turing.add_transition("addition with reminder", {'09#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'08#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'07#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'06#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'05#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'04#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'03#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'02#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'01#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'00#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'18#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'17#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'16#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'15#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'14#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'13#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'12#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'11#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'10#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'27#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'26#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'25#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'24#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'23#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'22#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'21#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'20#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'36#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'35#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'34#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'33#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'32#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'31#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'30#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'45#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'44#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'43#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'42#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'41#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'40#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'54#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'53#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'52#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'51#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'50#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'63#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'62#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'61#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'60#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'72#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'71#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'70#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'81#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})
turing.add_transition("addition with reminder", {'80#': ["addition without reminder", ['L', 'L', 'L'], ['#', '#', '9']]})
turing.add_transition("addition with reminder", {'90#': ["addition with reminder", ['L', 'L', 'L'], ['#', '#', '0']]})

turing.add_transition("addition with reminder", {'+9#': ["upper number ends (reminder)", ['N', 'L', 'L'], ['_', '#', '0']]})

turing.add_transition("addition with reminder", {'+##': ["both numbers end (reminder)", ['N', 'N', 'L'], ['#', '#', '1']]})

turing.add_transition("addition with reminder", {'9##': ["bottom number ends (reminder)", ['L', 'N', 'L'], ['#', '#', '1']]})

turing.add_transition("addition with reminder", {'0##': ["bottom number ends", ['L', 'N',  'L'], ['#', '#', '1']]})
turing.add_transition("addition with reminder", {'1##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '2']]})
turing.add_transition("addition with reminder", {'2##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '3']]})
turing.add_transition("addition with reminder", {'3##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '4']]})
turing.add_transition("addition with reminder", {'4##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '5']]})
turing.add_transition("addition with reminder", {'5##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '6']]})
turing.add_transition("addition with reminder", {'6##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '7']]})
turing.add_transition("addition with reminder", {'7##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '8']]})
turing.add_transition("addition with reminder", {'8##': ["bottom number ends", ['L', 'N', 'L'], ['#', '#', '9']]})

turing.add_transition("addition with reminder", {'+0#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '1']]})
turing.add_transition("addition with reminder", {'+1#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '2']]})
turing.add_transition("addition with reminder", {'+2#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '3']]})
turing.add_transition("addition with reminder", {'+3#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '4']]})
turing.add_transition("addition with reminder", {'+4#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '5']]})
turing.add_transition("addition with reminder", {'+5#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '6']]})
turing.add_transition("addition with reminder", {'+6#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '7']]})
turing.add_transition("addition with reminder", {'+7#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '8']]})
turing.add_transition("addition with reminder", {'+8#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '9']]})

turing.add_transition("upper number ends (reminder)", {'+9#': ["upper number ends (reminder)", ['N', 'L', 'L'], ['+', '#', '0']]})

turing.add_transition("upper number ends (reminder)", {'+0#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '1']]})
turing.add_transition("upper number ends (reminder)", {'+1#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '2']]})
turing.add_transition("upper number ends (reminder)", {'+2#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '3']]})
turing.add_transition("upper number ends (reminder)", {'+3#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '4']]})
turing.add_transition("upper number ends (reminder)", {'+4#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '5']]})
turing.add_transition("upper number ends (reminder)", {'+5#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '6']]})
turing.add_transition("upper number ends (reminder)", {'+6#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '7']]})
turing.add_transition("upper number ends (reminder)", {'+7#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '8']]})
turing.add_transition("upper number ends (reminder)", {'+8#': ["upper number ends", ['N', 'L', 'L'], ['+', '#', '9']]})

turing.add_transition("upper number ends (reminder)", {'+##': ["addition finished", ['L', 'N', 'L'], ['#', '#', '+']]})

turing.add_transition("both numbers end (reminder)", {'###': ["addition finished", ['L', 'N', 'L'], ['#', '#', '+']]})

turing.add_transition("bottom number ends (reminder)", {'+##': ["addition finished", ['L', 'N', 'L'], ['#', '#', '+']]})

turing.add_state("addition finished")
turing.add_state("check if anything left to add")
turing.add_state("copy down real")
turing.add_state("find upper real")
turing.add_state("align upper real")
turing.add_state("align down real")

turing.add_transition("addition finished", {"default": ["check if anything left to add", ['N', 'N', 'N'], ['_', '_', '_']]})

turing.add_transition("check if anything left to add", {'0##': ["copy down real", ['L', 'L', 'N'], ['#', '0', '#']]})
turing.add_transition("check if anything left to add", {'1##': ["copy down real", ['L', 'L', 'N'], ['#', '1', '#']]})
turing.add_transition("check if anything left to add", {'2##': ["copy down real", ['L', 'L', 'N'], ['#', '2', '#']]})
turing.add_transition("check if anything left to add", {'3##': ["copy down real", ['L', 'L', 'N'], ['#', '3', '#']]})
turing.add_transition("check if anything left to add", {'4##': ["copy down real", ['L', 'L', 'N'], ['#', '4', '#']]})
turing.add_transition("check if anything left to add", {'5##': ["copy down real", ['L', 'L', 'N'], ['#', '5', '#']]})
turing.add_transition("check if anything left to add", {'6##': ["copy down real", ['L', 'L', 'N'], ['#', '6', '#']]})
turing.add_transition("check if anything left to add", {'7##': ["copy down real", ['L', 'L', 'N'], ['#', '7', '#']]})
turing.add_transition("check if anything left to add", {'8##': ["copy down real", ['L', 'L', 'N'], ['#', '8', '#']]})
turing.add_transition("check if anything left to add", {'9##': ["copy down real", ['L', 'L', 'N'], ['#', '9', '#']]})

turing.add_transition("copy down real", {'0##': ["copy down real", ['L', 'L', 'N'], ['#', '0', '#']]})
turing.add_transition("copy down real", {'1##': ["copy down real", ['L', 'L', 'N'], ['#', '1', '#']]})
turing.add_transition("copy down real", {'2##': ["copy down real", ['L', 'L', 'N'], ['#', '2', '#']]})
turing.add_transition("copy down real", {'3##': ["copy down real", ['L', 'L', 'N'], ['#', '3', '#']]})
turing.add_transition("copy down real", {'4##': ["copy down real", ['L', 'L', 'N'], ['#', '4', '#']]})
turing.add_transition("copy down real", {'5##': ["copy down real", ['L', 'L', 'N'], ['#', '5', '#']]})
turing.add_transition("copy down real", {'6##': ["copy down real", ['L', 'L', 'N'], ['#', '6', '#']]})
turing.add_transition("copy down real", {'7##': ["copy down real", ['L', 'L', 'N'], ['#', '7', '#']]})
turing.add_transition("copy down real", {'8##': ["copy down real", ['L', 'L', 'N'], ['#', '8', '#']]})
turing.add_transition("copy down real", {'9##': ["copy down real", ['L', 'L', 'N'], ['#', '9', '#']]})

turing.add_transition("copy down real", {'###': ["find upper real", ['R', 'N', 'N'], ['#', '+', '#']]})

turing.add_transition("find upper real", {'#+#': ["find upper real", ['R', 'N', 'N'], ['#', '_', '#']]})

turing.add_transition("find upper real", {"default": ["align upper real", ['R', 'N', 'N'], ['_', '_', '_']]})

turing.add_transition("align upper real", {"default": ["align upper real", ['R', 'N', 'N'], ['_', '_', '_']]})

turing.add_transition("align upper real", {'#+#': ["align down real", ['N', 'R', 'N'], ['_', '#', '_']]})

turing.add_transition("align down real", {"default": ["align down real", ['N', 'R', 'N'], ['_', '_', '_']]})

turing.add_transition("align down real", {'###': ["addition without reminder", ['L', 'L', 'N'], ['_', '_', '_']]})

turing.add_state("delete plus")

turing.add_transition("check if anything left to add", {'###': ["delete plus", ['N', 'N', 'R'], ['#', '#', '#']]})

turing.add_state("finish")

turing.add_transition("delete plus", {'##+': ["finish", ['N', 'N', 'N'], ['#', '#', '#']]})

turing.action("start")
