import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('landoop running')
@cli.command()
def start(): click.echo('landoop started')
if __name__ == '__main__': cli()
