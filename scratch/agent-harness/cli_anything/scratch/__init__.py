import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scratch running')
@cli.command()
def start(): click.echo('scratch started')
if __name__ == '__main__': cli()
