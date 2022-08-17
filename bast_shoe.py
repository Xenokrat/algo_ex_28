def BastShoe(command: str) -> str:
    global current_str
    if not isinstance(command, str):
        return current_str
    parsed_command = parse_command(command)
    command_no = parsed_command[0]
    operations = {
        1: addition,
        2: deletion,
        3: index,
        4: undo,
        5: redo
    }
    if command_no not in operations:
        return current_str

    func = operations[command_no]
    res = func(*parsed_command)
    return res


def parse_command(command: str) -> tuple:
    op_num = int(command[0])
    if len(command) > 1:
        arg = command[2:]
        return op_num, arg
    else:
        return op_num,


def addition(*args):
    global current_str
    global list_of_operations
    global current_index

    # check for valid second argument
    if len(args) != 2:
        return current_str

    # clear list of operations if edit after undo
    if current_index != len(list_of_operations) - 1:
        list_of_operations = [list_of_operations[current_index]]
        current_index = 0

    new_text = args[1]
    new_str = current_str + new_text
    current_str = new_str

    list_of_operations.append(new_str)
    current_index += 1

    return new_str


def deletion(*args):
    global current_str
    global list_of_operations
    global current_index

    # check for valid second argument
    if len(args) != 2:
        return current_str
    try:
        deletion_count = int(args[1])
    except ValueError:
        return current_str

    # clear list of operations if edit after undo
    if current_index != len(list_of_operations) - 1:
        list_of_operations = [list_of_operations[current_index]]
        current_index = 0

    new_str = current_str[:-deletion_count]
    current_str = new_str

    list_of_operations.append(new_str)
    current_index += 1

    return new_str


def index(*args):
    if len(args) != 2:
        return current_str
    ind = int(args[1])
    if 0 <= ind < len(current_str):
        return current_str[ind]
    else:
        return ''


def undo(*args):
    global current_str
    global list_of_operations
    global current_index

    if current_index <= 0:
        return current_str

    current_index -= 1
    current_str = list_of_operations[current_index]

    return current_str


def redo(*args):
    global current_str
    global list_of_operations
    global current_index

    if current_index >= len(list_of_operations) - 1:
        return current_str

    current_index += 1
    current_str = list_of_operations[current_index]

    return current_str


current_str = ''
current_index = 0
list_of_operations = ['']
