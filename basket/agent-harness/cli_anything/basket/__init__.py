import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('basket running')
@cli.command()
def start(): click.echo('basket started')
if __name__ == '__main__': cli()
