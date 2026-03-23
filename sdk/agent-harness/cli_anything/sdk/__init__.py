import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sdk running')
@cli.command()
def start(): click.echo('sdk started')
if __name__ == '__main__': cli()
