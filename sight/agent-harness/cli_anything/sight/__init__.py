import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sight running')
@cli.command()
def start(): click.echo('sight started')
if __name__ == '__main__': cli()
