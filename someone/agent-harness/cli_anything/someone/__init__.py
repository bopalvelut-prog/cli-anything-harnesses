import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('someone running')
@cli.command()
def start(): click.echo('someone started')
if __name__ == '__main__': cli()
