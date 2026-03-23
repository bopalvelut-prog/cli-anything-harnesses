import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slice running')
@cli.command()
def start(): click.echo('slice started')
if __name__ == '__main__': cli()
