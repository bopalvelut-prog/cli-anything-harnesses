import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('myth running')
@cli.command()
def start(): click.echo('myth started')
if __name__ == '__main__': cli()
