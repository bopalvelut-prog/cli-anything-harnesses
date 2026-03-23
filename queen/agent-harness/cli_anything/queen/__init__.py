import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('queen running')
@cli.command()
def start(): click.echo('queen started')
if __name__ == '__main__': cli()
