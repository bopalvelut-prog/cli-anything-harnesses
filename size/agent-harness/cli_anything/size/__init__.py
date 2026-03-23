import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('size running')
@cli.command()
def start(): click.echo('size started')
if __name__ == '__main__': cli()
