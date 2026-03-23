import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('heart running')
@cli.command()
def start(): click.echo('heart started')
if __name__ == '__main__': cli()
