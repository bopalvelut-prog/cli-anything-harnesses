import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stop running')
@cli.command()
def start(): click.echo('stop started')
if __name__ == '__main__': cli()
