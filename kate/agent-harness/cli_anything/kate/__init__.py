import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kate running')
@cli.command()
def start(): click.echo('kate started')
if __name__ == '__main__': cli()
