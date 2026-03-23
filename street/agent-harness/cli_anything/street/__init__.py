import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('street running')
@cli.command()
def start(): click.echo('street started')
if __name__ == '__main__': cli()
