import click
from .interpreter import SamInterpreter

@click.group()
def cli():
    """Sam Programming Language CLI"""
    pass

@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def run(filename):
    """Run a Sam source file"""
    interpreter = SamInterpreter()
    interpreter.run_file(filename)

@cli.command()
def shell():
    """Start the interactive Sam shell"""
    interpreter = SamInterpreter()
    interpreter.run_shell()

def main():
    cli()

if __name__ == '__main__':
    main()
