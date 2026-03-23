import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('series running')
@cli.command()
def start(): click.echo('series started')
if __name__ == '__main__': cli()
