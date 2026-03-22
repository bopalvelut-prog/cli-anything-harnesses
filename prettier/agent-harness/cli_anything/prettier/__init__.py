import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('pattern', default='. ')
def format(pattern): subprocess.run(['prettier', '--write', pattern])
@cli.command()
def check(): subprocess.run(['prettier', '--check', '.'])
if __name__ == '__main__': cli()
