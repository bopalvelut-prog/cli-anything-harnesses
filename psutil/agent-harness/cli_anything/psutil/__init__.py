import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('psutil running')
@cli.command()
def start(): click.echo('psutil started')
if __name__ == '__main__': cli()
