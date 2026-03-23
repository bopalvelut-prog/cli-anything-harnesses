import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('century running')
@cli.command()
def start(): click.echo('century started')
if __name__ == '__main__': cli()
