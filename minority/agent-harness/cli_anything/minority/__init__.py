import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minority running')
@cli.command()
def start(): click.echo('minority started')
if __name__ == '__main__': cli()
