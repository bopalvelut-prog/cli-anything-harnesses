import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plymouth running')
@cli.command()
def start(): click.echo('plymouth started')
if __name__ == '__main__': cli()
