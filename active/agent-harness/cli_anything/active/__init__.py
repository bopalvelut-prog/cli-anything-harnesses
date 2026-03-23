import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('active running')
@cli.command()
def start(): click.echo('active started')
if __name__ == '__main__': cli()
