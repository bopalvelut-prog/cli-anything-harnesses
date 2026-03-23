import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rice running')
@cli.command()
def start(): click.echo('rice started')
if __name__ == '__main__': cli()
