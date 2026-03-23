import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('expect running')
@cli.command()
def start(): click.echo('expect started')
if __name__ == '__main__': cli()
