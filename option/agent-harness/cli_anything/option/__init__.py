import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('option running')
@cli.command()
def start(): click.echo('option started')
if __name__ == '__main__': cli()
