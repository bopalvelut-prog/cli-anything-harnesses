import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('neighbor running')
@cli.command()
def start(): click.echo('neighbor started')
if __name__ == '__main__': cli()
