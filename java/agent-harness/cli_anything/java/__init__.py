import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('java running')
@cli.command()
def start(): click.echo('java started')
if __name__ == '__main__': cli()
