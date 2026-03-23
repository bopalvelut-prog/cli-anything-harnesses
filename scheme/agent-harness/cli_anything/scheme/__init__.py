import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scheme running')
@cli.command()
def start(): click.echo('scheme started')
if __name__ == '__main__': cli()
