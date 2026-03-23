import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pinia running')
@cli.command()
def start(): click.echo('pinia started')
if __name__ == '__main__': cli()
