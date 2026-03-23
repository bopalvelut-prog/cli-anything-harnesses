import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('isolate running')
@cli.command()
def start(): click.echo('isolate started')
if __name__ == '__main__': cli()
