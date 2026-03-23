import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('officer running')
@cli.command()
def start(): click.echo('officer started')
if __name__ == '__main__': cli()
