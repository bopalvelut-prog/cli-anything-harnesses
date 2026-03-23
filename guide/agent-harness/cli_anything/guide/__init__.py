import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guide running')
@cli.command()
def start(): click.echo('guide started')
if __name__ == '__main__': cli()
