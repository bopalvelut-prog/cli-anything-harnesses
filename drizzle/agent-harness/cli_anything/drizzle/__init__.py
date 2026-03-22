import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def generate(): subprocess.run(['drizzle-kit', 'generate'])
@cli.command()
def push(): subprocess.run(['drizzle-kit', 'push'])
if __name__ == '__main__': cli()
