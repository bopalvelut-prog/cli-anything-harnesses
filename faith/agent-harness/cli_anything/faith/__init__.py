import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('faith running')
@cli.command()
def start(): click.echo('faith started')
if __name__ == '__main__': cli()
