import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('together running')
@cli.command()
def start(): click.echo('together started')
if __name__ == '__main__': cli()
