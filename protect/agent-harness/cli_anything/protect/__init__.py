import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('protect running')
@cli.command()
def start(): click.echo('protect started')
if __name__ == '__main__': cli()
