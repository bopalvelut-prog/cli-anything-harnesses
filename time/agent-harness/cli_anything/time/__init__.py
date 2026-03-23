import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('time running')
@cli.command()
def start(): click.echo('time started')
if __name__ == '__main__': cli()
