import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autom running')
@cli.command()
def start(): click.echo('autom started')
if __name__ == '__main__': cli()
