import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('replace running')
@cli.command()
def start(): click.echo('replace started')
if __name__ == '__main__': cli()
