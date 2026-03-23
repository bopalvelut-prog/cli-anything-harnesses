import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prelude running')
@cli.command()
def start(): click.echo('prelude started')
if __name__ == '__main__': cli()
