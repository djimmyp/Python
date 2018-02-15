# Python program to maintain a to do list with descriptions and due dates.

The program allows the user to add tasks, search for tasks, and delete tasks. The tasks are stored in a text file between runs in order to persist the data.

The program takes a "command" argument as the first argument, followed by additional arguments or options based on the provided command.  Commands can be "add", "search", or "delete". If a command is unsuccessful for any reason, a non-zero status code will be returned. The add command requires two arguments, the description and the due date of the task. The search command requires one argument and has two optional flags, one of them which supports python style regular expressions with -r flag and another which supports searching by upcoming due date with -d flag and a mandatory numeric argument. The delete command requires two arguments, the description and the due date of the task.
