import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ceremony running')
@cli.command()
def start(): click.echo('ceremony started')
if __name__ == '__main__': cli()
