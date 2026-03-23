import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transition running')
@cli.command()
def start(): click.echo('transition started')
if __name__ == '__main__': cli()
