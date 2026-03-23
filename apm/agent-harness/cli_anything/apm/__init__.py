import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apm running')
@cli.command()
def start(): click.echo('apm started')
if __name__ == '__main__': cli()
