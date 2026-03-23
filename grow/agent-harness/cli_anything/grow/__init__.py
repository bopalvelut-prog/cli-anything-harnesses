import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grow running')
@cli.command()
def start(): click.echo('grow started')
if __name__ == '__main__': cli()
