import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quick running')
@cli.command()
def start(): click.echo('quick started')
if __name__ == '__main__': cli()
