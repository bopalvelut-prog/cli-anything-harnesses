import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pt running')
@cli.command()
def start(): click.echo('pt started')
if __name__ == '__main__': cli()
