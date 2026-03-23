import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('railroad running')
@cli.command()
def start(): click.echo('railroad started')
if __name__ == '__main__': cli()
