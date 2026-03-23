import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('form running')
@cli.command()
def start(): click.echo('form started')
if __name__ == '__main__': cli()
