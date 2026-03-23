import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('click running')
@cli.command()
def start(): click.echo('click started')
if __name__ == '__main__': cli()
