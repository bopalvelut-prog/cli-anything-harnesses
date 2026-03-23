import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('essential running')
@cli.command()
def start(): click.echo('essential started')
if __name__ == '__main__': cli()
