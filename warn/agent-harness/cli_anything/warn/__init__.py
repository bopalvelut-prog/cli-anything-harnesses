import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warn running')
@cli.command()
def start(): click.echo('warn started')
if __name__ == '__main__': cli()
