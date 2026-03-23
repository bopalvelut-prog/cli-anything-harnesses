import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aom running')
@cli.command()
def start(): click.echo('aom started')
if __name__ == '__main__': cli()
