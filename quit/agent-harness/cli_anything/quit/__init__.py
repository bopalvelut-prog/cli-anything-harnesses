import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quit running')
@cli.command()
def start(): click.echo('quit started')
if __name__ == '__main__': cli()
