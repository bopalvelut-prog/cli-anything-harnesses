import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transparent running')
@cli.command()
def start(): click.echo('transparent started')
if __name__ == '__main__': cli()
