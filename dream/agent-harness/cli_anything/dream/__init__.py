import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dream running')
@cli.command()
def start(): click.echo('dream started')
if __name__ == '__main__': cli()
