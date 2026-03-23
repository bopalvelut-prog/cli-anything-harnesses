import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('entire running')
@cli.command()
def start(): click.echo('entire started')
if __name__ == '__main__': cli()
