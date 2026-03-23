import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('acquia running')
@cli.command()
def start(): click.echo('acquia started')
if __name__ == '__main__': cli()
