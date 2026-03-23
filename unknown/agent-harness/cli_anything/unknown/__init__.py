import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unknown running')
@cli.command()
def start(): click.echo('unknown started')
if __name__ == '__main__': cli()
