import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('garlic running')
@cli.command()
def start(): click.echo('garlic started')
if __name__ == '__main__': cli()
