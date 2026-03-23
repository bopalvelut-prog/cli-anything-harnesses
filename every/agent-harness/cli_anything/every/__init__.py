import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('every running')
@cli.command()
def start(): click.echo('every started')
if __name__ == '__main__': cli()
