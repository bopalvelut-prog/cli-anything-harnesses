import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('employee running')
@cli.command()
def start(): click.echo('employee started')
if __name__ == '__main__': cli()
