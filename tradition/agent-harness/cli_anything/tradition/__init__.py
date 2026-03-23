import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tradition running')
@cli.command()
def start(): click.echo('tradition started')
if __name__ == '__main__': cli()
