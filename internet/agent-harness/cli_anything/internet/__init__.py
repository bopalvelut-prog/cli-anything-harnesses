import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('internet running')
@cli.command()
def start(): click.echo('internet started')
if __name__ == '__main__': cli()
