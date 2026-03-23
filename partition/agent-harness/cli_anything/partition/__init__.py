import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('partition running')
@cli.command()
def start(): click.echo('partition started')
if __name__ == '__main__': cli()
