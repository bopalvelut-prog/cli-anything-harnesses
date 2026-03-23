import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('within running')
@cli.command()
def start(): click.echo('within started')
if __name__ == '__main__': cli()
