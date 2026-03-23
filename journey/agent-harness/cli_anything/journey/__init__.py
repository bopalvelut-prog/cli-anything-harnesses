import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('journey running')
@cli.command()
def start(): click.echo('journey started')
if __name__ == '__main__': cli()
