import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kitty running')
@cli.command()
def start(): click.echo('kitty started')
if __name__ == '__main__': cli()
