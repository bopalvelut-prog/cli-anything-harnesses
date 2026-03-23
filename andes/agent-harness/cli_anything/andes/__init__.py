import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('andes running')
@cli.command()
def start(): click.echo('andes started')
if __name__ == '__main__': cli()
