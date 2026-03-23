import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('catch running')
@cli.command()
def start(): click.echo('catch started')
if __name__ == '__main__': cli()
