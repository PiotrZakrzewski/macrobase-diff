from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
import click
from pandas import DataFrame, read_csv
import sqlite3


ESC_SEQUENCE = '.quit'

@click.command()
@click.argument("data", type=click.Path(exists=True))
def mb_sql(data):
    df = read_csv(data)
    conn = sqlite3.connect(':memory:')
    df.to_sql("data", conn)
    c = conn.cursor()
    session = PromptSession(lexer=PygmentsLexer(SqlLexer))
    print("""Your csv is loaded as table 'data'.
Type in DIFF query on columns you are interested in.
enter .quit to exit""")
    while True:
        try:
            cmd = session.prompt('sql> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            if cmd == ESC_SEQUENCE:
                break
            try:
                c.execute(cmd)
                for r in c.fetchall():
                    print(r)
            except:
                print("Invalid command")


if __name__ == "__main__":
    mb_sql()
