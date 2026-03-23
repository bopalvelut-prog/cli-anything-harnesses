import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('champion running')
@cli.command()
def start(): click.echo('champion started')
if __name__ == '__main__': cli()
