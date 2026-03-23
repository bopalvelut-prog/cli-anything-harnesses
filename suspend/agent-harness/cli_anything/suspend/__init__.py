import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suspend running')
@cli.command()
def start(): click.echo('suspend started')
if __name__ == '__main__': cli()
