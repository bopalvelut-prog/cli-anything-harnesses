import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('legend running')
@cli.command()
def start(): click.echo('legend started')
if __name__ == '__main__': cli()
