import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grasp running')
@cli.command()
def start(): click.echo('grasp started')
if __name__ == '__main__': cli()
