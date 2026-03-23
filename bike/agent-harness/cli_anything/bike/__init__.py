import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bike running')
@cli.command()
def start(): click.echo('bike started')
if __name__ == '__main__': cli()
