import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sport running')
@cli.command()
def start(): click.echo('sport started')
if __name__ == '__main__': cli()
