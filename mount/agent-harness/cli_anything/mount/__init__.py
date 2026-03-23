import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mount running')
@cli.command()
def start(): click.echo('mount started')
if __name__ == '__main__': cli()
