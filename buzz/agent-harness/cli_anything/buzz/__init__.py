import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buzz running')
@cli.command()
def start(): click.echo('buzz started')
if __name__ == '__main__': cli()
