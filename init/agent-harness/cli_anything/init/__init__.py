import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('init running')
@cli.command()
def start(): click.echo('init started')
if __name__ == '__main__': cli()
