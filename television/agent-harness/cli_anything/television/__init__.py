import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('television running')
@cli.command()
def start(): click.echo('television started')
if __name__ == '__main__': cli()
