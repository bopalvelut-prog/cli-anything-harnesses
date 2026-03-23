import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('machine running')
@cli.command()
def start(): click.echo('machine started')
if __name__ == '__main__': cli()
