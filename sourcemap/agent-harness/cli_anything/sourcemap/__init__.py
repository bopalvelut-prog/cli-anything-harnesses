import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sourcemap running')
@cli.command()
def start(): click.echo('sourcemap started')
if __name__ == '__main__': cli()
