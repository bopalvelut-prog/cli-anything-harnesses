import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resign running')
@cli.command()
def start(): click.echo('resign started')
if __name__ == '__main__': cli()
