import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('totally running')
@cli.command()
def start(): click.echo('totally started')
if __name__ == '__main__': cli()
