import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('triggers running')
@cli.command()
def start(): click.echo('triggers started')
if __name__ == '__main__': cli()
