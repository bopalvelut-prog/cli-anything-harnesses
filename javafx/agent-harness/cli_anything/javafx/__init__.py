import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('javafx running')
@cli.command()
def start(): click.echo('javafx started')
if __name__ == '__main__': cli()
