import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('val running')
@cli.command()
def start(): click.echo('val started')
if __name__ == '__main__': cli()
