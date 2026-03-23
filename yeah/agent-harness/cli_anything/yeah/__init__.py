import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yeah running')
@cli.command()
def start(): click.echo('yeah started')
if __name__ == '__main__': cli()
