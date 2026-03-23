import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marry running')
@cli.command()
def start(): click.echo('marry started')
if __name__ == '__main__': cli()
