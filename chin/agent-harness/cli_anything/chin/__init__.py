import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chin running')
@cli.command()
def start(): click.echo('chin started')
if __name__ == '__main__': cli()
