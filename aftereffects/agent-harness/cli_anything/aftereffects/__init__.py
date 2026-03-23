import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aftereffects running')
@cli.command()
def start(): click.echo('aftereffects started')
if __name__ == '__main__': cli()
