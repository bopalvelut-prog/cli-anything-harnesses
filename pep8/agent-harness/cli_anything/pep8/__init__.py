import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pep8 running')
@cli.command()
def start(): click.echo('pep8 started')
if __name__ == '__main__': cli()
