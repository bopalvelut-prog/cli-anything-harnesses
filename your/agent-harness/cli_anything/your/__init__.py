import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('your running')
@cli.command()
def start(): click.echo('your started')
if __name__ == '__main__': cli()
