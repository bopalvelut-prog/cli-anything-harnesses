import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nixops running')
@cli.command()
def start(): click.echo('nixops started')
if __name__ == '__main__': cli()
