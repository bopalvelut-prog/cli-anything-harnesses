import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fuel running')
@cli.command()
def start(): click.echo('fuel started')
if __name__ == '__main__': cli()
