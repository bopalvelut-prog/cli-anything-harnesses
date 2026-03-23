import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('iron running')
@cli.command()
def start(): click.echo('iron started')
if __name__ == '__main__': cli()
