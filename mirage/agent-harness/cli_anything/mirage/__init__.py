import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mirage running')
@cli.command()
def start(): click.echo('mirage started')
if __name__ == '__main__': cli()
