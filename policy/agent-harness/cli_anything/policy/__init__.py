import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('policy running')
@cli.command()
def start(): click.echo('policy started')
if __name__ == '__main__': cli()
