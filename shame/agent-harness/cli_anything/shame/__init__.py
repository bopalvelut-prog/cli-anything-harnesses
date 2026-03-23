import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shame running')
@cli.command()
def start(): click.echo('shame started')
if __name__ == '__main__': cli()
