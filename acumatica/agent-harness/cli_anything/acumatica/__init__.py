import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('acumatica running')
@cli.command()
def start(): click.echo('acumatica started')
if __name__ == '__main__': cli()
