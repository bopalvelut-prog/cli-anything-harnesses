import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('infinity running')
@cli.command()
def start(): click.echo('infinity started')
if __name__ == '__main__': cli()
