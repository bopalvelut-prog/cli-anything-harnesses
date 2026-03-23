import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chatops running')
@cli.command()
def start(): click.echo('chatops started')
if __name__ == '__main__': cli()
