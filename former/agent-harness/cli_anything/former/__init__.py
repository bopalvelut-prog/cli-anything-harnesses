import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('former running')
@cli.command()
def start(): click.echo('former started')
if __name__ == '__main__': cli()
