import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mycli running')
@cli.command()
def start(): click.echo('mycli started')
if __name__ == '__main__': cli()
