import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.option('-t', '--tracetime', default=1)
def top(tracetime): subprocess.run(['nethogs', '-t', str(tracetime)])
@cli.command()
def current(): click.echo('Bandwidth monitoring')
if __name__ == '__main__': cli()
