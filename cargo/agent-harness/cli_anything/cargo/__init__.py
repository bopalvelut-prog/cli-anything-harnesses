import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cargo running')
@cli.command()
def start(): click.echo('cargo started')
if __name__ == '__main__': cli()
