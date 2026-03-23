import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('embrace running')
@cli.command()
def start(): click.echo('embrace started')
if __name__ == '__main__': cli()
