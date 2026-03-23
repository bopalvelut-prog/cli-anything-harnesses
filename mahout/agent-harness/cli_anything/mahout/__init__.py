import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mahout running')
@cli.command()
def start(): click.echo('mahout started')
if __name__ == '__main__': cli()
