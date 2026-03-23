import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('receive running')
@cli.command()
def start(): click.echo('receive started')
if __name__ == '__main__': cli()
