import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hour running')
@cli.command()
def start(): click.echo('hour started')
if __name__ == '__main__': cli()
