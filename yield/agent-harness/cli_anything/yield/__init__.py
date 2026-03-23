import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yield running')
@cli.command()
def start(): click.echo('yield started')
if __name__ == '__main__': cli()
