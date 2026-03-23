import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('education running')
@cli.command()
def start(): click.echo('education started')
if __name__ == '__main__': cli()
