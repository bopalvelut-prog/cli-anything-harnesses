import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('depend running')
@cli.command()
def start(): click.echo('depend started')
if __name__ == '__main__': cli()
