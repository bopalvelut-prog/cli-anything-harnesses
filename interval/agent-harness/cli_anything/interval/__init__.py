import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('interval running')
@cli.command()
def start(): click.echo('interval started')
if __name__ == '__main__': cli()
