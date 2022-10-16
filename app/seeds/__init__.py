from flask.cli import AppGroup
from .users import seed_users, undo_users
from .biz import seed_all_data_sans_users, undo_all_data_sans_users
# from .types import seed_types, undo_types
# from .transactions import seed_transactions, undo_transations

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    # seed_types()
    # seed_transactions()
    seed_all_data_sans_users()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # undo_types()
    # undo_transations()
    undo_all_data_sans_users()
    # Add other undo functions here
