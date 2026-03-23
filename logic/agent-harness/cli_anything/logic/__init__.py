import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('logic running')
@cli.command()
def start(): click.echo('logic started')
if __name__ == '__main__': cli()
