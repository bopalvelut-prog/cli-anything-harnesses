import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('possible running')
@cli.command()
def start(): click.echo('possible started')
if __name__ == '__main__': cli()
