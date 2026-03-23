import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weekly running')
@cli.command()
def start(): click.echo('weekly started')
if __name__ == '__main__': cli()
