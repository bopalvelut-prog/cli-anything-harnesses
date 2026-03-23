import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('station running')
@cli.command()
def start(): click.echo('station started')
if __name__ == '__main__': cli()
