import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('caml running')
@cli.command()
def start(): click.echo('caml started')
if __name__ == '__main__': cli()
