import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grey running')
@cli.command()
def start(): click.echo('grey started')
if __name__ == '__main__': cli()
