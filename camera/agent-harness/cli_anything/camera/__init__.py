import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('camera running')
@cli.command()
def start(): click.echo('camera started')
if __name__ == '__main__': cli()
